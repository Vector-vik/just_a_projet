"""Настройка API."""
import os
from typing import (
    Dict,
    Union,
)

import flask
from flask import Flask
from flask_restplus import Api
from sqlalchemy.orm.exc import NoResultFound
from werkzeug.exceptions import HTTPException

from base.logger import logger

ERROR_MESSAGE: Dict[str, Union[bool, str]] = {
    'success': False,
    'message': 'An unhandled exception occurred.',
}

DEBUG: bool = bool(os.environ.get('DEBUG', False))


def configure_app(flask_app):
    """Настройка приложения и БД."""
    db_url: str = os.environ.get('DB_URL', 'sqlite:///:memory:')
    db_name: str = os.environ.get('DB_NAME', 'test')

    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    flask_app.config['SQLALCHEMY_BINDS'] = {db_name: db_url}
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = 'list'
    flask_app.config['RESTPLUS_VALIDATE'] = True
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = True
    flask_app.config['ERROR_404_HELP'] = True
    flask_app.debug = DEBUG

    # Логирование запросов к БД
    flask_app.config['SQLALCHEMY_ECHO'] = False

    flask_app.url_map.strict_slashes = False


application = Flask(__name__)
configure_app(application)
authorizations: Dict[str, Dict[str, str]] = {
    'auth_token': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
    },
}

api = Api(
    application,
    doc='/swagger/' if DEBUG else None,  # Для отключения swagger на проде
    authorizations=authorizations,
    security='auth_token',
)


def _exc_handler(e):
    if isinstance(e, HTTPException) and 400 <= e.code < 500:
        logger.warning(str(e))
    else:
        logger.exception(e)

    if isinstance(e, HTTPException):
        return flask.jsonify({
            'success': False,
            'message': e.description,
        }), e.code
    return flask.jsonify(ERROR_MESSAGE), 500


@application.errorhandler(Exception)
def handle_500(e):
    """Обработка ошибки 500."""
    return _exc_handler(e)


@api.errorhandler
def default_error_handler(e):
    """Дефолтный обработчик ошибок."""
    return _exc_handler(e)


@api.errorhandler(NoResultFound)
def database_not_found_error_handler(_):
    """Обработчик ошибок БД."""
    logger.exception('A database result was required but none was found.')
    return flask.jsonify(ERROR_MESSAGE), 500

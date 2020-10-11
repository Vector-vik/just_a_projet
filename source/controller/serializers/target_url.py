"""Сериализатор данных для controller.target_url."""
from flask_restful.reqparse import RequestParser

from base import api


target_url_post_parser: RequestParser = api.parser()
target_url_post_parser.add_argument(
    name='target_url',
    required=True,
    type=str,
)

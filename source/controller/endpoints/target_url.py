"""Содержит ендпоинты для работы с сущностью ссылки сканирования."""
from typing import (
    Union,
    Dict,
)

from flask import request
from flask_restplus import (
    Namespace,
    Resource,
)
from flask_restplus.reqparse import ParseResult

from base import api
from controller.serializers import target_url_post_parser
from controller.use_cases import start_scan


target_url = Namespace('target_url', description='Target url endpoints')


@target_url.route('/target_url/')
class TargetUrl(Resource):
    """Работа с сылкой сканирования."""

    @api.expect(target_url_post_parser)
    def post(self) -> Dict[str, Union[bool, int]]:
        """Создание сканирования.

        Получение target-url от пользователя и сохранение его в PostgreSQL и
        запуск сканирования: отправка target-url worker'y.
        """
        data: ParseResult = target_url_post_parser.parse_args(request)
        scan_id: int = start_scan(
            target_url=data.target_url,
        )

        return {
            'success': bool(scan_id),
            'scan_id': scan_id,
        }

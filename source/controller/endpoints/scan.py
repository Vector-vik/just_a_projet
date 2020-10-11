"""Содержит ендпоинты для работы с сущностью сканирования."""
from typing import (
    Dict,
    Union,
    Optional,
)

import flask
from flask import request
from flask_restplus import (
    Namespace,
    Resource,
)
from flask_restplus.reqparse import ParseResult

from base import api
from controller.serializers import scan_post_parser
from controller.use_cases import (
    get_scan_info,
    update_scan_status,
    delete_scan,
)


scan = Namespace('scan', description='Scan endpoints')


@scan.route('/scan/<int:scan_id>')
class Scan(Resource):
    """Отдаёт token для продолженния kyc."""

    def get(self, scan_id: int) -> Dict[str, Union[str, int]]:
        """Получение данных о текущем статусе сканирования."""
        return get_scan_info(
            scan_id=scan_id,
        )

    @api.expect(scan_post_parser)
    def patch(self, scan_id: int) -> Dict[str, bool]:
        """Получение результатов сканирования от воркера."""
        data: ParseResult = scan_post_parser.parse_args(request)
        status: Optional[str] = data.status
        if not status:
            flask.abort(400)

        update_scan_status(
            scan_id=scan_id,
            status=data.status,
        )

        return {
            'success': True,
        }

    def delete(self, scan_id: int) -> Dict[str, bool]:
        """Удаление данных о сканировании и его результатах."""
        success: bool = delete_scan(
            scan_id=scan_id,
        )

        return {
            'success': success,
        }

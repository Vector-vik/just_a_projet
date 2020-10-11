"""Сериализатор данных для controller.scan."""
from flask_restful.reqparse import RequestParser

from base import api
from controller.models import ScanStatus

scan_post_parser: RequestParser = api.parser()
scan_post_parser.add_argument(
    name='status',
    required=True,
    type=lambda x: x if x in [
        status.value for status in list(ScanStatus)
    ] else None,
)

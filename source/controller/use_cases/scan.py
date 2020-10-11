"""Кейсы бизнес логики по работе со сканированием."""
import os
import ujson
from typing import (
    Dict,
    Union,
)

from base import (
    logger,
    channel,
)
from controller import queries
from controller.models import Scan


def start_scan(target_url: str) -> int:
    """
    Бизнес логика начала сканирования.

    :param target_url: Ссылка которую необходимо найти.
    :return: 0, если не получилось начать сканирование.
    """
    if len(target_url) > 100:
        return 0

    try:
        scan_id: int = queries.create_scan(
            target_url=target_url,
        )

        data: Dict[str, Union[str, int]] = {
            'scan_id': scan_id,
            'target_url': target_url,
        }

        channel.basic_publish(
            exchange='',
            routing_key=os.environ.get('QUEUE_NAME', 'unknown'),
            body=ujson.dumps(data),
        )

    except Exception as error:  # Тут лучше отлавливать конкретные исключения
        logger.exception(error)
        return 0
    else:
        return scan_id


def get_scan_info(scan_id: int) -> Dict[str, Union[str, int]]:
    """
    Бизнес логика получения данных по сканированию.

    :param scan_id: Идентификатор сканирования.
    :return: Удобный формат данных для фронта с информацией по сканированию.
    """
    scan: Scan = queries.get_scan(
        scan_id=scan_id,
    )

    if not scan:
        return {
            'message': 'Wrong scan_id',
        }

    status: str = scan.status.value if scan.status else 'Unknown'
    return {
        'scan_id': scan.scan_id,
        'target_url': scan.target_url,
        'status': status,
    }


def update_scan_status(scan_id: int, status: str) -> None:
    """
    Бизнес логика обновления статуса сканирования.

    :param scan_id: Идентификатор сканирования.
    :param status: Статус сканирования.
    """
    queries.update_scan(
        scan_id=scan_id,
        status=status,
    )


def delete_scan(scan_id: int) -> bool:
    """
    Бизнес логика по удалению сканирования.

    :param scan_id: Идентификатор сканирования.
    :return: True, если получилось удалить сканирование.
    """
    scan: Scan = queries.get_scan(
        scan_id=scan_id,
    )
    if not scan:
        return False

    status: str = scan.status.value if scan.status else 'Unknown'
    queries.create_deleted_scan(
        scan_id=scan.scan_id,
        target_url=scan.target_url,
        status=status,
    )

    queries.delete_scan(
        scan_id=scan_id,
    )

    return True

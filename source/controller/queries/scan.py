"""Запросы для работы с сущностью сканирования."""
from base import db

from controller.models import (
    Scan,
    ScanStatus,
)


def create_scan(target_url: str) -> int:
    """Создание сканирования.

    :param target_url: Ссылка которую необходимо найти.
    :return: Идентификатор созданного сканирования.
    """
    scan: Scan = Scan(
        target_url=target_url,
        status=ScanStatus.PENDING.value,
    )
    db.session.add(scan)
    db.session.commit()

    return scan.scan_id


def get_scan(scan_id: int) -> Scan:
    """Получение результатов сканирования.

    :param scan_id: Идентификатор сканирования.
    :return: Текущее состояние сканирования.
    """
    return Scan.query.filter(
        Scan.scan_id == scan_id,
    ).first()


def update_scan(scan_id: int, status: str) -> None:
    """Обновление статуса сканирования.

    :param scan_id: Идентификатор сканирования.
    :param status: Статус сканирования.
    """
    Scan.query.filter(
        Scan.scan_id == scan_id,
    ).update({
        Scan.status: status,
    })
    db.session.commit()


def delete_scan(scan_id: int) -> None:
    """Удаление сканирования из базы.

    :param scan_id: Идентификатор сканирования.
    """
    Scan.query.filter(
        Scan.scan_id == scan_id,
    ).delete()
    db.session.commit()

"""Запросы для работы с сущностью удалённого сканирования."""
from base import db

from controller.models import DeletedScan


def create_deleted_scan(scan_id: int, target_url: str, status: str) -> None:
    """Создание сканирования.

    :param scan_id: Идентификатор сканирования, который удалили.
    :param target_url: Ссылка которую необходимо найти.
    :param status: Статус сканирования.
    """
    scan: DeletedScan = DeletedScan(
        scan_id=scan_id,
        target_url=target_url,
        status=status,
    )
    db.session.add(scan)
    db.session.commit()

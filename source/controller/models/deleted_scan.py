"""Описание таблицы controller.deleted_scan."""
from base import db

from controller.models.scan import ScanStatus


class DeletedScan(db.Model):
    """Модель таблицы."""

    __tablename__: str = 'deleted_scan'

    deleted_scan_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        comment='Идентификатор удалённоего сканирования',
    )

    scan_id = db.Column(
        db.Integer,
        nullable=False,
        comment='Идентификатор сканирования, которое удалали',
    )

    target_url = db.Column(
        db.String(100),
        nullable=False,
        comment='Ссылка которую необходимо найти',
    )

    status = db.Column(
        db.Enum(ScanStatus),
        on_default=ScanStatus.PENDING.value,
        comment='Статус сканирования',
    )

    def __repr__(self):
        return f'<Deleted scan {self.scan_id} - {self.status}>'


db.Index(
    'deleted_scan_id',
    DeletedScan.deleted_scan_id,
    unique=True,
)

db.Index(
    'deleted_scan_status',
    DeletedScan.status,
    unique=False,
)

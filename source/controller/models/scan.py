"""Описание таблицы controller.scan."""
import enum

from base import db


class ScanStatus(enum.Enum):
    """Enum для статуса сканирования."""

    PENDING = 'PENDING'
    IN_PROGRESS = 'IN_PROGRESS'
    SUCCESS = 'SUCCESS'
    FAILED = 'FAILED'


class Scan(db.Model):
    """Модель таблицы."""

    __tablename__: str = 'scan'

    scan_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        comment='Идентификатор сканирования',
    )

    target_url = db.Column(
        db.String(100),
        nullable=False,
        comment='Ссылка которую необходимо найти',
    )

    status = db.Column(
        db.Enum(ScanStatus),
        nullable=False,
        comment='Статус сканирования',
    )

    def __repr__(self):
        return f'<Scan {self.scan_id} - {self.status}>'


db.Index(
    'scan_id',
    Scan.scan_id,
    unique=True,
)

db.Index(
    'status',
    Scan.status,
    unique=False,
)

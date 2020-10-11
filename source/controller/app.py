"""Сборка и запуск сервиса."""
import os

from base import (
    api,
    application,
    db,
)
from controller import (
    models,
    endpoints,
)

MODELS = [
    models.scan,
    models.deleted_scan,
]

app_name: str = os.environ.get('APP_NAME', 'Unknown app')
app_version: str = os.environ.get('APP_VERSION', 'v0.0')

api.title = app_name
api.version = app_version

# Настройка бд
db.init_app(application)
db.app = application
db.create_all()

# Настройка endpoints
api.add_namespace(
    ns=endpoints.target_url,
    path=f'/{app_name}/{app_version}',
)

api.add_namespace(
    ns=endpoints.scan,
    path=f'/{app_name}/{app_version}',
)


if __name__ == '__main__':
    application.run(port=5000)

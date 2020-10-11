"""Бизнес логика по сканированию для воркера."""
import ujson
from typing import (
    Dict,
    Union,
)

import requests

PAGE: str = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Title</title>
</head>
<body>
<a href="https://www.rabbitmq.com/getstarted.html">RabbitMQ</a>
<a href="https://docs.python.org/3/library/asyncio.html">asyncio</a>
<a href="https://github.com/">Github</a>
<a href="https://www.rabbitmq.com/getstarted.html">RabbitMQ again</a>
</body>
</html>
"""


def scan(*args, **kwargs):
    """Бизнес логика сканирования."""
    data: Dict[str, Union[str, int]] = ujson.loads(args[3].decode('utf-8'))

    scan_id: int = data.get('scan_id', 0)
    target_url: int = data.get('target_url', 0)

    if target_url in PAGE:
        status = 'SUCCESS'
    else:
        status = 'FAILED'

    requests.patch(
        f'http://127.0.0.1:5000/controller/v0.1/scan/{scan_id}',
        data={
            'status': status,
        },
    )

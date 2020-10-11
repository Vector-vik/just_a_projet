"""Создание очереди."""
import os

import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('0.0.0.0'),  # noqa:S104
)
channel = connection.channel()
channel.queue_declare(
    queue=os.environ.get('QUEUE_NAME', 'unknown'),
    durable=True,
)

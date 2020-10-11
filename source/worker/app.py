"""Приложение по сканированию."""
import os

from base import channel
from worker.use_cases import scan


if __name__ == '__main__':
    channel.basic_consume(
        queue=os.environ.get('QUEUE_NAME', 'unknown'),
        on_message_callback=scan,
        auto_ack=True,
    )

    channel.start_consuming()

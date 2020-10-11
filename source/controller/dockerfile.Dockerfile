FROM python:3.7.3
MAINTAINER Viktor Sergeev <sergeevviktorsergeevich@yandex.ru>

ENV PORT=5000
ENV HOST=0.0.0.0
ENV WORKERS=10

WORKDIR /opt/project

RUN apt install default-libmysqlclient-dev -y
RUN pip install gunicorn[gevent]

ADD requirements.txt /opt/project
RUN pip install -r requirements.txt

ADD source/base /opt/project/source/base
ADD source/controller /opt/project/source/controller

WORKDIR /opt/project/source

CMD exec gunicorn --pythonpath=/opt/project/source/ --bind $HOST:$PORT --workers=$WORKERS --max-requests 250 -t 45 --reload controller.app

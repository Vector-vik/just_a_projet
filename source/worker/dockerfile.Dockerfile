FROM python:3.7.3
MAINTAINER Viktor Sergeev <sergeevviktorsergeevich@yandex.ru>

WORKDIR /opt/project/

RUN apt install default-libmysqlclient-dev -y

ADD requirements.txt /opt/project
RUN pip install -r requirements.txt

ADD source/base /opt/project/source/base
ADD source/worker /opt/project/source/worker

WORKDIR /opt/project/source

CMD exec python3.7 -m worker.app
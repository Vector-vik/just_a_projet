# Тестовое задание

Добро пожаловать в тесовое задание, на что стоит обратить внимание 
перед проверкой:

* Код и файлы расположенные в пакете base не являются объектом рассмотрения 
моего скила, они необходимы для выполнения задания, но писать их нормально, 
писать к ним фасады заняло бы ещё больше времени. Это некая база над 
библиотеками которые в теории есть по умолчанию у каждого проекта.
* Некоторые вещи например докстринги на русском языке не стоит обращать 
внимание ибо просто так принято писать на моём текущем проекте, это 
обсуждаемая вещь и изменяемая
* В тестовом задании есть проблема, ничего не говориться про файл о том как его
передавать и получать и где искать, так что я сделал на своё усмотрение
* https://aio-pika.readthedocs.io/en/latest/quick-start.html
* 
* 
* 
* 
* 
* 

## Запуск сервиса
Всё вместе
````
docker-compose -f docker_compose.yml up --build -d services
````

или же можно отдельно:
````
docker-compose -f docker_compose.yml up --build -d controller
docker-compose -f docker_compose.yml up --build -d worker
docker-compose -f docker_compose.yml up --build -d postgresql
docker-compose -f docker_compose.yml up --build -d rabbitmq
````

Maintainer: Viktor Sergeev
cell: 8(999)242-82-91
tg: @iwannabeurfly

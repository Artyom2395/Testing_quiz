# Testing_quiz
Шаг 1: Установите Docker
Вы можете загрузить Docker для своей операционной системы с официального сайта Docker: https://docs.docker.com/get-docker/
Шаг 2: Клонируйте репозиторий
Склонируйте этот репозиторий с GitHub на ваш локальный компьютер:
```
git clone <URL репозитория>
``` 
Шаг 3: Перейдите в каталог проекта
Перейдите в каталог вашего проекта:
```
cd <название-каталога-проекта>
``` 
Шаг 4: Сборка Docker образов
В этом приложении есть три файла: Dockerfile для PostgreSQL, Dockerfile.web для приложения, файл docker-compose.yaml для настройки проекта, выглядит так
```
services:
  db:
    container_name: mydbcontainer
   build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "5432:5432"
    volumes:
      - ./db_data:/var/lib/postgresql/data

  web:
    container_name: mywebcontainer
    build:
      context: .
      dockerfile: Dockerfile.web
    ports:
      - "8000:8000"
    depends_on:
      - db
```
Здесь мы создаем два сервиса: db и web. db представляет собой контейнер для PostgreSQL базы данных, и мы прокидываем порт 5432 для доступа к базе данных. 
В web сервисе мы указываем, что он зависит от db, чтобы подождать, пока база данных будет готова к подключению.
Далее мы соберем Docker образы. Убедитесь, что вы находитесь в каталоге вашего проекта и выполните следующую команду для сборки образов:
```
docker-compose build
``` 
Эта команда выполнит сборку образов на основе ваших Dockerfile файлов. Образы будут названы myproject_db для базы данных и myproject_web для вашего веб-сервиса.
Шаг 5: Запуск контейнеров
Теперь, когда образы созданы, вы можете запустить контейнеры, используя следующую команду:
```
docker-compose up
``` 
Это запустит два контейнера: mydbcontainer для базы данных PostgreSQL и mywebcontainer для вашего FastAPI приложения.
Шаг 6: Проверка приложения
Тестируем работу приложения(н-р, Postman)
Отправляем post запрос на url http://0.0.0.0:8000/questions/
в body > raw > втаявляем следующий запрос 
```
{
    "questions_num": 3
}
```
Шаг 6: Завершение работы
Чтобы завершить работу приложения и остановить контейнеры, выполните следующую команду:
```
docker-compose down
```
Это остановит и удалит контейнеры.

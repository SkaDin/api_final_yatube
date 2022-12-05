# **api_final**
## Автор: 
### *Сушков Денис*
## Описание: 
### api final - это REST API для блог-платформы Yatube. Позволяет просматривать и отправлять посты, просматривать группы, подписываться на авторов.
## Как запустить проект:
### Клонировать репозиторий и перейти в него в командной строке:

    git clone git@github.com:SkaDin/api_final_yatube.git
    cd api_final_yatube
### Cоздать и активировать виртуальное окружение:

    python -m venv venv
    source vens/Scripts/activate
### Установить зависимости из файла requirements.txt:

    python -m pip install --upgrade pip
    pip install -r requirements.txt
### Выполнить миграции:

    python manage.py migrate
### Запустить проект:

    python manage.py runserver
## Примеры запросов:
### Запрос на получение JWT-токена:
```
  [POST].../api/v1/jwt/create/
  {
    "username": "User",
    "password": "Change_Me"
}
```
### Ответ:
```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3MDM0NTgxNCwianRpIjoiODYyYTM3MjY4ZTg4NGMwZGE0NDAzNTE1YTgzZGZmOGMiLCJ1c2VyX2lkIjoyfQ.eCpp2n0eKh5CEPh-8Tk6qMpwtjdtCCnlfrBpdbWDN_Q",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcwMjU5NzE0LCJqdGkiOiJkZTRiMTBlMDEwYzA0NTcyYmQ3ZmYwZTIxYTFmOWRiMSIsInVzZXJfaWQiOjJ9.e8Ket6Wh1df3TJZIKElAyZua34RIuNhKdii0fXhBwfc"
}
```

### Запрос с использованием токена пользователя User для публикации поста:
```
    [POST].../api/v1/posts/
    {
    "text": "Тестовый текст"
    }
```
### Ответ:
```
[
    {
        "id": 1,
        "text": "Тестовый текс",
        "author": "User",
        "image": null,
        "group": null,
        "pub_date": "2022-12-05T16:48:48.645052Z"
    }
]
```
### Подробная документация в формате ReDoc доступна по адресу .../redoc/

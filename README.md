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

    python -m venv env
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
    "password": "123456789d"
}
```

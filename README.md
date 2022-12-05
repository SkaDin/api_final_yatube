# api_final_yatube
## Автор проекта: Сушков Денис





<h1>Как запустить проект:</h1>
Клонировать репозиторий и перейти в него в командной строке:

git clone git@github.com:SkaDin/api_final_yatube.git
cd kittygram
Cоздать и активировать виртуальное окружение:

python -m venv env
source vens/Scripts/activate
Установить зависимости из файла requirements.txt:

python -m pip install --upgrade pip
pip install -r requirements.txt
Выполнить миграции:

python manage.py migrate
Запустить проект:

python manage.py runserver

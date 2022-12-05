<h1>Как запустить проект:</h1>
Клонировать репозиторий и перейти в него в командной строке:

git clone git@github.com:SkaDin/api_final_yatube.git
cd kittygram
Cоздать и активировать виртуальное окружение:

python3 -m venv env
source vens/Scripts/activate
Установить зависимости из файла requirements.txt:

python3 -m pip install --upgrade pip
pip install -r requirements.txt
Выполнить миграции:

python3 manage.py migrate
Запустить проект:

python3 manage.py runserver

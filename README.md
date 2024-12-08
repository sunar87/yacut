# Учебный проект YaCut
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/en/2.3.x/)
[![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/index.html)

```YaCut``` - это сервис укорачивания ссылок, реализованный на фреймворке Flask.<br>
Цель проекта - отработать навыки работы с Flask и SQLAlchemy.

## Технологии
- Python 3.9
- Flask 2.0.2
- SQLAlchemy 1.4.29
- Alembic 1.7.5
- WTForms 3.0.1

## Описание сервиса
Назначение YaCut — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

Возможности сервиса:
- генерация коротких ссылок и связь их с исходными длинными ссылками,
- переадресация на исходный адрес при обращении к коротким ссылкам.
### Пользовательский интерфейс
Пользовательский интерфейс сервиса представляет собой страницу с формой.<br>
В форме предусмотрены два поля для ввода: 
- поле для исходной длинной ссылки,
- необязательное поле для пользовательского варианта короткой ссылки. 

### API интерфейс
Сервис обслуживает два эндпоинта:
- ```/api/id/``` — POST-запрос на создание новой короткой ссылки;
- ```/api/id/<short_id>/``` — GET-запрос на получение оригинальной ссылки по указанному короткому идентификатору.

Примеры запросов к API, варианты ответов и ошибок приведены в файле спецификации openapi.yml. Для удобной работы с документом воспользуйтесь онлайн-редактором [Swagger Editor].

### База данных
В проекте настроено подключение к базе данных через ORM SQLAlchemy.<br> Миграции базы данных настроены через библиотеку Alembic.


## Как развернуть проект на компьютере:
1. Клонировать репозиторий c GitHub на компьютер и перейти в него в командной строке
```
$ git clone https://github.com/sunar87/yacut.git
$ cd yacut
```
2. Создать и активировать виртуальное окружение
```
# Windows
$ python -m venv venv
$ source venv/Scripts/activate

# Linux
python3 -m venv venv
source venv/bin/activate
```
3. Обновить менеджер пакетов pip
```
$ python -m pip install --upgrade pip
```
4. Установить зависимости из requirements.txt
```
$ pip install -r requirements.txt
```
5. Создать файл .env с переменными окружения. Пример наполнения:
```
FLASK_APP=yacut
FLASK_ENV=development
SECRET_KEY= MY_SECRET_KEY
DATABASE_URI=sqlite:///db.sqlite3
```
6. Создать базу данных
```
$ flask db upgrade
```

### Лицензия
The MIT License (MIT)

### Автор проекта
Python backend developer,<br>
Войтов Семён

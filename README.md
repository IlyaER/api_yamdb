# api_yamdb
api_yamdb


### Запуск проекта в dev-режиме
- Установите и активируйте виртуальное окружение
```
python -m venv venv
```
#### Activate
```
	venv\Scripts\activate
```
(для отключения виртуального окружения)
```
	deactivate
```
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- В корневой папке выполните команды:
```
python api_yamdb\manage.py makemigrations
python api_yamdb\manage.py migrate
```
- если база данных пустая, то для создания суперпользователя выполните команду:
```
python api_yamdb\manage.py createsuperuser
```
- запустите сервер
```
python api_yamdb\manage.py runserver
```
В дальнейшем для запуска нужно выполнять только последнюю команду.


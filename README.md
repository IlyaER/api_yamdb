# Проект YaMDb


## Описание


### API
Основной функционал.

## Основные технологии

+ Django
+ djangorestframework
+ djangorestframework-simplejwt
+ PyJWT

## Импорт данных

Набор данных находится в папке ```api_yamdb/static/data``` 
Для запуска импорта выполните

```
python3 manage.py load_data
```

## Запуск проекта

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

##
[Документация проекта -> {{server}}/redoc/](http://localhost:8000/redoc/)

## Примеры

----

Проект: [Яндекс.Практикум](https://practicum.yandex.ru)  
Команда: 
+ [gseldon](https://github.com/gseldon)
...




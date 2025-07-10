# Куда пойти.

Cайт о самых интересных местах в Москве.

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в формате: `ПЕРЕМЕННАЯ=значение`.

Доступны следующие переменные:
- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.(Необязательная настройка)
- `ALLOWED_HOSTS` — Список строк, представляющих имена хостов/доменов, которые может обслуживать этот сайт Django.Записываетсяв виде `адрес1,адрес2,адрес3` Подробнее см. [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).
- `DATABASE_URL` — однострочный адрес к базе данных, например: `sqlite:///db.sqlite3`. Больше информации в [документации](https://github.com/jacobian/dj-database-url)
- `STATIC_ROOT` — папка, куда складывать статику (Необязательная настройка)
- `DB_ENGINE` — Серверная часть базы данных для использования. (Необязательная настройка)
Встроенные серверные базы данных:
  - 'django.db.backends.postgresql'
  - 'django.db.backends.mysql'
  - 'django.db.backends.sqlite3'
  - 'django.db.backends.oracle'
- `DB_NAME` — Имя используемой базы данных (Необязательная настройка)

`SECRET_KEY` — ключ шифрования паролей пользователей сайта, его можно получуить следуюющим образом:

```bash
python manage.py shell
>>> from django.core.management.utils import get_random_secret_key
>>> get_random_secret_key()
> 
```

Затем создайте и экспортируйте переменную окружения `SECRET_KEY`.

## Запуск
Для работы требуется [python](https://www.python.org/) версии 3.10. 
- Скачайте код
- Установите зависимости командой:
  
```bash
pip install -r requirements.txt
```

- Создайте файл базы данных и сразу примените все миграции командой:

```bash
python3 manage.py migrate
```

- Создайте и заполните переменные окружения
- Запустите сервер командой:

```bash
python3 manage.py runserver
```

### Для того, чтобы добавить новые места, используется скрипт *load_place.py*

Способ применения:

```bash
python manage.py load_place [аргументы] 
```

Поддерживаемые аргументы:
* *--url* или *-u*

Импорт данных о месте по ссылке на JSON-файл.
Пример:

```bash
python manage.py load_place --url https://example.com/place.json
```

* *--path* или *-p*

Импорт данных о месте из локального JSON-файла.
Пример:

```bash
python manage.py load_place --path ./data/place.json
```

* *--demo* или *-d*

Импорт списка мест из demo JSON-файла, содержащего массив URL-адресов JSON-описаний мест.
Пример:

```bash
python manage.py load_place --demo ./data/demo.json
```

### Примечания

* JSON-файл должен содержать следующую структуру:

```json
{
  "title": "Название места",
  "description_short": "Краткое описание",
  "description_long": "Полное описание",
  "coordinates": {
    "lat": 55.751244,
    "lng": 37.618423
  },
  "imgs": [
    "https://example.com/image1.jpg",
    "https://example.com/image2.jpg"
  ]
}
```

* В случае с --demo JSON-файл должен быть в формате:

```json
{
  "places": [
    "https://example.com/place1.json",
    "https://example.com/place2.json"
  ]
}
```

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).

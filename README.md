Вот простой, но полезный `README.md` для твоего проекта на Odoo 17, покрывающий все важные моменты:

---

````markdown
# My Product Thing — Odoo 17 Custom Module

## 📦 Описание
Модуль добавляет пользовательскую сущность **"Product Thing"** с полями:
- `name`: Название
- `production_date`: Дата производства
- `color`: Цвет (enum: red, blue, green, black, white)
- `weight`: Вес (float)

Реализованы:
- Табличное и карточное (форменное) отображение
- Цветовое отображение `color` в таблице
- Возможность **создавать записи только через форму**
- Возможность **редактировать записи через таблицу**
- Кнопка в форме, доступная по правам доступа

---

## 🧪 Требования
- Odoo 17
- PostgreSQL 15–17
- Docker / Docker Compose (рекомендуется)

---

## 🚀 Быстрый запуск (через Docker)

1. Клонируйте проект и перейдите в каталог:
```bash
git clone <repo_url>
cd my_project
````

2. Запустите контейнеры:

```bash
docker-compose up -d
```

3. Зайдите в Odoo:

* [http://localhost:8069](http://localhost:8069)
* Логин: `admin`
* Пароль: `admin`

---

## 🧩 Установка модуля

1. Перейдите в **Apps**
2. Нажмите **Update Apps List**
3. Найдите **My Product Thing**
4. Нажмите **Install**

---

## 👤 Права доступа

Созданы 3 группы:

* **User** – может редактировать и видеть кнопку только у своих записей
* **Limited** – видит кнопку, но не может редактировать чужие записи
* **Admin** – полный доступ ко всему

---

## 📂 Структура

```bash
my_module/
├── __init__.py
├── __manifest__.py
├── models/
│   └── product_thing.py
├── security/
│   ├── ir.model.access.csv
│   ├── ir.model.xml
│   └── security.xml
└── views/
    └── product_thing_views.xml
```

---

## ❓Полезные команды

* Обновить модуль (в dev):

```bash
./odoo-bin -u my_module -d <dbname> --dev=reload
```

---

## 🛠 Поддержка

Если что-то не работает — проверь:

* Правильность `model` в `access.csv`
* Метод, связанный с кнопкой
* Очистку кэша Odoo (`Update Apps List`)

---

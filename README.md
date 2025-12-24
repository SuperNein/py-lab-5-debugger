# Лабораторная работа 4
Симуляция с пользовательсĸими ĸоллеĸциями и псевдослучайной моделью

Вариант 1. «Библиотеĸа»

---

### Цель работы
- Освоить реализацию пользовательских коллекций
- Освоить работу с псевдослучайными моделями

---

### Структура проекта

```
lab-4-collections
│   .gitignore
│   .pre-commit-config.yaml
│   pyproject.toml
│   README.md
│   requirements.txt
│    
├───src
│   │   main.py
│   │   __init__.py
│   │   
│   ├───common
│   │       config.py
│   │       constants.py
│   │       __init__.py
│   │           
│   ├───enums
│   │       book_types.py
│   │       index.py
│   │       __init__.py
│   │           
│   └───services
│           book.py
│           book_collections.py
│           generators.py
│           library.py
│           simulation.py
│           __init__.py
│           
└───tests
        conftest.py
        tests_book.py
        tests_book_collections.py
        tests_library.py
        __init__.py
```

### Библиотеки

- typing
- logging
- enum
- pytest

---

### Установка и запуск

```
# Установка зависимостей
pip install -r requirements.txt

# Запуск
python -m src.main
```

---

### Реализация

#### Основные классы
- `Book` - базовый класс книги с атрибутами title, author, year, genre, isbn, borrowed.
- `DigitalBook` - подкласс цифровая книга с дополнительным атрибутом readers, без атрибута borrowed. Не может быть "взята", но имеет счетчик читателей.
- `Magazine` - подкласс журнал с дополнительным атрибутом issue.

#### События псевдослучайной симуляции
- Добавление книги
- Удаление книги
- Удаление случайно сгенерированной книги (высок шанс отсутствия в библиотеке)
- Поиск книги
- Замена книги

---

### Выводы

В ходе работы я научился:
- Создавать пользовательские списковые и словарные коллекции
- Работать с магическими методами классов
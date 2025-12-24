# Лабораторная работа 5

Отладĸа ĸодовой базы проеĸта на Python с помощью средств отладĸи

---

## Цели работы
- Заĸрепить навыĸи работы с отладчиĸом
- Сформировать понимания типовых логичесĸих и runtime-ошибоĸ
- Освоить методиĸи поисĸа, анализа и устранения ошибоĸ
- Развить умения объяснять причину неĸорреĸтного поведения программы

---

## Исходные данные
[Лабораторная работа 4](https://github.com/SuperNein/py-lab-4-collections)

---

## Структура проекта

```
lab-5-debugger
│   .gitignore
│   BUG_REPORT.md
│   README.md
│   
├───buggy_app
│   │   .log
│   │   .pre-commit-config.yaml
│   │   pyproject.toml
│   │   requirements.txt
│   │   
│   ├───src
│   │   │   main.py
│   │   │   __init__.py
│   │   │   
│   │   ├───common
│   │   │       config.py
│   │   │       constants.py
│   │   │       __init__.py
│   │   │           
│   │   ├───enums
│   │   │       book_types.py
│   │   │       index.py
│   │   │       __init__.py
│   │   │           
│   │   └───services
│   │           book.py
│   │           book_collections.py
│   │           generators.py
│   │           library.py
│   │           simulation.py
│   │           __init__.py
│   │           
│   └───tests
│           conftest.py
│           tests_book.py
│           tests_book_collections.py
│           tests_library.py
│           __init__.py
│           
└───screenshots
        bug_1_console.png
        bug_1_variables.png
        bug_2_console_logs.png
        bug_2_variables.png
        bug_3_console_logs.png
        bug_3_variables_after.png
        bug_3_variables_before.png
        bug_4_console_logs.png
        bug_4_variables_in.png
        bug_4_variables_out.png
        bug_5_console.png
        bug_5_variables_after.png
        bug_5_variables_before.png
```

---

## Ошибки
[Отчет об ошибках](./BUG_REPORT.md)

Все ошибки в `buggy_app` закомментированы и пронумерованы.

---

## Выводы
В ходе работы я освоил:
- Методики отладки программного кода
- Умения подобно объяснить причину некорректного поведения программы
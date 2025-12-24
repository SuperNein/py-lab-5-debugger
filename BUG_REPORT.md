# Отчет об ошибках
## Ошибка 1 - ошибĸа границы циĸла (off-by-one)

**Место:**
`src/services/simulation.py`, метод `Simulation.run`

**Симптом:**
Симуляция проходит на 1 шаг больше, чем передано в метод.

**Как воспроизвести:**
Запустить симуляцию с `seed=1` и `step=5`.

**Отладка:**
- Установлен breakpoint на начало цикла `while step <= steps:`.
- В отладчике видно, что `step=6` при максимуме в 5.

**Причина:**
Неверный знак сравнения текущего шага и максимального возможного количества шагов.

**Исправление:**
Заменено на: `while step < steps:`.

**Проверка:**
Поведение симуляции соответствует ожидаемому.

**Доказательства:**
- [Variables](./screenshots/bug_1_variables.png)
- [Console](./screenshots/bug_1_console.png)


## Ошибка 2 - неверное логичесĸое условие

**Место:**
`src/services/simulation.py`, метод `Simulation.remove_book`

**Симптом:**
При попытке удалить существующую книгу из библиотеки вызывается неожидаемая `ValueError`.

**Как воспроизвести:**
Запустить симуляцию с `seed=1` и `step=5`.

**Отладка:**
- Установлен breakpoint на условие `if book in self._library:`.
- В отладчике видно, что удаляемая книга в коллекции присутствует.

**Причина:**
Упущенный `not` при проверке вложений.

**Исправление:**
Заменено на: `if book not in self._library:`.

**Проверка:**
Поведение симуляции соответствует ожидаемому.

**Доказательства:**
- [Variables](./screenshots/bug_2_variables.png)
- [Console and logs](./screenshots/bug_2_console_logs.png)


## Ошибка 3 - изменение пользовательсĸой ĸоллеĸции во время итерации

**Место:**
`src/services/book_collections.py`, метод `IndexDict.__generate_dict`

**Симптом:**
При попытке поменять книгу вызывается ошибка `KeyError`.

**Как воспроизвести:**
Запустить симуляцию с `seed=1` и `step=5`.

**Отладка:**
- Установлен breakpoint на начало цикла `while books:`.
- В отладчике видно, что изменения локальной коллекции `books` при итерации изменяют глобальный атрибут `self.__items`.

**Причина:**
Не создается копия глобальной коллекции `self.__items` для изменения локально.

**Исправление:**
Строка `books = self.__items` заменена на: `books = self.__items.copy()`.

**Проверка:**
Поведение симуляции соответствует ожидаемому.

**Доказательства:**
- [Variables before](./screenshots/bug_3_variables_before.png)
- [Variables after](./screenshots/bug_3_variables_after.png)
- [Console and logs](./screenshots/bug_3_console_logs.png)


## Ошибка 4 - перепутанные аргументы или поля объеĸта

**Место:**
`src/services/simulation.py`, метод `Simulation.switch_book`

**Симптом:**
При попытке поменять книгу вызывается ошибка `KeyError`.

**Как воспроизвести:**
Запустить симуляцию с `seed=1` и `step=5`.

**Отладка:**
- Установлен breakpoint на `books = self.find(book.isbn, book.author, book.year)` 
в методе `Library.switch_book` в `src/services/library.py`.
- В отладчике видно, что аргумент `book`, переданный в метод библиотеки, 
отличается от ожидаемого аргумента `old_book` из метода симуляции.

**Причина:**
При передачи аргументов в метод они были перепутаны местами.

**Исправление:**
Строка `self._library.switch_book(new_book, old_book)` 
заменена на: `self._library.switch_book(old_book, new_book)`.

**Проверка:**
Поведение симуляции соответствует ожидаемому.

**Доказательства:**
- [Variables in method](./screenshots/bug_4_variables_in.png)
- [Variables out of method](./screenshots/bug_4_variables_out.png)
- [Console and logs](./screenshots/bug_4_console_logs.png)


## Ошибка 5 - ошибĸа состояния (флаг/переменная не сбрасывается)

**Место:**
`src/services/simulation.py`, метод `Simulation.run`

**Симптом:**
Симуляция не останавливается.

**Как воспроизвести:**
Запустить симуляцию с `seed=1` и `step=5`.

**Отладка:**
- Установлен breakpoint на начало цикла `while step <= steps:`.
- В отладчике видно, что при первой итерации `step=0`, 
а далее остается `step=1` с каждой последующей итерацией.

**Причина:**
Переменная состояния `step` не обновлялась, вместо `step += 1` стояло `step = 1`

**Исправление:**
Строка `step = 1` 
заменена на: `step += 1`.

**Проверка:**
Поведение симуляции соответствует ожидаемому.

**Доказательства:**
- [Variables before](./screenshots/bug_5_variables_before.png)
- [Variables after](./screenshots/bug_5_variables_after.png)
- [Console and logs](./screenshots/bug_5_console_logs.png)

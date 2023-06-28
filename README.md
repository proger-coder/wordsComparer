# wordsComparer

## Описание

wordsComparer - это микросервис, написанный на Python и использующий Flask. Он сравнивает два созвучных слова и возвращает результаты через два конечных пункта API.

## Установка и Запуск

Установите зависимости, указанные в файле `requirements.txt`:

```bash
pip install -r requirements.txt
```

Запустите сервис:

```bash
python fonetika.py
```

## API Endpoints

### GET `/`

Возвращает страницу с описанием сервиса в виде HTML. Эта страница содержит таблицу с информацией о других роутах.

### POST `/only_boolean`

Принимает JSON-объект вида `{given: string, answer: string, limit: int}`, где:
- `given` - слово из задания,
- `answer` - ответ,
- `limit` - предельное расстояние Левенштейна, при котором слова ещё считаются совпавшими.

Возвращает JSON-объект вида `{match: bool}`, где:
- `match` - результат совпадения.

### POST `/full_info`

Принимает JSON-объект вида `{given: string, answer: string}`, где:
- `given` - слово из задания,
- `answer` - ответ.

Возвращает JSON-объект вида `{given_word: string, answer_word: string, distance: int}`, где:
- `distance` - исчисленное расстояние Левенштейна.

## Используемые библиотеки и ресурсы

- Flask
- Язык: Python
- [Репозиторий проекта](https://github.com/proger-coder/wordsComparer)
- Сделано на основе [russian_soundex](https://github.com/roddar92/russian_soundex)

---

# rtk_test
Тестовое задание от Ростелеком

## Структура проекта
- tests.py - директория с тестами
- conftest.py - pytest фикстуры
- data.py - набор тестовых данных (сервисы, фильмы)
- http_requests.py - функции для работы с API
- pytest.ini - настройка pytest

## Тесты
1. Позитивные (фильм доступен для девайса, в прокате) - для всех типов девайсов
2. Фильм ещё не вышел в прокат (для всех типов девайсов)
3. Прокат фильма закончился (для всех типов девайсов)
4. Токен невалидный
5. Ключ в запросе невалидный

## Логирование
Чтобы включить логирование, нужно в pytest.ini указать log_cli=true
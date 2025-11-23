# UI-тестирование сайта Effective Mobile

## Описание

Автоматизированное тестирование сайта [https://effective-mobile.ru](https://effective-mobile.ru) с использованием **Playwright** и **PyTest**.

Тестируются переходы по разделам:
- О нас
- Вакансии
- Отзывы
- Контакты

Проект построен по паттерну Page Object.

---

## Запуск через Docker

1. Постройте Docker-образ:

`
docker build -t em-ui-tests .
`


2. Запустите ваш модуль тестирования:

`
docker run --rm em-ui-tests
`

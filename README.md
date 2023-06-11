# Test
## Установка
1) git clone https://github.com/margulanz/test.git
2) cd test
3) python -m venv venv
4) .\venv\scripts\activate
5) poetry install
6) manage.py runserver
## Эндпойнты
1) Создание теста -> `/test/`. При вызове этой ручки создается тест с уникальным логином (набор букв в 10 знаков) который будет возвращен в ответе и его можно будет использовать для прохождения теста.
2) Сохранить результаты теста IQ и время когда он был пройден -> `/test/scoreiq/`. Передаются набранные баллы от 0 до 50 и логин теста к которому нужно это прикрепить
3) Сохранить результаты теста EQ и время когда был пройден -> `/test/scoreeq/`. Передается упорядоченный список букв (размером в 5 элемента) из набора set(а, б, в, г, д)
4) Можно посмотреть текущий результат прохождения по заданному тесту -> `/test/results/<login>/`. Передается логин, в ответе получаю результаты 2 тестов (кол-во баллов, упорядоченный список букв которые ввел пользователь, время прохождения каждого теста и логин)

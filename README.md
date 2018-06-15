# Тестовое задание

## Требования: 
Python3, chromedriver

## Установка (Windows):
    
    python -m venv venv
    venv\scripts\activate
    git clone https://github.com/gh720/ql_test.git
    cd ql_test
    pip3 install -r requirements.txt

## Запуск (Windows):

* Добавить директорию, содержащую chromedriver в переменную Path

`set Path=Path-to-chromedriver;%Path%`

* Запустить тест:

`python3 -m unittest mail_ru_test.mail_ru_send_email_test`

* Можно также запустить вместе с тестами корректной и некорректной аутентификации

`python3 -m unittest mail_ru_test`
     

<h1><i>Инструкция для запуска проекта.</i></h1>


### (используется дистрибутив Ubuntu (wsl2))
---
Инструкция для запуска:
1) Произведите клонирование данного репозитория на локальный компьтер (`git clone https://github.com/annapyanova/practice.git`).
2) С помощью команды `python3 -m venv venv` установите виртуальное окружение.
3) Выполните `source venv/bin/activate` для его активации.
4) Перейдите в дирректорию **backend**.
5) Установите все необходимые зависимости из **requirements.txt** (`pip3 install -r requirements.txt`).
6) Запуск сервера осуществляется с помощью команды `uvicorn main:app --reload`.
7) После успешного запуска перейдите по адресу [localhost:8000/docs](http://localhost:8000/docs).

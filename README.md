<h1><i>Инструкция для запуска проекта</i></h1>

### Для запуска используется cmd.
---
Инструкция для запуска:
1) Произведите клонирование данного репозитория на локальный компьтер (`git clone https://github.com/annapyanova/practice.git`).
2) С помощью команды `python3 -m venv venv` установите виртуальное окружение.
3) Выполните `venv\Scripts\activate.bat` (`source venv/bin/activate` при использовании wsl2) для его активации.
4) Перейдите в дирректорию **backend**.
5) Установите все необходимые зависимости из **requirements.txt** (`pip3 install -r requirements.txt`).
6) Запуск сервера осуществляется с помощью команды `uvicorn main:app --reload`.
7) После успешного запуска перейдите по адресу [localhost:8000/docs](http://localhost:8000/docs).

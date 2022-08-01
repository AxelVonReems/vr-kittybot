## Проект VR-kittybot

"Данный проект представляет из себя модифицированную версию учебного Telegram-бота. В отличие от учебного проекта данный бот имеет доступ к 5 API, обращение к которым произходит при вводе команды или с использованием экранной клавиатуры. В процессе работы бота ведется логирование."

## Стек технологий

Python 3.9
Bot API Telegram 13.7
python-dotenv 0.19.0

## Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/AxelVonReems/vr-kittybot.git
```

Перейти в папку с проектом

```
cd vr-kittybot
```

Cоздать и активировать виртуальное окружение:

```
WIN: python -m venv venv
MAC: python3 -m venv venv
```

```
WIN: source venv/scripts/activate
MAC: source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
WIN: python -m pip install --upgrade pip
MAC: python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Зарегистрировать свою версию бота у телеграм-бота @BotFather. Для регистрации бота необходимо начать диалог с ботом @BotFather: нажмите кнопку Start («Запустить»). Затем отправьте команду "/newbot" и укажите параметры нового бота - имя и техническое имя (должно оканчиваться на bot).

Создать в корневой папке файл .env и указать в нем токен бота, полученный при его регистрации, в формате TOKEN=<ваш токен>.

Запустить проект:

```
WIN: python kittybot.py
MAC: python3 kittybot.py
```

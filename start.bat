@chcp 65001 >nul
@echo off
echo [INFO]Удаление всех __pycache__ и .pyc файлов...
for /d /r . %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d"
for /r %%f in (*.pyc) do del "%%f"


echo [INFO] Активация виртуального окружения...
call venv\Scripts\activate

echo [INFO] Установка зависимостей...
call pip install -r requirements.txt

echo [INFO] Запуск Telegram-бота...
python -m bot.main

echo.
echo [INFO] Бот завершил работу. Нажмите любую клавишу для выхода...
pause
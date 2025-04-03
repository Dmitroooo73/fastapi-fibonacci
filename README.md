FastAPI Fibonacci
Простое API на FastAPI для вычисления чисел Фибоначчи

 Описание
Этот проект предоставляет API-сервис на FastAPI, который вычисляет числа Фибоначчи.
API поддерживает:

Вычисление n-го числа Фибоначчи

Обработку граничных случаев (n = 0, отрицательные n)

Автотесты с TestClient

🔧 Установка и запуск

pip install fastapi uvicorn
uvicorn main:app --reload
Перейди на http://127.0.0.1:8000/docs, чтобы протестировать API.

🛠 Тестирование

pytest test_main.py

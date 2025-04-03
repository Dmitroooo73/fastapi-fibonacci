from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Сервер работает! Открой /docs для тестирования."}

@app.get("/fibonacci/{n}")
def fibonacci(n: int):
    if n < 0:
        return {"error": "N должно быть неотрицательным числом"}
    
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    
    return {"nth_fibonacci": a}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

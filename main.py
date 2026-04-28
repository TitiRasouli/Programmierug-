from fastapi import FastAPI

app = FastAPI()

@app.get("/double/{number}")
def double_number(number: int):
    return {"result": number * 2}
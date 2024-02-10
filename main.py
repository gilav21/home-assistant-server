# python -m uvicorn main:app --port 3000 --reload

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test/{id}")
async def test(id: int):
    return {"message": f"The id is {id}"}

@app.post("/test2")
async def test2(body: dict):
    return {"message": "This is a POST request with a body", "id is ": body["id"]}
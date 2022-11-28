# main.py
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def hello():
    return {"message":"Hello TutLinks.com"}

#uvicorn --port 5001 --host 127.0.0.1 main:app --reload

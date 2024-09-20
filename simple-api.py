from fastapi import FastAPI, Header
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/hello")
async def say_name(name: str | None = None, age: int | None = None) -> dict:
    return {"message": f"Hello {name}", "age": age}


class BookCreateModel(BaseModel):
    title: str
    author: str


@app.post("/create_book")
async def create_book(book_data: BookCreateModel):
    return {
        "title": book_data.title,
        "author": book_data.author,
    }


@app.get("/get_headers", status_code=201)
async def get_headers(
        accept:str = Header(None),
        content_type: str = Header(None),
        user_agent: str = Header(None),
        host: str = Header(None),
):
    request_headers = {
        "Accept": accept,
        "Content-Type": content_type,
        "User-Agent": user_agent,
        "Host": host
    }

    return request_headers

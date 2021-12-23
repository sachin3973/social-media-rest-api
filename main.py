from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = False
    rating: Optional[int] = None


my_posts = [
    {
        "title": "First Post",
        "content": "content of first post",
        "id": 1
    },
    {
        "title": "Second Post",
        "content": "content of second post",
        "id": 2
    }
]


def find_post(id):
    for post in my_posts:
        if post['id'] == id:
            return post


@app.get("/")
def root():
    return {"message": "Hello world!"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts")
def create_post(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}


@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(int(id))
    return{"post_detail": post}

from random import randrange
from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_post = [{"title": "title of the post 1", "content": "content of post 1", "id": 1}, {
    "title": "fav foods", "content": "I like pizza", "id": 2}]

@app.get("/")
async def root():
    return {"message":"Welcome to my API"}

@app.get("/posts")
def get_post():
    return {"data": my_post}

# @app.post("/createposts")
# def create_posts(payload: dict = Body(...)):
#     print(payload)
#     return {"new_post": f"title {payload['title']} content: {payload['content']}"}


@app.post("/posts")
def post_validation(post_val: Post):
    post_dict = post_val.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_post.append()
    # print(post_val)
    # print(post_val.dict())
    return {"data": post_dict}

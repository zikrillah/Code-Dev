from random import randrange
from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

# Create the dictionary for posts
my_posts = [{"title": "title of the post 1", "content": "content of post 1", "id": 1}, {
    "title": "fav foods", "content": "I like pizza", "id": 2}]

# Create function to looking the post_detail
def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p

# Create function to find the index
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i


@app.get("/")
async def root():
    return {"message":"Welcome to my API"}

@app.get("/posts")
def get_post():
    return {"data": my_posts}

# @app.post("/createposts")
# def create_posts(payload: dict = Body(...)):
#     print(payload)
#     return {"new_post": f"title {payload['title']} content: {payload['content']}"}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def post_validation(post_val: Post):
    post_dict = post_val.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    # print(post_val)
    # print(post_val.dict())
    return {"data": post_dict}
 
# @app.get("/posts/latest")
# def get_latest_post():
#     latest_post = my_posts[len(my_posts)-1]
#     return {"detail": latest_post}

@app.get("/posts/{id}")
def get_posts(id: int, response: Response):
    #print(type(id))
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return{"message": f"post with id: {id} was not found"}
    return{"post_detail": post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_posts(id: int):
    # deleting post
    # find the indec in the array that has required ID
    # my_posts.pop(index)
    # print(type(id))
    index = find_index_post(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_posts(id: int, post: Post):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    # print(post)
    return {"massage": post_dict}

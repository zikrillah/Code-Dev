## Get the POST data
- FastAPI using the **Body** *library* to parse the payload on the **POST** request

- FastAPI utilyze the pydantic
    - Pydentic model : print using ```print(post_val)```
    - Convert pydentic modle to dictionary using ```print(post_val.dict())```

Pydentic model
```
title='top beaches in florida' content='check out these awsome beaches in post validation' published=True rating=None
```

Python dictionary model
```
{'title': 'top beaches in florida', 'content': 'check out these awsome beaches in post validation', 'published': True, 'rating': None}
```

## CRUD
#### Create
- POST /posts 
    - ```@app.post("/posts")```
#### Read
- GET /posts/:id
    - ```@app.get("/posts/{id}")```
- GET /posts
    - ```@app.get("/posts")```
#### Update
- PUT/PATCH /posts/:id
    - ```@app.put("/posts/{id}")```
#### Delete
- DELETE
    - ```@app.delete("/posts/{id}")```

## Convert data on fastAPI
- We can directly convert type data on fatAPI using this command ```the def get_posts(id: int):```

## Order is matter
This code
```
@app.get("/posts/{id}")
def get_posts(id: int):
    #print(type(id))
    post = find_post(id)
    return{"post_detail": post}

@app.get("/posts/latest")
def get_latest_post():
    latest_post = my_posts[len(my_posts)-1]
    return {"detail": latest_post}
```
If we request using ```http://127.0.0.1:8000/posts/latest``` trigger an error because the FastAPI first matching rule, so we need to reorder the code to avidong the error.

## Handling the response code
Requirement from fastapi library:
- Response
- status
- HTTPException

We can use:
```
<if statement>
    ...
        response.status_code = status.HTTP_404_NOT_FOUND
        return{"message": f"post with id: {id} was not found"}
    ...
```
but we can simplify using the **HTTPException**
```
<if statement>
    ...
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} was not found")
    ...
```
For every methode you can change the status code by adding the status on the path ex:
```
@app.post("/posts", status_code=status.HTTP_201_CREATED)
```
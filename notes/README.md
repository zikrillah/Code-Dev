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

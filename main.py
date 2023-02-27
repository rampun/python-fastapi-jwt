from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# show all blogs with limit and published status
@app.get('/blogs')
def index(limit=10, published: bool=True, sort: Optional[str] = None): #sort is an optional param
    # only get limit published blogs  # ?limit=10&published=true
    if published:
        return {'data': f'{limit} blog list'}
    else:
        return {'data': 'all blog list'}

# show drafted blogs
@app.get('/blog/draft')
def showDraft():
    return {'data': 'drafted blog list'}

# show blog detail by id
@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}

# show comments for a blog
@app.get('/blog/{id}/comments')
def comments(id, limit=20):
    # fetch comments for the blog id = id
    # return limit
    return {'data': {'1','2'}}




class Blog(BaseModel):
    id: int
    title: str
    body: str
    published: Optional[bool]


# create new blog
@app.post('/blog/create')
def create_blog(request: Blog):
    return request

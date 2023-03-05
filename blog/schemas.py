from typing import List, Union
from pydantic import BaseModel


class BlogBase(BaseModel):
    title: str
    body: str

# extend blobase class


class Blog(BlogBase):

    class Config():
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []

    class Config():
        orm_mode = True


class ShowBlog(BaseModel):
    title: str
    creator: ShowUser

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str  # using username not email because jwt requires the identifier as username
    password: str


# for JWT token
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None

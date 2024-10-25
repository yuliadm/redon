from typing import Optional
from pydantic import BaseModel

class Paper(BaseModel):
    doi: str
    title: str
    authors: list[str]
    publication: str
    summary:str

    def __init__(self, **data):  # Accept keyword arguments
            super().__init__(**data)
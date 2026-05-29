from pydantic import BaseModel
from typing import List


class Entity(BaseModel):
    name: str
    attributes: List[str]


class Page(BaseModel):
    name: str
    route: str
    description: str


class Flow(BaseModel):
    name: str


class Role(BaseModel):
    name: str
    description: str
    permissions: List[str]


class DesignSchema(BaseModel):

    entities: List[Entity]

    pages: List[Page]

    flows: List[dict]

    roles: List[Role]
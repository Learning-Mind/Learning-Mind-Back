from typing import Any, List
from pydantic import BaseModel

class RoadmapNodeSchema(BaseModel):
    node_id: int
    roadmap_id: int
    title: str
    parent_id: int | None = None
    # roadmap: 
    # children
    # parent

class RoadmapSchema(BaseModel):
    roadmap_id: int
    title: str
    nodes: List[Any] = []
    # created_at: datetime
    # updated_at: datetime

class CreateRoadmapSchema(BaseModel):
    title: str

# class RoadmapResponseSchema(ResponseSchema):
class RoadmapResponseSchema(BaseModel):
    roadmap_id: int
    title: str
    nodes: List[Any] = []
    # created_at: datetime
    # updated_at: datetime

class RoadmapNodeSchema(BaseModel):
    node_id: int
    roadmap_id: int
    title: str
    parent_id: int | None = None
    order_in_parent: int
    # roadmap: 
    # children
    # parent

class CreateRoadmapNodeSchema(BaseModel):
    roadmap_id: int
    parent_id: int | None = None
    title: str

# class RoadmapNodeResponseSchema(ResponseSchema):
class RoadmapNodeResponseSchema(BaseModel):
    node_id: int
    roadmap_id: int
    title: str
    parent_id: int | None = None
    order_in_parent: int
    # roadmap: 
    # children
    # parent
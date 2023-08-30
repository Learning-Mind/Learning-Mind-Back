from pydantic import BaseModel

from schema.api import ResponseSchema

class RoadmapSchema(BaseModel):
    roadmap_id: int
    title: str
    # created_at: datetime
    # updated_at: datetime

class CreateRoadmapSchema(BaseModel):
    title: str

class RoadmapResponseSchema(ResponseSchema):
    roadmap_id: int
    title: str
    # created_at: datetime
    # updated_at: datetime

class RoadmapNodeSchema(BaseModel):
    node_id: int
    roadmap_id: int
    title: str
    parent_id: int | None = None
    # roadmap: 
    # children
    # parent

class CreateRoadmapNodeSchema(BaseModel):
    roadmap_id: int
    parent_id: int | None = None
    title: str

class RoadmapNodeResponseSchema(ResponseSchema):
    node_id: int
    roadmap_id: int
    title: str
    parent_id: int | None = None
    # roadmap: 
    # children
    # parent
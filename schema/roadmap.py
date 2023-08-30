from pydantic import BaseModel

from schema.api import ResponseSchema

class RoadmapSchema(BaseModel):
    roadmap_id: int
    title: str

class CreateRoadmapSchema(BaseModel):
    title: str

class RoadmapResponseSchema(ResponseSchema):
    roadmap_id: int
    title: str
    # created_at: datetime
    # updated_at: datetime
    
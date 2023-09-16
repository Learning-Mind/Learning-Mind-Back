from pydantic import BaseModel


class MemoSchema(BaseModel):
    memo_id: int
    contents: str
    # roadmaps
    # roadmap_nodes
    
class CreateMemoSchema(BaseModel):
    contents: str
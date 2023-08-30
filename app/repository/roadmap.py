from sqlalchemy import select
from app.models.roadmap import Roadmap, RoadmapNode
from app.repository.base import BaseDataManager
from schema.roadmap import RoadmapNodeSchema, RoadmapSchema


class RoadmapDataManager(BaseDataManager):
    async def add_roadmap(self, roadmap: Roadmap):
        """Create roadmap to database."""

        model = await self.add_one(roadmap)
        return RoadmapSchema(**model.to_dict())
    
    async def get_root_node(self, roadmap_id: int) -> RoadmapNodeSchema | None:
        """Get root node by roadmap_id."""
        
        stmt = select(RoadmapNode).where(
            RoadmapNode.roadmap_id == roadmap_id, 
            RoadmapNode.parent_id == None
        )
        model = await self.get_one(stmt)
        
        # TODO exception...
        if model is None:
            return None
        else:
            return RoadmapNodeSchema(**model.to_dict())

    async def add_roadmap_node(self, roadmap_node: RoadmapNode):
        """Create Roadmap Node to database."""
        model = await self.add_one(roadmap_node)
        return RoadmapNodeSchema(**model.to_dict())
    
    async def get_roadmap_node_by_id(self, node_id: int):
        """Get Roadmap Node by node_id"""
        stmt = select(RoadmapNode).where(RoadmapNode.node_id == node_id)
        model = await self.get_one(stmt)
        
        return RoadmapNodeSchema(**model.to_dict())
    


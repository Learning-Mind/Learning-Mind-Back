from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.orm.exc import NoResultFound

from app.models.sql import Roadmap, RoadmapNode
from app.repository.base import BaseDataManager
from schema.roadmap import RoadmapNodeSchema, RoadmapSchema



class RoadmapDataManager(BaseDataManager):
    async def add_roadmap(self, roadmap: Roadmap):
        """Create roadmap to database."""

        model = await self.add_one(roadmap)
        return RoadmapSchema(**model.to_dict())
    
    async def get_roadmap_by_id(self, roadmap_id: int):
        """Get Roadmap by roadmap_id."""
        
        stmt = select(Roadmap)\
            .options(selectinload(Roadmap.nodes))\
            .where(Roadmap.roadmap_id == roadmap_id)
            
        model = (await self.session.execute(stmt)).scalars().one()

        return RoadmapSchema(
            roadmap_id=model.roadmap_id,
            title=model.title,
            nodes=[RoadmapNodeSchema(**node.to_dict()) for node in model.nodes]
        )
    
    async def get_roadmap_by_tree(self, roadmap_id: int):
        stmt = select(Roadmap).options(selectinload(Roadmap.nodes, RoadmapNode.children)).where(Roadmap.roadmap_id == roadmap_id)
        model: Roadmap | None = await self.get_one(stmt)

        print(model.nodes)
        
        return None
        
    async def update_roadmap_title(self, roadmap_id: int, title: str):
        model = (await self.session.execute(
            select(Roadmap)
            .filter_by(roadmap_id=roadmap_id)
        )).fetchone()
        
        model.title = title
        return RoadmapSchema(**model.to_dict())
    
    async def get_root_node(self, roadmap_id: int) -> RoadmapNodeSchema | None:
        """Get root node by roadmap_id."""
        
        stmt = select(RoadmapNode).where(
            RoadmapNode.roadmap_id == roadmap_id, 
            RoadmapNode.parent_id == None
        )
        try:
            model = await self.get_one(stmt)
            return RoadmapNodeSchema(**model.to_dict())
        except NoResultFound:
            return None

    async def get_last_node_in_parent(self, roadmap_id: int, parent_id: int | None) -> RoadmapNodeSchema | None:
        """Get last node - max number of order_in_parent."""
        
        stmt = select(RoadmapNode).where(
            RoadmapNode.roadmap_id == roadmap_id,
            RoadmapNode.parent_id == parent_id,
        ).order_by(RoadmapNode.order_in_parent.desc()).limit(1)
        
        try:
            model: RoadmapNode = await self.get_one(stmt)
            return RoadmapNodeSchema(**model.to_dict())
        except NoResultFound:
            return None
        
    async def add_roadmap_node(self, roadmap_node: RoadmapNode):
        """Create Roadmap Node to database."""
        model = await self.add_one(roadmap_node)
        return RoadmapNodeSchema(**model.to_dict())
    
    async def get_roadmap_node_by_id(self, node_id: int):
        """Get Roadmap Node by node_id"""
        stmt = select(RoadmapNode).where(RoadmapNode.node_id == node_id)
        model = await self.get_one(stmt)
        
        return RoadmapNodeSchema(**model.to_dict())
    


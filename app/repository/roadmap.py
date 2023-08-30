from sqlalchemy import select
from app.models.roadmap import Roadmap
from app.repository.base import BaseDataManager
from schema.roadmap import RoadmapSchema


class RoadmapDataManager(BaseDataManager):
    async def add_roadmap(self, roadmap: Roadmap):
        """Create roadmap to database."""

        model = await self.add_one(roadmap)
        return RoadmapSchema(**model.to_dict())
    

from app.models.roadmap import Roadmap
from app.repository.roadmap import RoadmapDataManager
from app.service.base import BaseService
from schema.roadmap import CreateRoadmapSchema


class RoadmapService(BaseService):
    async def create_roadmap(self, roadmap: CreateRoadmapSchema):
        roadmap_model = Roadmap(
            title=roadmap.title
        )
        return await RoadmapDataManager(self.session).add_roadmap(roadmap_model)
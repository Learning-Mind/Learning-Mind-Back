from app.models.roadmap import Roadmap, RoadmapNode
from app.repository.roadmap import RoadmapDataManager
from app.service.base import BaseService
from schema.roadmap import CreateRoadmapNodeSchema, CreateRoadmapSchema


class RoadmapService(BaseService):
    async def create_roadmap(self, roadmap: CreateRoadmapSchema):
        """Create Roadmap."""
        roadmap_model = Roadmap(
            title=roadmap.title
        )
        return await RoadmapDataManager(self.session).add_roadmap(roadmap_model)

    async def create_roadmap_node(self, roadmap_node: CreateRoadmapNodeSchema):
        """로드맵 노드를 생성한다."""
        # TODO root node가 이미 있는지 확인
        if roadmap_node.parent_id is None:
            root_node = await RoadmapDataManager(self.session).get_root_node(roadmap_id=roadmap_node.parent_id)
            
            if root_node:
                # TODO root node가 있으면 excetion
                pass

        # TODO parent id 가 같은 roadmap에 있는지 확인
        
        roadmap_node_model = RoadmapNode(
            title=roadmap_node.title,
            roadmap_id=roadmap_node.roadmap_id,
            parent_id=roadmap_node.parent_id,
        )
        
        return await RoadmapDataManager(self.session).add_roadmap_node(roadmap_node_model)
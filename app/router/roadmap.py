from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends
from app.db.session import get_async_session
from app.service.roadmap import RoadmapService

from schema.roadmap import CreateRoadmapNodeSchema, CreateRoadmapSchema, RoadmapNodeResponseSchema, RoadmapResponseSchema


router = APIRouter()

# 특정 로드맵 조회 API
@router.get(
    path="/{roadmap_id}",
    summary="id로 로드맵 조회",
    description="roadmap_id로 로드맵을 조회합니다.",
    response_model=RoadmapResponseSchema,
)
async def get_roadmap_item(
    roadmap_id: int,
    se: AsyncSession = Depends(get_async_session)
):
    result = await RoadmapService(se).get_roadmap_item_by_id(roadmap_id=roadmap_id)

    return RoadmapResponseSchema(
        code=0,
        message="",
        roadmap_id=result.roadmap_id,
        title=result.title,
        nodes=result.nodes
    )


# 로드맵 생성 API
@router.post(
    path="/write",
    summary="로드맵 생성",
    description="로드맵을 생성합니다.",
    response_model=RoadmapResponseSchema,
)
async def write_roadmap(
    body: CreateRoadmapSchema,
    se: AsyncSession = Depends(get_async_session)
) -> RoadmapResponseSchema:
    result = await RoadmapService(se).create_roadmap(body)
    return RoadmapResponseSchema(
        code=0,
        message="",
        roadmap_id=result.roadmap_id,
        title=result.title
    )

# 로드맵 노드 생성 API
@router.post(
    path="/node/write",
    response_model=RoadmapNodeResponseSchema
)
async def write_roadmap_node(
    body: CreateRoadmapNodeSchema,
    se: AsyncSession = Depends(get_async_session)
):
    result = await RoadmapService(se).create_roadmap_node(roadmap_node=body)
    return RoadmapNodeResponseSchema(
        code=200,
        message="",
        node_id=result.node_id,
        roadmap_id=result.roadmap_id,
        title=result.title,
        parent_id=result.parent_id,
        order_in_parent=result.order_in_parent,
    )

# TODO 로드맵 노드 이름 수정 API

# TODO 로드맵 parent 수정 API
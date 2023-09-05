from typing import List

from sqlalchemy import Column, ForeignKey, Table
from app.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship



memo_roadmap_asso_table = Table(
    "memo_roadmap_asso_table",
    Base.metadata,
    Column("roadmap_id", ForeignKey("roadmap.roadmap_id"), primary_key=True),
    Column("memo_id", ForeignKey("memo.memo_id"), primary_key=True),
)

memo_roadmapnode_asso_table = Table(
    "memo_roadmapnode_asso_table",
    Base.metadata,
    Column("node_id", ForeignKey("roadmap_node.node_id"), primary_key=True),
    Column("memo_id", ForeignKey("memo.memo_id"), primary_key=True),
)


class RoadmapModel(Base):
    __tablename__ = "roadmap"
    
    roadmap_id: Mapped[int] = mapped_column("roadmap_id", primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column("title")
    nodes: Mapped[List["RoadmapNodeModel"]] = relationship(back_populates="roadmap")
    memos: Mapped["MemoModel"] = relationship(
        secondary=memo_roadmap_asso_table,
        back_populates="roadmaps"
    )
    
    
class RoadmapNodeModel(Base):
    __tablename__ = "roadmap_node"
    
    node_id: Mapped[int] = mapped_column("node_id", primary_key=True, autoincrement=True)
    roadmap_id: Mapped[int] = mapped_column(ForeignKey("roadmap.roadmap_id"))
    roadmap: Mapped["RoadmapModel"] = relationship(back_populates="nodes")
    title: Mapped[str] = mapped_column("title")
    parent_id: Mapped[int] = mapped_column(ForeignKey("roadmap_node.node_id"), nullable=True)
    children: Mapped[List["RoadmapNodeModel"]] = relationship("RoadmapNodeModel", back_populates="parent")
    parent: Mapped["RoadmapNodeModel"] = relationship("RoadmapNodeModel", back_populates="children", remote_side=[node_id])
    order_in_parent: Mapped[int] = mapped_column("order_in_parent", default=0)
    memos: Mapped["MemoModel"] = relationship(
        secondary=memo_roadmapnode_asso_table,
        back_populates="roadmap_nodes"
    )


class MemoModel(Base):
    __tablename__ = "memo"
    
    memo_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    contents: Mapped[str] = mapped_column("contents")
    roadmaps: Mapped[List["RoadmapModel"]] = relationship(
        secondary=memo_roadmap_asso_table,
        back_populates="memos"
    )
    roadmap_nodes: Mapped[List["RoadmapNodeModel"]] = relationship(
        secondary=memo_roadmapnode_asso_table,
        back_populates="memos"
    )
    # TODO tags

    
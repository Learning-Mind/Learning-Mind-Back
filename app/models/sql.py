from datetime import datetime
from typing import List
import uuid

from sqlalchemy import Column, ForeignKey, Table, Uuid, func
from app.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


# ----------------------------- M:N relationship ----------------------------- #
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

# ----------------------------------- User ----------------------------------- #
class User(Base):
    __tablename__ = "user"
    user_id: Mapped[int] = mapped_column("user_id", primary_key=True, autoincrement=True)
    nickname: Mapped[str] = mapped_column("nickname", unique=True)
    email: Mapped[str] = mapped_column("email", unique=True)
    hashed_password: Mapped[str] = mapped_column("hashed_password")
    name: Mapped[str] = mapped_column("name")


# ---------------------------------- Roadmap --------------------------------- #
class Roadmap(Base):
    __tablename__ = "roadmap"
    roadmap_id: Mapped[int] = mapped_column("roadmap_id", primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column("title")
    nodes: Mapped[List["RoadmapNode"]] = relationship(back_populates="roadmap")
    memos: Mapped["Memo"] = relationship(
        secondary=memo_roadmap_asso_table,
        back_populates="roadmaps"
    )
    
    
class RoadmapNode(Base):
    __tablename__ = "roadmap_node"
    node_id: Mapped[int] = mapped_column("node_id", primary_key=True, autoincrement=True)
    roadmap_id: Mapped[int] = mapped_column(ForeignKey("roadmap.roadmap_id"))
    roadmap: Mapped["Roadmap"] = relationship(back_populates="nodes")
    title: Mapped[str] = mapped_column("title")
    parent_id: Mapped[int] = mapped_column(ForeignKey("roadmap_node.node_id"), nullable=True)
    children: Mapped[List["RoadmapNode"]] = relationship("RoadmapNode", back_populates="parent")
    parent: Mapped["RoadmapNode"] = relationship("RoadmapNode", back_populates="children", remote_side=[node_id])
    order_in_parent: Mapped[int] = mapped_column("order_in_parent", default=0)
    memos: Mapped["Memo"] = relationship(
        secondary=memo_roadmapnode_asso_table,
        back_populates="roadmap_nodes"
    )


# ----------------------------------- Memo ----------------------------------- #
class Memo(Base):
    __tablename__ = "memo"
    memo_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    contents: Mapped[str] = mapped_column("contents")
    roadmaps: Mapped[List["Roadmap"]] = relationship(
        secondary=memo_roadmap_asso_table,
        back_populates="memos"
    )
    roadmap_nodes: Mapped[List["RoadmapNode"]] = relationship(
        secondary=memo_roadmapnode_asso_table,
        back_populates="memos"
    )
    # TODO tags

    
from typing import List

from sqlalchemy import ForeignKey
from app.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Roadmap(Base):
    __tablename__ = "roadmap"
    
    roadmap_id: Mapped[int] = mapped_column("roadmap_id", primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column("title")
    nodes: Mapped[List["RoadmapNode"]] = relationship(back_populates="roadmap")
    
    
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

    
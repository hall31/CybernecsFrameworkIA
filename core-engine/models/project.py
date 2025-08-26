from sqlalchemy import Column, String, DateTime, JSON, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
from core.database import Base

class Project(Base):
    __tablename__ = "projects"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    idea = Column(Text, nullable=False)
    roadmap = Column(JSON, nullable=True)
    stack = Column(JSON, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    path = Column(String, nullable=True)  # chemin du code généré
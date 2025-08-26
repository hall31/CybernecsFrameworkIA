from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.project import Project
from models.log import Log
from api.schemas import ProjectCreate, LogCreate
from typing import List, Optional
from uuid import UUID

class ProjectCRUD:
    @staticmethod
    async def create(db: AsyncSession, project: ProjectCreate) -> Project:
        db_project = Project(**project.dict())
        db.add(db_project)
        await db.commit()
        await db.refresh(db_project)
        return db_project
    
    @staticmethod
    async def get_all(db: AsyncSession) -> List[Project]:
        result = await db.execute(select(Project).order_by(Project.created_at.desc()))
        return result.scalars().all()
    
    @staticmethod
    async def get_by_id(db: AsyncSession, project_id: UUID) -> Optional[Project]:
        result = await db.execute(select(Project).where(Project.id == project_id))
        return result.scalar_one_or_none()
    
    @staticmethod
    async def update(db: AsyncSession, project_id: UUID, **kwargs) -> Optional[Project]:
        project = await ProjectCRUD.get_by_id(db, project_id)
        if project:
            for key, value in kwargs.items():
                setattr(project, key, value)
            await db.commit()
            await db.refresh(project)
        return project

class LogCRUD:
    @staticmethod
    async def create(db: AsyncSession, log: LogCreate) -> Log:
        db_log = Log(**log.dict())
        db.add(db_log)
        await db.commit()
        await db.refresh(db_log)
        return db_log
    
    @staticmethod
    async def get_by_project(db: AsyncSession, project_id: UUID) -> List[Log]:
        result = await db.execute(
            select(Log).where(Log.project_id == project_id).order_by(Log.timestamp.desc())
        )
        return result.scalars().all()
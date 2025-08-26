import logging
import asyncio
from datetime import datetime
from uuid import UUID
from typing import Optional
from core.database import AsyncSessionLocal
from api.crud import LogCRUD
from api.schemas import LogCreate

class DatabaseLogger:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        console_handler.setFormatter(formatter)
        
        self.logger.addHandler(console_handler)
    
    async def log_to_db(self, project_id: UUID, message: str, level: str = "INFO"):
        try:
            async with AsyncSessionLocal() as db:
                log_data = LogCreate(
                    project_id=project_id,
                    message=f"[{level}] {message}"
                )
                await LogCRUD.create(db, log_data)
        except Exception as e:
            # Fallback to console if DB fails
            self.logger.error(f"Failed to log to DB: {e}")
    
    def info(self, message: str, project_id: Optional[UUID] = None):
        self.logger.info(message)
        if project_id:
            asyncio.create_task(self.log_to_db(project_id, message, "INFO"))
    
    def warning(self, message: str, project_id: Optional[UUID] = None):
        self.logger.warning(message)
        if project_id:
            asyncio.create_task(self.log_to_db(project_id, message, "WARNING"))
    
    def error(self, message: str, project_id: Optional[UUID] = None):
        self.logger.error(message)
        if project_id:
            asyncio.create_task(self.log_to_db(project_id, message, "ERROR"))
    
    def debug(self, message: str, project_id: Optional[UUID] = None):
        self.logger.debug(message)
        if project_id:
            asyncio.create_task(self.log_to_db(project_id, message, "DEBUG"))

# Global logger instance
db_logger = DatabaseLogger()
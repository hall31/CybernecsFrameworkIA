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
import datetime
from typing import Optional

def log_event(agent: str, message: str, level: str = "INFO") -> None:
    """
    Log an event with timestamp, agent name, and message
    
    Args:
        agent (str): Name of the agent or component
        message (str): Log message
        level (str): Log level (INFO, WARNING, ERROR, DEBUG)
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Color codes for different log levels
    colors = {
        "INFO": "\033[94m",      # Blue
        "WARNING": "\033[93m",   # Yellow
        "ERROR": "\033[91m",     # Red
        "DEBUG": "\033[90m",     # Gray
        "SUCCESS": "\033[92m"    # Green
    }
    
    # Reset color code
    reset_color = "\033[0m"
    
    # Get color for the log level
    color = colors.get(level, colors["INFO"])
    
    # Format the log message
    formatted_message = f"{color}[{timestamp}] {level:8} | {agent:15} | {message}{reset_color}"
    
    # Print to console
    print(formatted_message)

def log_success(agent: str, message: str) -> None:
    """Log a success message"""
    log_event(agent, message, "SUCCESS")

def log_warning(agent: str, message: str) -> None:
    """Log a warning message"""
    log_event(agent, message, "WARNING")

def log_error(agent: str, message: str) -> None:
    """Log an error message"""
    log_event(agent, message, "ERROR")

def log_debug(agent: str, message: str) -> None:
    """Log a debug message"""
    log_event(agent, message, "DEBUG")

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
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
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
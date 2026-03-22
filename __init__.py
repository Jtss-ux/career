# Required by Google ADK to recognise this directory as a Python module.
# ADK imports root_agent from here automatically when you run:
#   adk web career_agent
#   adk deploy cloud_run --service_name=career-agent career_agent
from .agent import root_agent

__all__ = ["root_agent"]

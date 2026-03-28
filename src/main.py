"""Main entry point for the agent."""

import asyncio
import logging
import os
from dotenv import load_dotenv
from src.agent import MyAgent, AgentConfig

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()


async def main():
    """Main function."""
    # Create agent configuration
    config = AgentConfig(
        name=os.getenv("AGENT_NAME", "databricks-agent"),
        model=os.getenv("AGENT_MODEL", "gpt-4"),
        debug=os.getenv("DEBUG", "false").lower() == "true",
    )
    
    # Initialize agent
    agent = MyAgent(config=config)
    logger.info(f"Agent initialized: {config.name}")
    
    try:
        # Example: Run the agent with a prompt
        response = await agent.run("What is 42 plus 8?")
        print(f"Agent response: {response}")
        
    except Exception as e:
        logger.error(f"Error: {e}")
    finally:
        agent.shutdown()


if __name__ == "__main__":
    asyncio.run(main())

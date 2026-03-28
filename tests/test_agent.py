"""Tests for the agent module."""

import pytest
from src.agent import MyAgent, AgentConfig


def test_agent_initialization():
    """Test agent initialization."""
    config = AgentConfig(name="test-agent")
    agent = MyAgent(config=config)
    
    assert agent.config.name == "test-agent"
    assert agent.agent is not None


@pytest.mark.asyncio
async def test_agent_run():
    """Test running the agent."""
    agent = MyAgent()
    
    # This is a placeholder test
    # In a real scenario, you'd mock the agent's run method
    assert agent.agent is not None

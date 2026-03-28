# Databricks AgentBricks Agent

A general-purpose agent built with Databricks AgentBricks framework.

## Project Structure

```
.
├── src/                    # Agent source code
│   ├── __init__.py
│   ├── agent.py           # Main agent implementation
│   └── main.py            # Entry point
├── tests/                 # Test suite
│   ├── __init__.py
│   └── test_agent.py
├── requirements.txt       # Python dependencies
├── pyproject.toml         # Project configuration
├── .env.example          # Environment variables template
└── README.md             # This file
```

## Setup

1. **Clone the repository and install dependencies:**

   ```bash
   cd /workspaces/agentic-tbd
   pip install -r requirements.txt
   ```

2. **Configure Databricks credentials:**

   ```bash
   cp .env.example .env
   # Edit .env with your Databricks credentials
   ```

3. **Run the agent:**

   ```bash
   python -m src.main
   ```

## Features

- **General-purpose agent** built with Databricks AgentBricks
- **Tool registration system** for extending agent capabilities
- **Async support** for non-blocking execution
- **Configuration management** with Pydantic
- **Logging** for debugging and monitoring

## Development

### Running Tests

```bash
pip install -e ".[dev]"
pytest tests/
```

### Code Quality

```bash
black src/ tests/
ruff check src/ tests/
```

## Customization

### Adding New Tools

Edit [src/agent.py](src/agent.py) and add new tools in the `_register_tools()` method:

```python
@agent.tool(name="my_tool", description="Tool description")
def my_tool(param1: str, param2: int) -> str:
    """Tool implementation."""
    return result
```

### Modifying Agent Behavior

Configure the agent in [src/agent.py](src/agent.py) by modifying the `AgentConfig` class or updating environment variables in `.env`.

## Dependencies

- **databricks-agentbricks** - AgentBricks framework
- **databricks-sdk** - Databricks API SDK
- **pydantic** - Data validation
- **langchain** - LLM integration utilities
- **python-dotenv** - Environment configuration

## License

MIT

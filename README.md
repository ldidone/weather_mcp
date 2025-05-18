# Argentinian Weather MCP

MCP Server to provide argentinian weather as a tools.
This project was based on the [MCP Server Quickstart documentation](https://modelcontextprotocol.io/quickstart/server).

### The server exposes 2 tools:
- `get_forecast`: allows to get weather forecast for a argentinian location based on SMN.
- `get_weather`: allows to get weather information for a specific argentinian city based on SMN.

### Configure Claude Desktop as a host:

To use this MCP Server with Claude Desktop you need to add the following configuration into the file `claude_desktop_config.json`:
```
{
    "mcpServers": {
        "weather": {
            "command": "uv",
            "args": [
                "--directory",
                "/ABSOLUTE/PATH/TO/PARENT/FOLDER/weather,
                "run",
                "weather.py"
            ]
        }
    }
}

```
### Example of use:
In the following image you can see an example of use the MCP with Claude Desktop asking for the forecast in spanish:

![Captura de pantalla 2025-05-18 a la(s) 20 38 41](https://github.com/user-attachments/assets/aa0fbdaf-54ae-495e-accc-6895847eb0fb)

### Contact me:
- LinkedIn: [Lucas Didone](https://www.linkedin.com/in/lucas-didon%C3%A9/)
- X: [Lucas Didone](https://x.com/LDidone)



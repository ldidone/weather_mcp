from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("weather")

# Constants
SMN_API_BASE = "https://ws.smn.gob.ar/"
USER_AGENT = "weather-app/1.0"


async def make_smn_request(url: str) -> dict[str, Any] | None:
    """Make a request to the SMN API with proper error handling."""
    headers = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None


@mcp.tool()
async def get_forecast(city_name: str) -> str:
    """Get weather forecast for a argentinian location.
    Args:
        city_name(str): Name of the city
    Returns:
        str: Forecast information for the specified city
    """
    url = f"{SMN_API_BASE}/map_items/forecast"
    n_days = 5  # Number of days to forecast (Range: 1-5)
    forecasts = []
    for i in range(1, n_days):
        new_url = f"{url}/{i}"
        data = await make_smn_request(new_url)
        if not data:
            error_message = "Unable to fetch weather data."
            return error_message
        else:
            found_city = False
            for data_item in data:
                if data_item["name"].lower() == city_name.lower():
                    found_city = True
                    forecast = f"""
City: {data_item["name"]}
Day: {data_item["weather"]['day']}
Morning temp: {data_item["weather"]['morning_temp']}°C
Morning description: {data_item["weather"]['morning_desc']}
Afternoon temp: {data_item["weather"]['afternoon_temp']}°C
Afternoon description: {data_item["weather"]['afternoon_desc']}
                    """
                    forecasts.append(forecast)
            if not found_city:
                error_message = f"""City '{city_name}' not found in the response."""
                return error_message

    return "\n---\n".join(forecasts)


@mcp.tool()
async def get_weather(city_name: str) -> str:
    """Get weather information for a specific argentinian city.
    Args:
        city_name(str): Name of the city
    Returns:
        str: Weather information for the specified city
    """

    url = f"""{SMN_API_BASE}/map_items/weather"""

    data = await make_smn_request(url)
    if not data:
        error_message = "Unable to fetch weather data."
        return error_message
    else:
        found_city = False
        for data_item in data:
            if data_item["name"].lower() == city_name.lower():
                found_city = True
                weather = f"""
City: {data_item["name"]}
Temperature: {data_item["weather"]["temp"]}°C
Humidity: {data_item["weather"]["humidity"]}%
Description: {data_item["weather"]["description"]}
                """
                return weather
        if not found_city:
            error_message = f"""City '{city_name}' not found in the response."""
            return error_message


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport="stdio")

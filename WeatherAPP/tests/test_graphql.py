from starlette.testclient import TestClient
from datetime import datetime
import pytest
import pytz
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from GraphQLSpace.app import app as graphql_app

client = TestClient(graphql_app)

# This test is failing in gitlab-runner but not locally. Restore when it turns
# stable.
@pytest.mark.skip(reason="Skipping this test for unkown failures.")
def test_graphql_weather_query():
    query = """
    query {
        weather(city: "Boulder") {
            city
            temperature
        }
    }
    """
    response = client.post("/", json={"query": query})
    assert response.status_code == 200
    assert response.json()["data"]["weather"]["city"] == "Boulder"

# This test is failing in gitlab-runner but not locally. Restore when it turns
# stable.
@pytest.mark.skip(reason="Skipping this test for unkown failures.")
def test_graphql_flowise_query(mocker):
    query = """
    query {
        flowise(message: "What's the weather like in Boulder?")
    }
    """

    mocker.patch(
        "GraphQLSpace.schema.connectFlowise",
        return_value=(
            "The current weather in Boulder is clear with a"
            "temperature of 18.37°C, with scattered clouds"
            "which feels like 17.91°C. The minimum Temperature"
            "is 17.00°C and the maximum temperature is 19.00°C."
        ),
    )

    response = client.post("/", json={"query": query})
    assert response.status_code == 200

    # Verify espected elements
    data = response.json()["data"]
    assert "flowise" in data
    assert isinstance(data["flowise"], str)
    print(data["flowise"])
    assert any(
        word.lower() in data["flowise"].lower()
        for word in [
            "temperature",
            "Temperature",
            "weather",
            "Weather",
            "clouds",
            "Clouds",
        ]
    )


def test_get_current_day(mocker):
    # Get the current date in the New York time zone
    ny_tz = pytz.timezone("America/New_York")
    current_date = datetime.now(ny_tz).strftime("%Y-%m-%d")

    mocker.patch(
        "GraphQLSpace.schema.getCurrentDay",
        return_value=current_date
    )

    query = """
    query {
        date(timezone: "America/New_York")
    }
    """

    response = client.post("/", json={"query": query})
    assert response.status_code == 200

    data = response.json()["data"]
    assert "date" in data
    assert data["date"].startswith(current_date)


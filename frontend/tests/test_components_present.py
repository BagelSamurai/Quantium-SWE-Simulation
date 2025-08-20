import pytest
from dash.testing.application_runners import import_app
from selenium.webdriver.common.by import By
# --- ADD THESE THREE LINES ---
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# This line should already be correct
app = import_app("app")

def test_header_exists(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element("h1")
    assert header.text == "Pink Morsel Sales"
    dash_duo.wait_for_text_to_equal("h1", "Pink Morsel Sales")

def test_visualisation_is_present(dash_duo):
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#main-graph")
    assert graph is not None

def test_region_picker_is_present(dash_duo):
    dash_duo.start_server(app)
    region_picker = dash_duo.find_element("#region-control")
    assert region_picker is not None

@pytest.fixture(scope="session", autouse=True)
def setup_selenium():
    """Initializes the webdriver and makes it available for dash_duo."""
    webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
import os
import pytest
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session", autouse=True)
def setup_driver():

    driver_path = ChromeDriverManager().install()

    driver_dir = os.path.dirname(driver_path)

    os.environ["PATH"] += os.pathsep + driver_dir
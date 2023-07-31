import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def test(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://hr.smiligence.in/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()


import pytest
import allure
import os
from selenium import webdriver

@pytest.fixture(params=["chrome", "firefox"]) 
def driver(request):
    browser_name = request.param
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        d = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("-headless")
        d = webdriver.Firefox(options=options)
    
    yield d
    d.quit()

# Скриншот при падении
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        try:
            if not os.path.exists('screenshots'):
                os.makedirs('screenshots')
            driver = item.funcargs['driver']
            file_name = f"screenshots/{item.name}.png"
            driver.save_screenshot(file_name)
            allure.attach(driver.get_screenshot_as_png(), 
                          name="Failure_Screenshot", 
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(f"Ошибка скриншота: {e}")
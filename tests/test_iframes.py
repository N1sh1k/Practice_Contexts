import allure
from pages.context_page import ContextPage

@allure.feature("Работа с контекстами")
@allure.story("Nested iFrames")
def test_nested_iframes_navigation(driver):
    page = ContextPage(driver)
    
    with allure.step("Открыть страницу с вложенными фреймами"):
        page.open("https://the-internet.herokuapp.com/nested_frames")
    
    with allure.step("Навигация по вложенным фреймам"):
        page.wait_and_switch_to_frame("frame-top")
        page.wait_and_switch_to_frame("frame-left")
        assert "LEFT" in driver.page_source
        
        # Переход в соседний фрейм
        page.driver.switch_to.parent_frame()
        page.wait_and_switch_to_frame("frame-middle")
        assert "MIDDLE" in driver.page_source
    
    with allure.step("Выход и проверка нижнего фрейма"):
        page.switch_to_default()
        page.wait_and_switch_to_frame("frame-bottom")
        assert "BOTTOM" in driver.page_source
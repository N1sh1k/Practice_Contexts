import allure
import pytest
from selenium.webdriver.support import expected_conditions as EC
from pages.context_page import ContextPage

@allure.feature("Работа с контекстами")
@allure.story("Вкладки и окна")
def test_new_tab_opening(driver):
    page = ContextPage(driver)
    
    with allure.step("Открыть страницу"):
        page.open("https://the-internet.herokuapp.com/windows")
        initial_count = len(driver.window_handles)
    
    with allure.step("Открыть новую вкладку"):
        page.click(page.CLICK_HERE)
        page.wait_for_new_window(initial_count)
    
    with allure.step("Переключиться на новую вкладку и дождаться загрузки контента"):
        page.switch_to_window_by_index(-1)
        
        page.wait.until(EC.visibility_of_element_located(page.NEW_WINDOW_TEXT))
        
        actual_text = page.driver.find_element(*page.NEW_WINDOW_TEXT).text
        assert "New Window" == actual_text
    
    with allure.step("Вернуться в основное окно"):
        page.close_current_and_back()
        assert "The Internet" in driver.title
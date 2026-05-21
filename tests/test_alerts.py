import allure
from pages.context_page import ContextPage

@allure.feature("Работа с контекстами")
@allure.story("JavaScript Alerts")
def test_javascript_alert(driver):
    page = ContextPage(driver)
    
    with allure.step("Открыть страницу алертов"):
        page.open("https://the-internet.herokuapp.com/javascript_alerts")
    
    with allure.step("Вызвать и обработать Alert"):
        page.click(page.ALERT_BUTTON)
        alert_text = page.handle_alert("accept")
        assert "I am a JS Alert" in alert_text
    
    with allure.step("Проверить текст подтверждения на странице"):
        result = page.find_element(page.RESULT_TEXT).text
        assert "successfully" in result
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.logger = logging.getLogger(__name__)

    def open(self, url):
        self.logger.info(f"Открытие: {url}")
        self.driver.get(url)

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.logger.info(f"Клик по: {locator}")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    # --- МЕТОДЫ ДЛЯ ТЕСТОВ ---

    def wait_and_switch_to_frame(self, frame_reference):
        """Ожидание и переключение во фрейм"""
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(frame_reference))
        self.logger.info(f"Переключились во фрейм: {frame_reference}")

    def switch_to_default(self):
        """Возврат в основной контекст"""
        self.driver.switch_to.default_content()
        self.logger.info("Вернулись в основной контекст")

    def wait_for_new_window(self, current_count):
        """Явное ожидание открытия новой вкладки"""
        self.wait.until(lambda d: len(d.window_handles) > current_count)
        self.logger.info("Новое окно обнаружено")

    def switch_to_window_by_index(self, index):
        """Переключение на окно по индексу"""
        self.driver.switch_to.window(self.driver.window_handles[index])
        self.logger.info(f"Переключились на окно индекс {index}")

    def close_current_and_back(self):
        """Закрыть текущую вкладку и вернуться на первую"""
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.logger.info("Вкладка закрыта, вернулись назад")

    def handle_alert(self, action="accept"):
        """Умная работа с алертами"""
        alert = self.wait.until(EC.alert_is_present())
        text = alert.text
        if action == "accept":
            alert.accept()
        else:
            alert.dismiss()
        self.logger.info(f"Alert обработан ({action})")
        return text
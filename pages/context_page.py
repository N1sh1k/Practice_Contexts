from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ContextPage(BasePage):
    # Локаторы (адреса кнопок и полей)
    # Для фреймов
    FRAME_TOP = (By.NAME, "frame-top")
    FRAME_LEFT = (By.NAME, "frame-left")
    FRAME_MIDDLE = (By.NAME, "frame-middle")
    BODY = (By.TAG_NAME, "body")

    # Для новых окон
    WINDOWS_LINK = (By.LINK_TEXT, "Multiple Windows")
    CLICK_HERE = (By.LINK_TEXT, "Click Here")
    NEW_WINDOW_TEXT = (By.TAG_NAME, "h3") # Текст в новом окне

    # Для всплывающих окон
    ALERTS_LINK = (By.LINK_TEXT, "JavaScript Alerts")
    ALERT_BUTTON = (By.XPATH, "//button[text()='Click for JS Alert']")
    RESULT_TEXT = (By.ID, "result")
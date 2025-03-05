from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def find_and_click(self, locator, index=0):
        elements = self.find_elements(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", elements[index])
        elements[index].click()

    def get_element_text(self, locator, timeout=5):
        return self.wait_until_visible(locator, timeout).text


    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def input_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def wait_until_visible(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def click_and_wait(self, locator, next_locator):
        self.click_element(locator)
        self.wait_until_visible(next_locator)

    def scroll_and_click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        element.click()

    def click_and_check_url_change(self, locator, expected_url):
        element = self.wait_until_visible(locator)
        element.click()
        WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_url))

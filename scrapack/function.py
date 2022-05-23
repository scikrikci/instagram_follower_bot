from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class Selectors():
    def wait_for_element(self, time: int, selector: tuple):
        WebDriverWait(self.driver, time).until(
            expected_conditions.visibility_of_element_located(selector))
            
    def move_to_element_and_click(self, elem):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", elem)
        sleep(2)
        self.driver.execute_script("arguments[0].click();", elem)

    def move_mouse_to_element(self, element):
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def move_to_element(self, elem):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", elem)
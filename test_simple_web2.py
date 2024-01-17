import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


@pytest.mark.usefixtures("setup")
class TestExampleTwo:
    def test_search_google(self):
        self.driver.get("https://www.google.com")
        sleep(1)
        search = self.driver.find_element(By.CLASS_NAME, "gLFyf")
        search.send_keys('Github' + Keys.RETURN)
        sleep(1)
        print("\nDriver Title: " + self.driver.title)
        sleep(2)
    
    def test_title_github(self):
        self.driver.get('https://github.com')
        sleep(1)
        print("\nDriver Title: " + self.driver.title)
        sleep(2)
        

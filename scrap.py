from time import sleep
from selenium.webdriver.common.by import By
import json,sys

from scrapack import ScrapBase

class InstagramBot(ScrapBase):
    def __init__(self):
        super().__init__()
        self.followers_dict = []
        self.following_dict = []

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')

        self.wait_for_element(20, (By.XPATH, "//input[@name='username']"))
        print("wait main page")

        self.driver.find_element(
            By.XPATH, "//input[@name='username']").send_keys(f"{self.username}")
        print("username entered")
        self.driver.find_element(
            By.XPATH, "//input[@name='password']").send_keys(f"{self.password}")
        print("passwoord entered")
        self.driver.find_element(
            By.XPATH, "//button[starts-with(@class,'sqdOP  ')]").click()
        print("login clicked")

        self.wait_for_element(
            20, (By.XPATH, "//div[@class='cq2ai']/img[@alt='Instagram']"))
        print("wait main page")

        sleep(3)
        self.driver.get(f"https://www.instagram.com/{self.username}/")

        user_page_name = By.XPATH, "//div[@class='XBGH5']/h2"
        self.wait_for_element(20, (user_page_name))
        print("user page wait and entered")

        user_title = self.driver.find_element(
            By.XPATH, "//div[@class='XBGH5']/h2").text
        print("user title :", user_title)

        self.followers()
        print("finish followers")
        sleep(2)

        elem = self.driver.find_element(
            By.XPATH, "//div[starts-with(@class,'RnEpo  Yx5HN')]/descendant::button[@class='wpO6b  ']")
        self.move_to_element_and_click(elem)

        print("closed followers window")

        self.following()

        print(f"JSON: {json.dumps(self.following_dict, indent = 4)}")

        print("FINISH")

        self.quit()
        
            
    def fow(self, n):
        self.wait_for_element(
            20, (By.XPATH, f"//ul[@class='_6xe7A']/div/li[{n}]/descendant::span[@class='Jv7Aj mArmR MqpiF  ']/a/span"))

        self.move_to_element(self.driver.find_element(By.XPATH, f"//ul[@class='_6xe7A']/div/li[{n}]"))

        self.flw_name = self.driver.find_element(
            By.XPATH, f"//ul[@class='_6xe7A']/div/li[{n}]/descendant::span[@class='Jv7Aj mArmR MqpiF  ']/a/span").text
    
    def followers(self):
        followers = self.driver.find_element(
            By.XPATH, "//*[@id='react-root']/descendant::section/main/div/header/section/ul/li[2]/a/div/span").text
        followers = int(followers)
        print(followers)
        self.driver.find_element(
            By.XPATH, "//*[@id='react-root']/descendant::section/main/div/header/section/ul/li[2]/a").click()
        print("followers clicked")
        for i in range(1, followers):
            self.fow(i)
            self.followers_dict.append(self.flw_name)

    def following(self):
        following = self.driver.find_element(
            By.XPATH, "//*[@id='react-root']/descendant::section/main/div/header/section/ul/li[3]/a/div/span").text
        following = int(following)
        print(following)
        self.driver.find_element(
            By.XPATH, "//*[@id='react-root']/descendant::section/main/div/header/section/ul/li[3]/a").click()
        print("following clicked")
        self.wait_for_element(
            20, (By.XPATH, "//ul[@class='_6xe7A']/div/li/descendant::a[@class='notranslate _0imsa ']/span"))
        print("following page wait")

        for j in range(1, following):
            self.fow(j)
            if self.flw_name not in self.followers_dict:
                self.following_dict.append(self.flw_name)

if __name__ == "__main__":
    scraper = InstagramBot()
    scraper.login()
    

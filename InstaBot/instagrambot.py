from instaUserInfo import username, password, username1
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.common import exceptions


class Instagram:
    def __init__(self, username, username1, password):
        self.browser = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
        self.username = username
        self.username1 = username1
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com")
        time.sleep(3)
        usernameInput = self.browser.find_element_by_xpath(
            "//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath(
            "//*[@id='loginForm']/div/div[2]/div/label/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(3)

    def getFollowers(self):
        try:
            self.browser.get(f"https://www.instagram.com/{self.username1}")
            time.sleep(3)
            followers = self.browser.find_element_by_xpath(
                "//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
            time.sleep(3)
            dialog = self.browser.find_element_by_xpath(
                "/html/body/div[5]/div/div/div[2]")
            followerCount = len(dialog.find_elements_by_tag_name("li"))
            print(f"first count:{followerCount}")
            action = webdriver.ActionChains(self.browser)
            while True:
                dialog.click()
                action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                time.sleep(3)
                newCount = len(dialog.find_elements_by_tag_name("li"))
                if followerCount != newCount or newCount == 24:
                    print(f"New count:{newCount}")
                    time.sleep(3)
                    followerCount = newCount
                else:
                    break
            followers = dialog.find_elements_by_tag_name("li")
            followersList = []
            for user in followers:
                link = user.find_element_by_css_selector(
                    "a").get_attribute("href")
                # print(link)
                followersList.append(link)
            with open("InstaBot/followers.txt", "w", encoding="UTF-8") as file:
                for item in followersList:
                    file.write(item+"\n")
            time.sleep(5)
        except:
            print("Beklenmeyen Hata Oluştu.")

    def getFollowing(self):
        try:
            self.browser.get(f"https://www.instagram.com/{self.username1}")
            time.sleep(2)
            following = self.browser.find_element_by_xpath(
                "//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a").click()
            time.sleep(2)
            dialog = self.browser.find_element_by_xpath(
                "/html/body/div[5]/div/div/div[2]")
            followingCount = len(dialog.find_elements_by_tag_name("li"))
            print(f"First count {followingCount}")
            action = webdriver.ActionChains(self.browser)
            while True:
                dialog.click()
                action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                time.sleep(3)
                newCount = len(dialog.find_elements_by_tag_name("li"))
                if followingCount != newCount or followingCount == 24:
                    print(f"New count:{newCount}")
                    time.sleep(3)
                    followingCount = newCount
                else:
                    break
            following = dialog.find_elements_by_tag_name("li")
            followingList = []
            for user in following:
                link = user.find_element_by_css_selector(
                    "a").get_attribute("href")
                # print(link)
                followingList.append(link)
            with open("InstaBot/following.txt", "w", encoding="UTF-8") as file:
                for item in followingList:
                    file.write(item+"\n")
            time.sleep(5)
        except:
            print("Beklenmeyen Hata Oluştu.")

    def followUser(self, username1):
        self.browser.get("https://instagram.com/"+username1)
        time.sleep(2)
        followButton = self.browser.find_element_by_tag_name("button")
        print(followButton.text)
        if followButton.text != "Mesaj Gönder":
            followButton1 = self.browser.find_element_by_xpath(
                "//*[@id='react-root']/section/main/div/header/section/div[1]/div[1]/div/div/button").click()
            time.sleep(5)
        elif followButton.text == "İstek Gönderildi":
            print("Zaten İstek Atmışsın")
        else:
            print("Zaten takiptesin")

    def unFollowUser(self, username1):
        self.browser.get("https://instagram.com/"+username1)
        time.sleep(2)
        unFollowButton = self.browser.find_element_by_tag_name("button")
        if unFollowButton.text == "Mesaj Gönder":
            unFollowButton1 = self.browser.find_element_by_xpath(
                "//*[@id='react-root']/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button").click()
            time.sleep(2)
            unFollowButton2 = self.browser.find_element_by_xpath(
                "/html/body/div[5]/div/div/div/div[3]/button[1]").click()
            time.sleep(2)
        elif unFollowButton.text == "İstek Gönderildi":
            unFollowButton1 = self.browser.find_element_by_xpath(
                "//*[@id='react-root']/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button").click()
            time.sleep(2)
            unFollowButton2 = self.browser.find_element_by_xpath(
                "/html/body/div[5]/div/div/div/div[3]/button[1]").click()
            time.sleep(2)
        else:
            print("Zaten takip etmiyorsun")

    def notFollowing(self):
        notFollowing = []
        with open("InstaBot/followers.txt", "r", encoding="UTF-8") as followersFile:
            followers = followersFile.readlines()
        with open("InstaBot/following.txt", "r", encoding="UTF-8") as followingFile:
            following = followingFile.readlines()
        for i in following:
            if i not in followers:
                notFollowing.append(i)
                with open("InstaBot/notFollowing.txt", "w", encoding="UTF-8") as file:
                    for item in notFollowing:
                        file.write(item+"")

    def sendMessage(self):
        time.sleep(2)
        self.browser.get("https://www.instagram.com/direct/inbox/")
        time.sleep(2)
        notNowButton = self.browser.find_element_by_xpath(
            "/html/body/div[4]/div/div/div/div[3]/button[2]")
        notNowButton.click()
        time.sleep(5)
        clickUser = self.browser.find_element_by_xpath(
            "//*[@id='react-root']/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a/div/div[1]/div/span/img")
        clickUser.click()
        time.sleep(10)
        i = 0
        while(i < 1000):
            messageButton = self.browser.find_element_by_xpath(
                "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").click()
            self.browser.find_element_by_xpath(
                "//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys("CcC TÜRKLER GELİYOR")
            self.browser.find_element_by_xpath(
                "//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys(Keys.ENTER)
            i += 1


insta = Instagram(username, username1, password)

time.sleep(10)
print("\n\n\n\n\n\n")
print("*********HOŞGELDINIZ*********")
print("Yapmak istediğiniz işlemi seçiniz:")
print("1-Son mesaj attığın kişiye mesaj yolla")
print("2-Takipçileri al")
print("3-Takip ettiklerini al")
print("4-Seni takip etmeyenleri bul")
print("5-Kullanıcıyı takipten çıkar")
print("6-Kullanıcıyı takip et")
secim = int(input())
if secim == 1:
    insta.signIn()
    insta.sendMessage()
elif secim == 2:
    insta.signIn()
    insta.getFollowers()
elif secim == 3:
    insta.signIn()
    insta.getFollowing()
elif secim == 4:
    insta.signIn()
    insta.getFollowers()
    insta.getFollowing()
    insta.notFollowing()
elif secim == 5:
    insta.signIn()
    insta.unFollowUser(username1)
elif secim == 6:
    insta.signIn()
    insta.followUser(username1)
else:
    print("Yanlış bir tuşlama yaptınız")

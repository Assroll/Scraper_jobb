from selenium import webdriver
from time import sleep

from secrets import username, password

class Maze():
    def __init__(self):
        self.driver = webdriver.Chrome("C:\webdriver\chromedriver.exe")


    def login(self):
        #Goes into the adress
        self.driver.get('https://no.mymaze.com/')
        

        sleep(2)

        #Click logginbutton
        login_button = self.driver.find_element_by_xpath('//*[@id="menu-item-479"]/a')
        login_button.click()

        

        email_in = self.driver.find_element_by_id('ContentLoginContainer_tbEmail')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_id('ContentLoginContainer_tbPassword')
        #pw_in.click()
        pw_in.send_keys(password)

        sleep(3)

        sign_in = self.driver.find_element_by_xpath('//*[@id="ContentLoginContainer_LoginButton"]')
        sign_in.click()

        tips = self.driver.find_element_by_xpath('//*[@id="SCC_8359_strc_8359_92E76EE9EE2B529C_comp_80054"]/div[1]/div')
        tips.click()

        #bolig = self.driver.find_element_by_xpath('/html/body/form/div[1]/table/tbody/tr[2]/td[2]/iframe')

        #iframe = self.find_element_by_tag_name('iframe')[index]
        self.driver.switch_to_frame(iframe)
        #iframe = self.driver.find_element_by_xpath('/html/body/form')
        
        print("No of frames present in the web page are: ", len(seq))
        
        #self.driver.find_elements_by_tag_name('iframe')


       # self.driver.switchTo().frame(0)
        
       # self.driver.find_elements_by_class_name
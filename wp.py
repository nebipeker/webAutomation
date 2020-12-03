from selenium import webdriver
import time

def main(contact, message):

    browser = webdriver.Chrome("/Users/Alpha/Desktop/chromedriver")
    browser.get("https://web.whatsapp.com/")
    time.sleep(5)
    search = browser.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]")
    search.send_keys(contact)
    time.sleep(5)
    chatselector = browser.find_element_by_xpath("//span[@title='"+contact+"']")
    chatselector.click()
    chattextbox = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div")
    sendbutton = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]")
    while True:
        chattextbox.send_keys(message)
        time.sleep(0.5)
        sendbutton.click()

main('', '')
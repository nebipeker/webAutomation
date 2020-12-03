from selenium import webdriver
import time

def getter(username, password,browser):
    browser.get("https://www.instagram.com/")
    time.sleep(1)
    instalogin(username,password,browser)
    gotoProfile(username,browser)
    time.sleep(1)
    follower= browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")
    follower.click()
    time.sleep(1)
    followlist = getlist('isgrP',browser)
    time.sleep(3)
    gotoProfile(username, browser)
    following = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a")
    following.click()
    time.sleep(3)
    followinglist = getlist('isgrP',browser)

    browser.quit()
    return followlist,followinglist


def gotoProfile(username, browser):
    browser.get('https://www.instagram.com/'+username)
    time.sleep(3)

def instalogin(username,password,browser):
    usernamebox = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
    passwordbox = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")
    usernamebox.send_keys(username)
    passwordbox.send_keys(password)
    loginbutton = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button/div")
    loginbutton.click()
    time.sleep(2.5)

def getlist(classname, browser):
    jscommand = """
        followers = document.querySelector(".{}");
        followers.scrollTo(0, followers.scrollHeight);
        var lenOfPage=followers.scrollHeight;
        return lenOfPage;

        """.format(classname)
    lenOfPage = browser.execute_script(jscommand)
    match = False
    while (match == False):
        lastCount = lenOfPage
        time.sleep(1)
        lenOfPage = browser.execute_script(jscommand)
        if lastCount == lenOfPage:
            match = True
    time.sleep(5)
    listt = []
    followerbox = browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa ")
    for item in followerbox:
        listt.append(item.text)
    return listt

def main(username, password,path):
    browser = webdriver.Chrome(path)
    username=username
    password=password
    follower,following = getter(username,password,browser)
    print(following)
    print("now follower")
    print(follower)
    for i in following:
        if i not in follower:
           print(i)

username=''
password=''
path='' #"/Users/Alpha/Desktop/chromedriver"
main(username,password,path)
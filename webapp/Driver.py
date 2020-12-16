from time import sleep
from selenium import webdriver
import random
import Utilities

# 'Start' of the code
# Initialise browser and go to instagram.com
browser = webdriver.Firefox()
browser.implicitly_wait(5)


def main_loop(username, password):
    print("Initialising browser...\n")
    print("Connecting to instagram.com...\n")
    browser.get('https://www.instagram.com/')

    sleep(2)

    print("Accepting Cookies...\n")
    accept_cookies_button = browser.find_element_by_xpath(
        '/html/body/div[2]/div/div/div/div[2]/button[1]')
    accept_cookies_button.click()

    sleep(2)

    print("Searching for input field...\n")
    username_input = browser.find_element_by_css_selector(
        "input[name='username']")
    password_input = browser.find_element_by_css_selector(
        "input[name='password']")

    print("Writing in your data...\n")
    username_input.send_keys(username)
    password_input.send_keys(password)

    print("Clicking submit...\n")
    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()

    sleep(5)

    while True:
        click_comment_repeat()
        sleep(2)


# Functions for better modularity of the code
def click_comment_repeat():
    print("Connecting to instagram.com/explore...\n")
    browser.get('https://www.instagram.com/explore/')
    sleep(5)
    print("Fetching images...\n")
    images = browser.find_elements_by_tag_name("a")
    print("Clicking random image...\n")
    link = random.choice(images).get_attribute('href')
    while "/p/" not in link:
        link = random.choice(images).get_attribute('href')

    print("Got image on link: " + link)
    browser.get(link)

    sleep(2)

    print("Liking the image\n")
    like_button = browser.find_element_by_xpath(
        '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button')
    like_button.click()

    sleep(2)

    print("Writing the comment\n")
    comment_input = browser.find_element_by_xpath(
        '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea')

    comment_input.click()
    sleep(1)

    comment_input = browser.find_element_by_xpath(
        '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea')

    comment = random.choice(Utilities.comments)
    comment_input.send_keys(comment)
    comment_input.submit()

    print("Wrote: " + comment)

    sleep(2)


# browser.close()

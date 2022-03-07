from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep


#Credentials 
print("Entre your email or phone number: ")
username = input()
print("Entre your password: ")
psswd = input() 

#Tweet
print("What do you want to tweet?")
tweet = input()


print("Connecting...")

#Importing the browser
browser = webdriver.Firefox()
browser.get("http://twitter.com/i/flow/login")

sleep(5)

email = browser.find_element_by_css_selector('.r-30o5oe').send_keys(username)

nextButton =  browser.find_element_by_css_selector('div.css-18t94o4:nth-child(6) > div:nth-child(1)').click()

sleep(5)

password = browser.find_element_by_css_selector('.r-homxoj').send_keys(psswd)


login = browser.find_element_by_css_selector('.r-1sw30gj > div:nth-child(1)').click()


tweetButton = browser.find_element_by_css_selector('span.r-1inkyih:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1)').click()


writing_tweet = browser.find_element_by_css_selector('.public-DraftStyleDefault-block')

sleep(5)

ActionChains(browser).move_to_element(writing_tweet).click(writing_tweet).send_keys(tweet).perform()

send_tweet = browser.find_element_by_css_selector('div.r-l5o3uw:nth-child(4) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1)').click()

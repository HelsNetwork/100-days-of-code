from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


browser = webdriver.Firefox()
browser.get("http://twitter.com/i/flow/login")

sleep(10)

username = browser.find_element_by_css_selector(".r-30o5oe").send_keys("USERNAME")

next = browser.find_element_by_css_selector(
    "div.css-18t94o4:nth-child(6) > div:nth-child(1)"
).click()

sleep(5)

psswd = browser.find_element_by_css_selector(".r-homxoj").send_keys("PASSWORD")

login = browser.find_element_by_css_selector(".r-1sw30gj > div:nth-child(1)").click()

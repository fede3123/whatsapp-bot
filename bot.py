from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from time import sleep

driver = webdriver.Firefox()
# Goes to url
driver.get('https://web.whatsapp.com/')
print("In")
sleep(20)
# Find the chat
Chat = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1"]/div/div/div[11]/div/div')
Chat.click()
print("I got chat")
Write = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]')

# Send message
Write.send_keys('Hello world')

Write.send_keys(Keys.ENTER)

print("Message send")

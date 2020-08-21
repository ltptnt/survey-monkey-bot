import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

x=0

while True:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("-incognito") 
    driver = webdriver.Chrome(executable_path='LOCATION OF WEBDRIVER.EXE', options=chrome_options)
    driver.get('URL OF THE SURVEY MONKEY')
    
#Use inspect element to loctate the element or follow README. This can be modified to locate a button and then vote.click() can be used to click it 
    
    vote = driver.find_element_by_id('ID OF THE TEXTBOX')
    vote.send_keys('WHAT YOU WOULD LIKE TYPED IN THE TEXTBOX')


#This code locates the submit button and should work with any program
    
    vote_submit = driver.find_element_by_xpath("//button[contains(text(), ' Done')]")
    vote_submit.click()
    time.sleep(3)
    driver.close()

#replace 4 with the number of times you would like the program to run
    
    x=x+1
    if x==4:
        break


driver.quit()

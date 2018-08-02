from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import numpy
import requests
import time
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py

'''function declaration'''

def remove_emoji(string):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)


web_page = "https://www.instagram.com/p/Bl7pSQehs6Z/?taken-by=student.design"
page_response = requests.get(web_page, timeout=5)
soup = BeautifulSoup(page_response.content, "html.parser")

option = webdriver.ChromeOptions()
option.add_argument("--incognito")

browser = webdriver.Chrome(executable_path='C:/webdrivers/chromedriver', chrome_options=option)
browser.get("https://www.instagram.com/p/Bl7pSQehs6Z/?taken-by=student.design")

timeout = 20
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, '//img[@class="FFVAD"]')))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()

comment_array = []

while True:
    try :
        WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, '//a[@class="vTJ4h Dz3II"]')))
        load_more = browser.find_element(By.XPATH, '//a[@class="vTJ4h Dz3II"]')
        load_more.click()
        
    except TimeoutException:
        break
        
comments = browser.find_elements_by_xpath("//div[@class='C4VMK']/span")

for comment in comments:
    
    comment = comment.text
    comment = remove_emoji(comment)
    comment_array.append(comment)
    ##print(comment)
'''make counter fo bar graph'''

one = 0
two = 0
three = 0

for item in comment_array:
    if item == '1':
        one = one + 1
    if item == '2':
        two = two + 1
    if item == '3':
        three = three + 1

y = comment_array
N = len(y)
x = range(N)
width = 1/1.5
plt.bar(x, y, width, color="blue")


fig = plt.gcf()
plot_url = py.plot_mpl(fig, filename='mpl-basic-bar')
 
    

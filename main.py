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

# Global Variables #
one = 0
two = 0
three = 0

# Function Declarations #
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

# Soup setup #
web_page = "https://www.instagram.com/p/Bl7pSQehs6Z/?taken-by=student.design"
page_response = requests.get(web_page, timeout=5)
soup = BeautifulSoup(page_response.content, "html.parser")

# Selenium/Chromedriver setup #
option = webdriver.ChromeOptions()
option.add_argument("--incognito")
browser = webdriver.Chrome(executable_path='C:/webdrivers/chromedriver', chrome_options=option)
browser.get("https://www.instagram.com/p/Bl7pSQehs6Z/?taken-by=student.design")

# Handles page timeout #
timeout = 20
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, '//img[@class="FFVAD"]')))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()



while True:
    try :
        WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, '//a[@class="vTJ4h Dz3II"]')))
        load_more = browser.find_element(By.XPATH, '//a[@class="vTJ4h Dz3II"]')
        load_more.click()
        
    except TimeoutException:
        break

comment_array = []     
comments = browser.find_elements_by_xpath("//div[@class='C4VMK']/span")

# Count the # of comments #
counter = 0
for comment in comments:

    comment = comment.text
    comment = remove_emoji(comment)
    comment_array.append(comment)
    counter = counter + 1
'''make counter fo bar graph'''


# Count # and type of votes and store into array #
for item in comment_array:
    if item == '1':
        one = one + 1
    if item == '2':
        two = two + 1
    if item == '3':
        three = three + 1
    performance = [one, two, three]

performance_counter = one+two+three
objects = ('1', '2', '3')
y_pos = np.arange(len(objects))
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('# Votes')
plt.title('Instagram Vote Counting Machine')

# Calculate accuracy of model
accuracy = ((1-(counter-performance_counter)/counter))*100

# Print everything
print('There are ' + str(counter) + ' votes')
print('There are ' + str(performance_counter) +  ' votes counted')
print('The machine is displaying with ' + str(accuracy) + ' % accuracy')

plt.show()


from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Chrome("I:\Coding-Part-2-Python\Python-3 ( C127 onwards )\Projects\PRO-C127\chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

scraped_data = []

# Define Exoplanet Data Scrapping Method
def scrape():
    soup = BeautifulSoup(browser.page_source , 'html.parser')
    bright_star_table = soup.find('table' , attrs={'class' , 'wikitable'})
    table_body = bright_star_table.find('tbody')
    table_rows = table_body.find_all('tr')
    for row in table_rows:
        table_coloumn = row.find_all('td')
        temp_list = []
        for column_data in table_coloumn:
            data = column_data.text.strip()
            temp_list.append(data)
        scraped_data.append(temp_list)

  
# Calling Method    
scrape()
stars_data = []
for i in range(0, len(scraped_data)):
    star_name = scraped_data[i][1]
    distance_name = scraped_data[i][3]
    mass = scraped_data[i][5]
    radius = scraped_data[i][6]
    lum = scraped_data[i][7]
    required_data = [star_name , distance_name , mass , radius, lum]
    stars_data.append(required_data)
print(stars_data)
# Define Header
headers = ["star_name" , "distance" , "mass" , "radius" , "luminosity"]

# Define pandas DataFrame   
stars_ts_1 = pd.DataFrame(stars_data , columns = headers)

# Convert to CSV
stars_ts_1.to_csv('stars_info.csv' , index = True , index_label='id')

    



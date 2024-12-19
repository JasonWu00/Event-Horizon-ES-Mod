"""
A Python script to auto-fill-in some of the descriptions for some components.
"""
import json
import os
import time
#import requests
from selenium import webdriver # 7vn pages load dynamically, requests cant handle it
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

COMPONENTS_PATH = "../Components/"
ES_7VN_LINK = "http://dev.endless-sky.7vn.io/outfits/"
USERAGENT = "404found_eh_es_parser/1.0 (https://github.com/JasonWu00/Event-Horizon-ES-Mod; https://github.com/JasonWu00)"

def fill_in_descs(path: str):
    """
    Given a directory, recursively inspect all subdirectories
    and fill in descriptions for all eligible json files.
    """
    dir_list = os.listdir(path)

    for filename in dir_list:
        if ".json" in filename: # begin description filling process
            with open(path+"/"+filename, 'r+', encoding='utf-8') as file:
                data = json.load(file)

                if data["ItemType"] != 1: # ItemType 1 is components, all others is comp stats
                    continue

                compname = data["Name"]

                # r = requests.get(ES_7VN_LINK+compname, timeout=10,
                #                  headers={"User-Agent": USERAGENT})
                browser = webdriver.Chrome() # create a Selenium web driver to handle dynamic pages
                final_link = ES_7VN_LINK+compname.replace(' ', '-').lower()
                print(f"Looking at this webpage: {final_link}")
                browser.get(final_link)
                found = browser.find_element('class name', 'col-md-4')
                wait = WebDriverWait(browser, timeout=2)
                wait.until(lambda d : found.is_displayed())
                time.sleep(2) # 7vn loads the main page, then the actual data a split second later; 2s eliminates any chances of slow loads
                html = browser.page_source
                soup = BeautifulSoup(html, 'html.parser')
                browser.close() # close the window so Chrome doesn't eat my entire ram
                print(f"Grabbing data for itemname {compname}")
                print(soup)
                #print(compname)
                all_pars = soup.find_all(['div'], attrs={'class': 'col-md-4'})[0] # item description is in a div element

                for para in all_pars:
                    if "No description" in para.get_text().strip(): # Empty pages has no description in div
                        print(f"No description for {compname}")
                        break
                    # Else:
                    description = para.get_text().strip()
                    description = description.replace('\n', ' ')
                    if description[:len(description)-1] == ' ':
                        description = description[:len(description)-2] # remove trailing whitespace
                    data["Description"] = description
                    print(data)
                    print(type(data))
                    file.seek(0) # move back to start of file to overwrite file instead of appending
                    json.dump(data, file) # write the updated json to data folder
                    file.truncate() # in case any old data remains
                    break
                
        elif "Stats" not in filename: # ignore Components Stats folder
            fill_in_descs(path+"/"+filename)

fill_in_descs(COMPONENTS_PATH)
#browser = webdriver.Chrome() # create a Selenium web driver to handle dynamic pages
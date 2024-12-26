"""
A Python script to auto-fill-in some of the descriptions for some components.
"""
import json
import os
import time
#import requests
from selenium import webdriver # 7vn pages load dynamically, requests cant handle it
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

COMPONENTS_PATH = "../Components"
WEAPONS_PATH = "../Weapons/Weapons By Faction"
ES_7VN_LINK = "http://dev.endless-sky.7vn.io/"
OUTFITS = "outfits/"
SHIPS = "ships/"
USERAGENT = "404found_eh_es_parser/1.0 (https://github.com/JasonWu00/Event-Horizon-ES-Mod; https://github.com/JasonWu00)"
INDEXERROR = "IndexError"
NO_DESC = "No description."

def fill_in_descs(path: str, specific_files = None, selective_fill = True):
    """
    Given a directory, recursively inspect all subdirectories
    and fill in descriptions for all eligible json files.

    path: a path to the folder with component jsons.
    selective_fill: whether to skip over jsons with descriptions already.
    specific_files: a list of json files to fill in, or None by default.
    """
    print(f"Path is: {path}")
    if specific_files != []:
        dir_list = specific_files
    else:
        dir_list = os.listdir(path)

    for filename in dir_list:
        if ".json" in filename: # begin description filling process
            with open(path+"/"+filename, 'r+', encoding='utf-8') as file:
                data = json.load(file)
                itemtype = data["ItemType"]
                print(f"Checking filename {filename}")
                print(f"Item type is {itemtype}")
                if itemtype != 1: # ItemType 1 is components, all others is comp stats
                    print(f"Skipping non-component file {filename}")
                    continue
                compname = data["Name"]
                print(f"Selective fill value is: {selective_fill}")
                if "Description" in data and selective_fill is True:
                    print(f"Skipping file with item name {compname}; desc already here")
                    continue


                # r = requests.get(ES_7VN_LINK+compname, timeout=10,
                #                  headers={"User-Agent": USERAGENT})
                # modify the final link to match the 7vn url naming scheme
                final_link=ES_7VN_LINK+OUTFITS+compname.replace(' ', '-').replace('\'', '').lower()

                soup = grab_page_with_selenium(final_link)
                print(f"Grabbing data for itemname {compname}")
                #print(soup)
                #print(compname)

                description = check_bs4_for_desc(soup, compname)
                if description == INDEXERROR: # index error of some sort; manually check later
                    description = NO_DESC
                if description == NO_DESC and data["DisplayCategory"] == 5:
                    # drones use ship descriptions
                    # drones have DisplayCategory 5

                    # modify final link to point to ships section
                    final_link=ES_7VN_LINK+SHIPS+\
                        compname.replace(' ', '-').replace('\'', '').lower()
                    soup = grab_page_with_selenium(final_link)
                    # Ship pages use "well" class for the description
                    description = check_bs4_for_desc(soup, compname, find_class="well")
                if description == INDEXERROR: # index error of some sort; manually check later
                    description = NO_DESC
                if "Description" in data and description==NO_DESC and data["Description"]!=NO_DESC:
                    print(f"Ignoring {filename}; desc already here")
                    # avoids overwriting existing descs with no_desc
                    continue

                data["Description"] = description
                print(data)
                print(type(data))
                file.seek(0) # move back to start of file to overwrite file instead of appending
                json.dump(data, file, indent=2) # write the updated json to data folder
                file.truncate() # in case any old data remains

        elif "Stat" not in filename and "." not in filename:
            # ignore all Components Stats folders, recursively check other folders
            # Also ignore files (they have extensions)
            fill_in_descs(path+"/"+filename, selective_fill=selective_fill)

def grab_page_with_selenium(link: str):
    """
    Given a link, use Selenium to parse its values and pass it back.

    link: an HTML link.
    """
    browser = webdriver.Chrome() # create a Selenium web driver to handle dynamic pages
    #browser.minimize_window() # I don't want Chrome windows popping up every 5 minutes
    # Turns out minimize windows cause some 7vn pages to not load at all; this is commented out.

    print(f"Looking at this webpage: {link}")
    browser.get(link)

    # a failed attempt at smart waiting; went back to using dumb waiting
    #found = browser.find_element(By.CLASS_NAME, 'col-md-4')
    #wait = WebDriverWait(browser, timeout=2)
    #wait.until(found.is_displayed())
    time.sleep(4) # 7vn loads the main page, then the actual data a split second later; needs 4s
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    browser.close() # close the window so Chrome doesn't eat my entire ram
    return soup

def check_bs4_for_desc(soup: BeautifulSoup, compname: str, find_class = 'col-md-4'):
    """
    Takes in a bs4 object, looks for a given item, returns it.

    soup: a BeautifulSoup object containing data for a webpage.
    compname: name of a component, used for debug printing purposes.
    find_class: the HTML class to look for when searching. Default is 'col-md-4' for outfits.
    """
    try:
        all_pars = soup.find_all(['div'], attrs={'class': find_class})[0] # item desc is in a div

        for para in all_pars:
            if NO_DESC in para.get_text().strip(): # Empty pages has no description in div
                print(f"No description for {compname}")
                return NO_DESC
            # Else:
            description = para.get_text().strip()
            description = description.replace('\n', ' ')
            if description[:len(description)-1] == ' ':
                description = description[:len(description)-2] # remove trailing whitespace
            return description

    except IndexError:
        print(f"IndexError reached for file {compname}")
        return INDEXERROR

# for subdir in ["Syndicate"]:
#     fill_in_descs(COMPONENTS_PATH+"/"+subdir, selective_fill=False)
#fill_in_descs(COMPONENTS_PATH+"/"+"Hai", specific_files=["pebble core.json", "sand cell.json"],
#              selective_fill=False)
#fill_in_descs(COMPONENTS_PATH+"/"+"Merchant", selective_fill=False)
fill_in_descs(WEAPONS_PATH, selective_fill=False)
# for subdir in ["Bunrodea"]:
#     fill_in_descs(WEAPONS_PATH+"/"+subdir, selective_fill=False)

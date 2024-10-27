import pandas as pd
import numpy as np
import re
from bs4 import BeautifulSoup
import requests
import os

path_to_es_data = "C:/Users/jason/OneDrive/Desktop/endless-sky/data"
# using human data as a small test

list_of_filenames = []
list_of_engine_stats = []
for folder in os.listdir(path_to_es_data):
    if '.' not in folder:
        for file in os.listdir(path_to_es_data+"/"+folder):
            if "engine" in file or "outfit" in file:
                list_of_filenames.append(folder+"/"+file)
print(list_of_filenames)

for file in list_of_filenames: # for every data file
    with open(path_to_es_data+"/"+file, "r") as filedata:
        
        contents = filedata.read()
        lines = contents.split("\n") # turn text into a list of lines
        engine_stats_keywords = ["thrust", "thrusting energy", "thrusting heat", "turn", "turning heat", "turning energy",
                                 "reverse thrust", "reverse thrusting energy", "reverse thrusting heat"]
        exclude_keywords = ["description", "thumbnail", "#"]
        found_engine = False

        for line in lines:
            #print(line)
            if any(keyword in line for keyword in ["Steering", "Thruster", "Engines"]) and line.count("\t") == 0 \
                and not any(bad_keyword in line for bad_keyword in exclude_keywords):

                #print(line)
                name = re.findall(r'"(.*?)"', line)[0]
                # https://stackoverflow.com/questions/171480/regex-grabbing-values-between-quotation-marks

                outfit_object = {"Name": name}
                found_engine = True

            elif found_engine and line.count("\t") >= 1: # sublines containing stats
                #print(line)
                if any(keyword in line for keyword in engine_stats_keywords) \
                    and not any(bad_keyword in line for bad_keyword in exclude_keywords):

                    stat_keyword = re.findall(r'"(.*?)"', line)[0]
                    stat_value = re.findall(r'[0-9\.]+', line)[0]
                    outfit_object[stat_keyword] = stat_value
            elif line == "" and found_engine: # end of the object

                list_of_engine_stats.append(outfit_object)
                found_engine = False

df = pd.DataFrame(list_of_engine_stats)
print(df.head(10))

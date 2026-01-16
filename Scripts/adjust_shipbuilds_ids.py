import json
import os
import time
import re
from typing import Optional

SHIPS_PATH = "../Ships"

def replace_shipids(path: str,):
    """
    Docstring for replace_shipids
    
    :param path: a path to the folder with component jsons.
    :type path: str
    """
    print(f"Path is: {path}")
    dir_list = []
    dir_list = os.listdir(path)

    for filename in dir_list:
        print(filename)
        if filename != "Ships" and "." not in filename: # all folders not named Ships
            replace_shipids(path+"/"+filename)
        elif ".json" in filename: # begin description filling process
            with open(path+"/"+filename, 'r+', encoding='utf-8') as file:
                data: dict = json.load(file)
                if data["ItemType"] != 8: # all ship builds have itemtype 8
                    continue
                #buildid: int = data["Id"]
                shipid: int = data["ShipId"]
                if shipid >= 1000: # all "main line" ships have ids between 300 and ~540
                    continue
                difficultyclass: int = 0 if "DifficultyClass" not in data else data["DifficultyClass"]
                if data["Id"] == shipid * 10 + difficultyclass:
                    continue
                data["Id"] = shipid * 10 + difficultyclass
                file.seek(0) # move back to start of file to overwrite file instead of appending
                json.dump(data, file, indent=2) # write the updated json to data folder
                file.truncate() # in case any old data remains

def write_new_ids(match):
    shipid = int(match.group(1))
    return f"{shipid} | {shipid*10}-{shipid*10+2}"

def replace_docs_shipids():
    """
    Docstring for replace_docs_shipids
    """
    path = "../Documentation/documentation.md"
    with open(path, 'r+', encoding='utf-8') as file:
        content = file.read()
        #print(len(content))
        pattern = r"([0-9]{3}) \| ([0-9]{4})-([0-9]{4})"
        result = re.sub(pattern, write_new_ids, content)
        file.seek(0)
        file.write(result)
        file.truncate()

replace_docs_shipids()

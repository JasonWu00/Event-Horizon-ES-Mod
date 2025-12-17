import json
import os
import time
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
        if filename != "Ships" and "." not in filename: # all folders not named Ships
            replace_shipids(path+"/"+filename)
        elif ".json" in filename: # begin description filling process
            with open(path+"/"+filename, 'r+', encoding='utf-8') as file:
                data: dict = json.load(file)
                #buildid: int = data["Id"]
                shipid: int = data["ShipId"]
                if shipid >= 1000: # all "main line" ships have ids between 300 and ~540
                    continue
                difficultyclass: int = 0 if "DifficultyClass" not in data else data["DifficultyClass"]
                data["Id"] = shipid * 10 + difficultyclass
                file.seek(0) # move back to start of file to overwrite file instead of appending
                json.dump(data, file, indent=2) # write the updated json to data folder
                file.truncate() # in case any old data remains
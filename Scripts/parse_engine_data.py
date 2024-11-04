"""
A short Python script to grab engine stats from the Endless Sky data files
and reform it into a Pandas DataFrame.
"""
import os
import re
import pandas as pd

path_to_es_data = "C:/Users/jason/OneDrive/Desktop/endless-sky/data"

list_of_filenames = []
list_of_engine_stats = []
for folder in os.listdir(path_to_es_data):
    if '.' not in folder:
        for file in os.listdir(path_to_es_data+"/"+folder):
            if "engine" in file or "outfit" in file:
                list_of_filenames.append(folder+"/"+file)
print(list_of_filenames)

for file in list_of_filenames: # for every data file
    with open(path_to_es_data+"/"+file, "r", encoding="utf-8") as filedata:

        contents = filedata.read()
        lines = contents.split("\n") # turn text in file into a list of lines
        # lines to read: engine force, energy, heat for turn, thrust, reverse
        engine_stats_keywords = ["outfit space", "thrust", "thrusting energy", "thrusting heat", "turn",
                                 "turning heat", "turning energy", "reverse thrust",
                                 "reverse thrusting energy", "reverse thrusting heat"]
        # lines to skip: comments, thumbnails, descriptions
        exclude_keywords = ["description", "thumbnail", "#"]
        found_engine = False

        for line in lines:
            #print(line)
            if any(keyword in line for keyword in ["Steering", "Thruster", "Engines", "Thrust", "Reverse"]) \
                and line.count("\t") == 0 \
                and not any(bad_keyword in line for bad_keyword in exclude_keywords):

                #print(line)
                name = re.findall(r'"(.*?)"', line)[0]
                name_hai = re.findall(r'`(.*?)`', line)
                #print(name_hai)
                if name_hai != []: name = name_hai[0]
                # https://stackoverflow.com/questions/171480/regex-grabbing-values-between-quotation-marks

                outfit_object = {"Name": name}
                found_engine = True

            elif found_engine and line.count("\t") >= 1: # sublines containing stats
                #print(line)
                if any(keyword in line for keyword in engine_stats_keywords) \
                    and not any(bad_keyword in line for bad_keyword in exclude_keywords):
                    #print(line)
                    stat_keyword = re.findall(r'"(.*?)"', line)[0]
                    stat_value = re.findall(r'[0-9\.]+', line)[0]
                    outfit_object[stat_keyword] = float(stat_value)
            elif line == "" and found_engine: # end of the object

                list_of_engine_stats.append(outfit_object)
                found_engine = False

df = pd.DataFrame(list_of_engine_stats).fillna(0)
df["thrust"] = df["thrust"] * 3600
df["turn"] = df["turn"] * 60
df["reverse thrust"] = df["reverse thrust"] * 3600
df["thrust per space"] = (df["thrust"] + df["reverse thrust"]) / df["outfit space"]
df["thrust per space"] = df["thrust per space"].round(3)
df["turn per space"] = df["turn"] / df["outfit space"]
df["turn per space"] = df["turn per space"].round(3)
print(df.head(14))
df_ion_engines = df[df["Name"].str.contains(" Ion ")]
print(df_ion_engines)
#df.to_csv("engines_stats.csv", index=False)
df_ion_engines.to_csv("engine_stats_baselines.csv", index=False)

import json
import os
import re

sql_dataset_path = "/home/pavel/BaoForPostgreSQL/long_dataset"
json_dataset_path = "/home/pavel/hybridQO/HyperQO/workload/JOB_selected.json"

queires = []

float_conversion_right = re.compile(r'\b(\d+(?:\.\d+)?)\s*((?:<=|>=|<|>))\s*([a-zA-Z_][\w]*\.[a-zA-Z_][\w]*)::float\b')
sub_float_conversion_right = r"'\1' \2 \3"

float_conversion_left = re.compile(r'\b([a-zA-Z_][\w]*\.[a-zA-Z_][\w]*)::float\s*((?:<=|>=|<|>))\s*(\d+(?:\.\d+)?)\b')
sub_float_conversion_left = r"\1 \2 '\3'"

for filename in os.listdir(sql_dataset_path):
    with open(sql_dataset_path + "/" + filename, "r") as f:
        sql = " ".join(f.readlines())
        sql = re.sub(float_conversion_right, sub_float_conversion_right, sql)
        sql = re.sub(float_conversion_left, sub_float_conversion_left, sql)
    
    queires.append([sql, filename, [0, False]])

with open(json_dataset_path, "w+") as f:
    json.dump(obj=queires, fp=f)
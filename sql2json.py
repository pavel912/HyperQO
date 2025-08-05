import json
import os

sql_dataset_path = "/home/pavel/BaoForPostgreSQL/long_dataset"
json_dataset_path = "/home/pavel/hybridQO/HyperQO/workload/JOB_selected.json"

queires = []

for filename in os.listdir(sql_dataset_path):
    with open(sql_dataset_path + "/" + filename, "r") as f:
        sql = " ".join(f.readlines())
    
    queires.append([sql, filename, [0, False]])

with open(json_dataset_path, "w+") as f:
    json.dump(obj=queires, fp=f)

import re
import json

dataset_path = "/home/pavel/hybridQO/HyperQO/workload/JOB_selected.json"

with open(dataset_path, "r") as f:
    dataset = json.load(f)

aliases = set()
alias_re = re.compile(r'\b[\w]+\s+as\s+([\w]+)\b')
for q in dataset:
    sql = q[0].lower()
    for al in re.findall(alias_re, sql):
        aliases.add(al)

aliases = list(aliases)
id2aliasname = {i: aliases[i - 1] for i in range(1, len(aliases) + 1)}
id2aliasname[0] = "start"
aliasname2id = {id2aliasname[i]: i for i in range(1, len(aliases) + 1)}
aliasname2id["start"] = 0

print(f"id2aliasname: {id2aliasname}")
print(f"aliasname2id: {aliasname2id}")
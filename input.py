# date:     11/22/2018
# purpose:  for reading and storing the input data

import json

inputstr = ""
with open("SampleDataset1/SampleDataset1.json", 'r') as file:
    inputstr = file.read()

json_str = json.loads(inputstr)

print(json_str)

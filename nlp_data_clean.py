import json

data = open("dump2014.json", "r")
datadict = json.load(data)

with open("timeseries.json") as ts:

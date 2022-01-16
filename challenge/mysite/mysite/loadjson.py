import json

##Loading in the jsons
json_data = open('./compounds.json',encoding='utf-8-sig')
data1 = json.load(json_data) # deserialises it
data2 = json.dumps(data1) # json formatted string

##Load in the json data
ModelName.objects.create(**json)
json_data.close()
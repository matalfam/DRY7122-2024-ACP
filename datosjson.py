#evaluacion n1 sdn-ndf creacion de json
#grupo 11

import json
import yaml

with open('myfile.json','r') as json_file:
	ourjson = json.load(json_file)

print("====================================")
print("Se mostraran a continuación los archivos pertenecientes a myfiles.json")
print("grupo 11")
print("====================================")
print(ourjson)


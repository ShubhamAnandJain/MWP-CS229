import os
import sys
import numpy as np
import json

f = open('testset.json')
data = json.load(f)

dataset = []

for line in data:
	# print(line)
	question = {}
	for key, value in line.items():

		if key == "Question":
			question[key] = ""
		else:
			question[key] = value

	dataset.append(question)

result = [json.dumps(record) for record in dataset]
jsonFile = open("cleaned_dataset.json", "w")

jsonFile.write('[\n')
for i in result:
	if i == result[-1]: jsonFile.write('\t'+i+'\n')
	else: jsonFile.write('\t'+i+',\n')
jsonFile.write(']\n')
jsonFile.close()
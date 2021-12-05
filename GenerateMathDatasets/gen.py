import json
import pprint
from random import seed
from random import randint

seed(1)

num_questions = [1000, 100, 100] #train, valid, test

low = 1
high = 1000
n_term_train_low = 2
n_term_train_high = 8
n_term_test_low = 2
n_term_test_high = 8

write_file = ["trainset.json", "validset.json", "testset.json"]

tot_curr = 0
challenge_data = 0

for curr_type in range(3):

	dataset = []
	for i in range(num_questions[curr_type]):
		question = {}

		question["iIndex"] = tot_curr + i

		# question["sQuestion"] = "I have some useless text, which is "

		# rexp = ""
		expression = ""
		operators = ["+", "-"]

		# for j in range(randint(n_term_low, n_term_high)):
		# 	add = 1
		# 	if j != 0:
		# 		do_op = operators[randint(0, len(operators)-1)]
		# 		exp += do_op
		# 		if do_op == "-":
		# 			add = -1
			
		# 	x = randint(low, high)
		# 	if(challenge_data==1):
		# 		if(curr_type!=0):
		# 			x = init_gen
			
		# 	rexp += str(x)

		question["sQuestion"] = "What is the value of "

		
		val = 0

		init_gen = randint(low, high)

		n_low = n_term_train_low
		n_high = n_term_train_high

		if curr_type == 2:
			n_low = n_term_test_low
			n_high = n_term_test_high

		for j in range(randint(n_low, n_high)):
			add = 1
			if j != 0:
				do_op = operators[randint(0, len(operators)-1)]
				expression += do_op
				if do_op == "-":
					add = -1
			
			x = randint(low, high)
			if(challenge_data==1):
				if(curr_type!=0):
					x = init_gen
			
			val += add * x
			expression += str(x)

		question["lEquations"] = ["X=" + expression]
		question["lSolutions"] = [val]

		expression = expression.replace("+", " plus ")
		expression = expression.replace("-", " minus ")

		question["sQuestion"] += expression
		question["sQuestion"] += "?"

		dataset.append(question)

	result = [json.dumps(record) for record in dataset]
	jsonFile = open(write_file[curr_type], "w")

	tot_curr += num_questions[curr_type]

	jsonFile.write('[\n')
	for i in result:
		if i == result[-1]: jsonFile.write('\t'+i+'\n')
		else: jsonFile.write('\t'+i+',\n')
	jsonFile.write(']\n')
	jsonFile.close()
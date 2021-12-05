import json
import pprint
from random import seed
from random import randint

seed(1)

num_questions = [1000, 100, 100] #train, valid, test

low = 1
high = 1000
n_term_train_low = 2
n_term_train_high = 5
n_term_test_low = 2
n_term_test_high = 5

write_file = ["trainset.json", "validset.json", "testset.json"]

tot_curr = 0
challenge_data = 0

colors = ["White", "Black", "Red", "Blue", "Green", "Yellow", "Azure", "Brown", "Violet", "Gray", "Golden", "Orange", "Magenta", "Pink"]
num_col = len(colors)

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

		question["sQuestion"] = "Sarah was given "
		to_gen = randint(n_term_train_low, n_term_train_high)

		used_cols = []
		store_val = []

		while(len(used_cols) < to_gen):
			x = randint(0, num_col-1)
			if colors[x] in used_cols:
				continue
			used_cols.append(colors[x])

		for i in range(to_gen-1):
			rng_gen = randint(low, high)
			store_val.append(rng_gen)
			question["sQuestion"] += str(rng_gen) + " " + used_cols[i] + " balls, "

		i += 1

		rng_gen = randint(low, high)
		store_val.append(rng_gen)
		question["sQuestion"] += "and " + str(rng_gen) + " " + used_cols[i] + " balls. "
		
		ask_0 = randint(0, to_gen-1)
		ask_1 = ask_0
		while ask_1 == ask_0:
			ask_1 = randint(0, to_gen-1)

		question["sQuestion"] += "How many more " + used_cols[ask_0] + " balls are there than " + used_cols[ask_1] + " balls?"

		expression = str(store_val[ask_0]) + "-" + str(store_val[ask_1])
		val = store_val[ask_0] - store_val[ask_1]

		question["lEquations"] = ["X=" + expression]
		question["lSolutions"] = [val]

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
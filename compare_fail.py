import os

models = ['GroupATT', 'MathEN', 'Graph2Tree']
dataset = 'SVAMP'
task_type = 'single_equation'
equation_fix = 'prefix'
folder = 'failure_cases'

if not os.path.exists(folder):
	os.makedirs(folder)

questions_list = {}

for model_name in models:

	script = "python3 run_mwptoolkit.py --model=" + model_name + " --dataset=" + dataset 
	script = script + " --task_type=" + task_type + " --equation_fix=" + equation_fix 
	script = script + " --k_fold=5 --test_step=5 --gpu_id=0 --test_only=True > "
	file_save = folder + '/' + "fail_" + model_name + "_" + dataset + ".txt"

	script = script + file_save

	os.system(script)
	f = open(file_save, "r")

	lines = f.readlines()

	for line in lines:
		terms = line.split(' ')
		if terms[0] == 'Question:':
			if line in questions_list:
				questions_list[line] += 1
			else:
				questions_list[line] = 1

	f.close()

questions_list = dict(sorted(questions_list.items(), key=lambda item: -item[1]))
for q, val in questions_list.items():
	print(val, q)
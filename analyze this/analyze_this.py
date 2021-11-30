def convert(equation):

	operators = ['+', '-', '/', '*', '(', ')']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']

	fin_eq = ''

	i = 0

	while(i < len(equation)):
		curr_char = equation[i]
		if curr_char in operators:
			fin_eq += curr_char
			i += 1
		else:
			j = i
			while((j<len(equation)) and (equation[j] not in operators)):
				j += 1
			fin_eq += 'X'
			# print(i, j)
			i = j
		# else:
		# 	sad = 1
			# print("THE FUCK")
			# print(curr_char)

	return fin_eq

f = open("mathen_true.txt", "r")
lines = f.readlines()

correct_eq = 0
total_fail = 0

for i in range(int(len(lines)/5)):

	test_out = lines[5*i+1].split()[-1]
	target_out = lines[5*i+2].split()[-1]

	# print(test_out)
	# print(target_out)

	# print(test_out)

	correct_eq += (convert(test_out) == convert(target_out))
	total_fail += 1

	right_eq = (convert(test_out) == convert(target_out))

	if right_eq:
		print(lines[5*i])
		print(lines[5*i+1])
		print(lines[5*i+2])
		print(lines[5*i+3])
		print(lines[5*i+4])

# print(correct_eq)
# print(total_fail)
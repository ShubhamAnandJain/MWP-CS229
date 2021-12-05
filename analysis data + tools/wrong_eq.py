def convert(equation):
  operators = ['+', '-', '/', '*', '(', ')']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
  num_lst = []

  fin_eq = ''
  i = 0

  while(i < len(equation)):
    curr_char = equation[i]
    if curr_char in operators:
      fin_eq += curr_char
      i += 1
    else:
      j = i
      num_str = ''
      while((j<len(equation)) and (equation[j] not in operators)):
        num_str += equation[j]
        j += 1
      # num_lst.append(float(num_str))
      fin_eq += 'X'
      i = j
  return fin_eq, num_lst

def contains(list_words, bag_of_words):

  if list_words in bag_of_words:
    return True

  return False

  for word in list_words:
    if word not in bag_of_words:
      return False

  return True


f = open("mathen_false.txt", "r")
#f = open("/content/drive/MyDrive/perm_correct_graph2tree.txt", "r")

lines = f.readlines()
correct_eq = 0
total_fail = 0
correct_number_lst = 0
correct_num_and_structure = 0
how_many_more = 0
how_many = 0
four_variables = 0
three_variables = 0
two_variables = 0

for i in range(int(len(lines)/5)):
  test_out = lines[5*i+1].split()[-1]
  target_out = lines[5*i+2].split()[-1]

  fin_eq_test, num_lst_test = convert(test_out)
  fin_eq_target, num_lst_target = convert(target_out)
  
  correct_eq += (fin_eq_test== fin_eq_target)
  

  set_num_test = set(sorted(num_lst_test))
  set_num_target = set(sorted(num_lst_target))

  #print(set_num_test)
  #print(set_num_target)

  correct_number_lst += ((set_num_test <= set_num_target) or (set_num_test == set_num_target))

  correct_num_and_structure += ((fin_eq_test== fin_eq_target) and ((set_num_test <= set_num_target) or (set_num_test >= set_num_target) or (set_num_test == set_num_target)))
  #correct_num_and_structure += ((fin_eq_test== fin_eq_target) and ((set_num_test == set_num_target)))
  total_fail += 1

  right_eq = ((fin_eq_test== fin_eq_target) and ((set_num_test <= set_num_target) or (set_num_test == set_num_target)))

  if (fin_eq_target != fin_eq_test):
    print(lines[5 * i])
    print(lines[5 * i + 1])
    print(lines[5 * i + 2])

# print("Number of equations with two variables:", two_variables)
# print("Number of equations with three variables:", three_variables)
# print("Number of equations with four variables:", four_variables)
# print("Number of equations with How many:", how_many)
# print("Number of equations with How many more:", how_many_more)
# print("Number of equations with correct structure and correct list of numbers:", correct_num_and_structure )
# print("Number of equations with correct structure and incorrect list of numbers:", correct_eq)
# print("Number of failure cases in total:", total_fail)
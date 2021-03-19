str_command = input("Please type command a + b or a-b: ")
str_command.replace(' ','')

priority1 = tuple('^')
priority2 = tuple('*/')
priority3 = ('+', '-')
operation_priority = priority1 + priority2 + priority3
charts = tuple(map(str, range(10))) + tuple('.-')

str_A = ''
str_B = ''
variables = ['']
operations = []

for i, letter in enumerate(str_command):
	if letter in operation_priority and (i > 0) and variables[len(operations)] != '':
		operations.append(letter)
		variables.append('')
	else:
		index = len(operations)
		variables[index] = variables[index] + letter


variables = list(map(float, variables))
result = variables[0]

for i, operation in enumerate(operations):
	if type(result) == str:
		break

	var_A = result
	var_B = variables[i+1]

	if operation in '+-*/':
		if var_B == 0 and operation == '/':
			result = 'Inf'
		else:
			result = eval('{0}{1}{2}'.format(var_A, operation, var_B))
	elif operation == '^':
		result = var_A ** var_B
	else:
		result = "unknown"

print("Result: " + str(result))
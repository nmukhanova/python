str_command = input("Введите выражение:").replace(' ','')
str_command = list(str_command)

supported_ops = ('+-*/^sqrt')
ops = {'+':2, '-':2, '/':1, '*':1, '^':0, 'sqrt':0}

variables = ['']
operations = []
stack = []
stroka = []
output = []
result = ''
itog = []


for i, letter in enumerate(str_command):
	if letter in '+-/*^' and (i>0) and variables[len(operations)] != '':
		operations.append(letter)
		variables.append('')
	else:
		index = len(operations)
		variables[index] = variables[index] + letter

#разделение выражения на отдельные элементы
for i in range(max(len(variables), len(operations))):
	if i < len(variables):
		stroka.append(variables[i])
	if i < len(operations):
		stroka.append(operations[i])


#отрицательные числа
for i, letter in enumerate(stroka):
	if '-' in str(letter) and ('1' in str(letter) or '2' in str(letter) or '3' in str(letter) or '4' in str(letter) or '5' in str(letter) or '6' in str(letter) or '7' in str(letter) or '8' in str(letter) or '9' in str(letter)):
		stroka[i] = str('(0' + stroka[i] + ')')	

#sin
for i, letter in enumerate(stroka):
	if 'sin' in str(letter) and ('1' in str(letter) or '2' in str(letter) or '3' in str(letter) or '4' in str(letter) or '5' in str(letter) or '6' in str(letter) or '7' in str(letter) or '8' in str(letter) or '9' in str(letter)):
		stroka[i] = str(math.sin((float(stroka[i].split('sin')).pop())))

#cos
for i, letter in enumerate(stroka):
	if 'cos' in str(letter) and ('1' in str(letter) or '2' in str(letter) or '3' in str(letter) or '4' in str(letter) or '5' in str(letter) or '6' in str(letter) or '7' in str(letter) or '8' in str(letter) or '9' in str(letter)):
		stroka[i] = str(math.cos((float(stroka[i].split('cos')).pop())))

#sqrt
for i, letter in enumerate(stroka):
	if 'sqrt' in str(letter) and ('1' in str(letter) or '2' in str(letter) or '3' in str(letter) or '4' in str(letter) or '5' in str(letter) or '6' in str(letter) or '7' in str(letter) or '8' in str(letter) or '9' in str(letter)):
		stroka[i] = str('(' + stroka[i] + '^0.5)')

#обратная польская запись (вот тут не до конца разобралась, каюсь)
str_command = ''.join(stroka)
for i in str_command:
	if i in '0123456789.':
		if len(output) == 0:
			output = [i] + output
		else:
			if output[0][-1] in '0123456789.' and digit: output[0] += i
			else:
				output = [i] + output
		digit = True
	else: digit = False

	if i == '(':
		stack = [i] + stack

	if i == ')':
		while stack != [] and stack[0] != '(': output, stack = [stack[0]] + output, stack[1:]
		if stack != [] and stack[0] == '(': stack = stack[1:]

	if i in ops:
		while stack != [] and stack[0] in ops and ops[i] >= ops[stack[0]]: output, stack = [stack[0]] + output, stack[1:]
		stack = [i] + stack

while stack != []: output, stack = [stack[0]] + output, stack[1:]


for i, letter in enumerate(output):
	if '^' in str(letter) and '^' in str(output[i+2]):
		output[i+1], output[i+2] = output[i+2], output[i+1]

output = ''.join(reversed(output))

#итог
for i, letter in enumerate(output.split()):
	if '.' in letter or '0' in letter or '1' in letter or '2' in letter or '3' in letter or '4' in letter or '5' in letter or '6' in letter or '7' in letter or '8' in letter or '9' in letter:
		itog.append(letter)
	elif letter == '^':
		chislo1 = float(itog.pop())
		chislo2 = float(itog.pop())
		itog.append(chislo1**chislo2)
	elif letter == 'sqrt':
		chislo2 = float(itog.pop())
		itog.append(chislo2**0.5)	
	elif letter == '*':
		chislo1 = float(itog.pop())
		chislo2 = float(itog.pop())
	elif letter == '/':
		chislo1 = float(itog.pop())
		chislo2 = float(itog.pop())
		if chislo2 == 0:
			result = 'Inf'
			break
		else:
			itog.append(chislo1/chislo2)
	elif letter == '+':
		chislo1 = float(itog.pop())
		chislo2 = float(itog.pop())
		itog.append(chislo1+chislo2)
	elif letter == '-':
		chislo1 = float(itog.pop())
		chislo2 = float(itog.pop())
		itog.append(chislo1-chislo2)
	else:
		print('Ответ')

if result == 'Inf':
	print('Попробуйте ещё раз')
else:
	print('result:' + str(itog[0]))





s = 'Муханова Наталия Алексеевна'
i = 13

#Задание 1
fio = []
print('№1 ' + str(fio == []))

#Задание 2
i = 0
x = 0
fio.append ([])
while i != len(s):
	if s[i] == ' ':
		fio.append([])
		i += 1
		x += 1
	else:
		fio[x].append(s[i])
		i += 1
print('№2 ' + str(fio == [['М', 'у', 'х', 'а', 'н', 'о', 'в', 'а'], ['Н', 'а', 'т', 'а', 'л', 'и', 'я'], ['А', 'л', 'е', 'к', 'с', 'е', 'е', 'в', 'н', 'а']]))

#Задание 3
x = 0
while x < len(fio):
    fio[x] = list(reversed(fio[x]))
    x += 1
print('№3 ' + str(fio == [['а', 'в', 'о', 'н', 'а', 'х', 'у', 'М'], ['я', 'и', 'л', 'а', 'т', 'а', 'Н'], ['а', 'н', 'в', 'е', 'е', 'с', 'к', 'е', 'л', 'А']]))

#Задание 4
char = fio[1][3]
print('№4 ' + str(char == 'а'))

#Задание 5
char = fio[1][3]
print('№5 ' + str(char == 'а'))

#Задание 6
fio_len = [len(fio[0]), len(fio[1]), len(fio[2])]
print('№6 ' + str(fio_len == [8, 7, 10]))

#Задание 7
min_len = min(fio_len)
print('№7 ' + str(min_len == 7))

#Задание 8
i = 0
chars = str()
while i < min_len:
	for x in range(len(fio)):
		chars += fio[x][i]
	i += 1
print('№8 ' + str(chars == 'аяавинолвнаеатехасуНк'))

#Задание 9
reversed_fio_dict = {
    'фамилия': fio[0],
    'имя': fio[1],
    'отчество': fio[2],
}
print('№9 ' + str(reversed_fio_dict == {'фамилия': ['а', 'в', 'о', 'н', 'а', 'х', 'у', 'М'], 'имя': ['я', 'и', 'л', 'а', 'т', 'а', 'Н'], 'отчество': ['а', 'н', 'в', 'е', 'е', 'с', 'к', 'е', 'л', 'А']}))

#Задание 10
reversed_fio_dict_keys = list(reversed_fio_dict.keys())
print('№10 ' + str(reversed_fio_dict_keys == ['фамилия', 'имя', 'отчество']))

#Задание 11
reversed_fio_dict_values = list(reversed_fio_dict.values())
print('№11 ' + str(reversed_fio_dict_values == [['а', 'в', 'о', 'н', 'а', 'х', 'у', 'М'], ['я', 'и', 'л', 'а', 'т', 'а', 'Н'], ['а', 'н', 'в', 'е', 'е', 'с', 'к', 'е', 'л', 'А']]))

#Задание 12
reversed_fio_dict_items = list(reversed_fio_dict.items())
print('№12 ' + str(reversed_fio_dict_items == [('фамилия', ['а', 'в', 'о', 'н', 'а', 'х', 'у', 'М']), ('имя', ['я', 'и', 'л', 'а', 'т', 'а', 'Н']), ('отчество', ['а', 'н', 'в', 'е', 'е', 'с', 'к', 'е', 'л', 'А'])]))

#Задание 13
res = reversed_fio_dict['фамилия']
print('№13 ' + str(res == ['а', 'в', 'о', 'н', 'а', 'х', 'у', 'М']))

#Задание 14
chars = {}
print('№14 ' + str(chars == {}))

#Задание 15
s = s.replace(' ', '').lower()
print('№15 ' + str(s == 'муханованаталияалексеевна'))

#Задание 16
res = {}
for i in s:
    res[i] = s.count(i)
res = list(res.items())
print('№16 ' + str(res == [('м', 1), ('у', 1), ('х', 1), ('а', 6), ('н', 3), ('о', 1), ('в', 2), ('т', 1), ('л', 2), ('и', 1), ('я', 1), ('е', 3), ('к', 1), ('с', 1)]))


#Задание 17
char1 = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
def nataliaCharToIndex(char: str) -> int:
	letter = char.lower()
	return char1.find(letter)+1
print('№17 ' + str(nataliaCharToIndex("Т") == 20))

#Задание 18
for i in range(len(fio)):
	y = 0
	s = []
	while y < len(fio[i]):
		s.append(nataliaCharToIndex(fio[i][y]))
		y += 1
	fio[i] = s
print('№18 ' + str(fio == [[1, 3, 16, 15, 1, 23, 21, 14], [33, 10, 13, 1, 20, 1, 15], [1, 15, 3, 6, 6, 19, 12, 6, 13, 1]]))


""" +++ КОНЕЦ =) +++ """

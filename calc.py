#simple div
str_input = input("A: ")

A = int(str_input)
#print(type(A))


operation = raw_input ("+ / * - ^ : ") 

str_input2 = input("B: ")
B = int(str_input2)
#print(type(B))
result = None

if operation == '/':
    result = A / B
#print(type(result))
elif operation == '+':
	result= A + B
elif operation == '-':
	result = A - B
elif operation == '*':
	result = A * B
elif operation == '^':
	result = A ** B

else: 
	result = "unknown"
#print(type(result))

print("Result: " + str(result))


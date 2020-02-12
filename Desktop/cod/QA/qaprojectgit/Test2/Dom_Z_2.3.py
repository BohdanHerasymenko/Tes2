print("Введите год:")
y = int(input())
x = y/4 - y//4
z = y/100 - y//100
v = y/400-y//400
if x == 0 and z > 0 or  v == 0:
    print("Yes")
else:
    print('No')
# Дано три числа. Упорядочите их в порядке возрастания.
# Программа должна считывать три числа a, b, c, за
# тем программа должна менять их значения так,
# чтобы стали выполнены условия a <= b <= c, затем программа выводит тройку a, b, c.
print("Введите числа:")
a = int(input())
b = int(input())
c = int(input())
if a > b:
    a, b = b, a
if b > c and a > c:
    a, b, c = c, a, b
elif b > c >= a:
    b, c = c, b
print(a, b, c)

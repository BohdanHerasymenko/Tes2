print("Введите строку (проверка на то, является ли строка записью числа):")
s = input()
print("Является ли строка записью числа:", s.isdigit())
print("Введите строку (проверка на количество пробелов и точек):")
m = input()
k = m.replace(" ", "")
n = m.replace(".", "")
print("Количество пробелов:", str(len(m)-len(k))+".", "Количество точек:", str(len(m)-len(n))+".")
l = "homework"
l = " "*48+l+" "*48
print("Начало строки"+l+"Конец строки")
print("Введите строку (хоть одно слово должно быть написано с маленькой буквы)")
a = input()
print(a.title())

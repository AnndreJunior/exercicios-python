a = float(input("Informe um número: "))
b = float(input("Informe outro número: "))
c = float(input("Informe mais um número: "))

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)

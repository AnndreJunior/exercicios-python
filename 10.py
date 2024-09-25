a = float(input("Informe o valor do primeiro lado do triângulo: "))
b = float(input("Informe o valor do segundo lado do triâangulo: "))
c = float(input("Informe o valor do terceiro lado do triângulo: "))

if a == b == c:
    print("Equilátero")
elif a == b or a == c or b == c:
    print("Isósceles")
else:
    print("Escaleno")

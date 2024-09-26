a = int(input("Informe o ângulo a: "))
b = int(input("Informe o ângulo b: "))
c = int(input("Informe o ângulo a: "))

if a == 90 or b == 90 or c == 90:
    print("Triângulo retângulo")
elif a > 90 or b > 90 or c > 90:
    print("Triângulo obtusângulo")
else:
    print("Triângulo acutângulo")

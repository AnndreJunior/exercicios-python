import math

quantidade_lados = int(input("Quantos lados seu polígono regular tem?\nQuantidade: "))
a = 0
b = 0
c = 0
area = 0

if quantidade_lados < 3:
    print("Não é um polígono")
elif quantidade_lados > 5:
    print("Polígono não identificado")
else:
    print("Informe o tamanho dos os lados do seu polígono em centímetros.")

    a = float(input("Primeiro lado: "))
    b = float(input("Segundo lado: "))
    c = float(input("Terceiro lado: "))
    if quantidade_lados == 3:
        p = (a + b + c) / 2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("Triângulo")
        print(f"Área: {area}")
    elif quantidade_lados == 4:
        d = float(input("Quarto lado: "))
        if a == b == c == d:
            area = a**2
        elif a == c and b == d:
            area = a * b
        print("Quadrilátero")
        print(f"Área: {area}")
    elif quantidade_lados == 5:
        d = float(input("Quarto lado: "))
        e = float(input("Quinto lado: "))
        area = 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * a**2
        print("Pentágono")
        print(f"Área: {area:.2f}")

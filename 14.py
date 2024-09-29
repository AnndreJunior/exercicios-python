a = float(input("Infome um número: "))
b = float(input("Infome outro número: "))
c = float(input("Infome mais um número: "))
d = float(input("Já pedi um número?\nNúmero: "))
e = float(input("Por favor, diga um número: "))
maior_numero = 0
menor_numero = 0

if a > b and a > c and a > d and a > e:
    maior_numero = a
    if b < c and b < d and b < e:
        menor_numero = b
    elif c < b and c < d and c < e:
        menor_numero = c
    elif d < b and d < c and d < e:
        menor_numero = d
    else:
        menor_numero = e
elif b > a and b > c and b > d and b > e:
    maior_numero = b
    if a < c and a < d and a < e:
        menor_numero = a
    elif c < a and c < d and c < e:
        menor_numero = c
    elif d < a and d < c and d < e:
        menor_numero = d
    else:
        menor_numero = e
elif c > a and c > b and c > d and c > e:
    maior_numero = c
    if a < b and a < d and a < e:
        menor_numero = a
    elif b < a and b < d and b < e:
        menor_numero = b
    elif d < a and d < b and d < e:
        menor_numero = d
    else:
        menor_numero = e
elif d > a and d > b and d > c and d > e:
    maior_numero = d
    if a < b and a < c and a < e:
        menor_numero = a
    elif b < a and b < c and b < e:
        menor_numero = b
    elif c < a and c < b and c < e:
        menor_numero = c
    else:
        menor_numero = e
else:
    maior_numero = e
    if a < b and a < c and a < d:
        menor_numero = a
    elif b < a and b < c and b < d:
        menor_numero = b
    elif c < a and c < b and c < d:
        menor_numero = c
    else:
        menor_numero = d

print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")

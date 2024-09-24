a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))

first = 0
second = 0
last = 0

if a < b and a < c:
    first = a
    if b < c:
        second = b
        last = c
    else:
        second = c
        last = b
elif b < a and b < c:
    first = b
    if a < c:
        second = a
        last = c
    else:
        second = c
        last = a
else:
    first = c
    if b < a:
        second = b
        last = a
    else:
        second = a
        last = b

print(f'{first}, {second}, {last}')
n1 = float(input("Informe a primeira nota do aluno: "))
n2 = float(input("Informe a segunda nota do aluno: "))
n3 = float(input("Informe a terceira nota do aluno: "))
n4 = float(input("Informe a quarta nota do aluno: "))

soma_das_quatro_notas = n1 + n2 + n3 + n4

md1 = soma_das_quatro_notas / 4

if md1 >= 7:
    print(f"Aprovado com média {md1:.1f}")
else:
    ne = float(input("Informe a nota de exame: "))
    soma_das_quatro_notas += ne
    md2 = soma_das_quatro_notas / 5
    if md2 >= 5:
        print(f"Aprovado em exame com média {md2:.1f}")
    else:
        print(f"Reprovado com média {md2:.1f}")

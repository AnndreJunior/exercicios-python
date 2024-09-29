y = float(input("Digite a quantia que você possue na conta, Mr. Datan: "))

if y > 0 and y >= 2000:
    x = float(input("Qual a quantia que você quer sacar?\nQuantia: "))
    if x % 5 == 0:
        if x > 0 and x <= 2000:
            y -= x + 0.50
            print(f"Você sacou R${x:.2f}")
            print(f"Seu salto atual é de R${y:.2f}")
        else:
            print("Valor do saque está fora do limite de R$2000.00")
    else:
        print("Erro ao tentar sacar")
else:
    print("Saldo inválido")

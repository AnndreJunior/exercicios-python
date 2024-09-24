print("Informe seu sexo.")
print("1. Feminino")
print("2. Masculino")

opcao = int(input("Opção: "))

altura = float(input("Informe sua altura(em metros): "))

peso_ideal = 0

if opcao == 1:
    peso_ideal = 72.7 * altura - 58
else:
    peso_ideal = 62.1 * altura - 44.7

print(f"Seu peso ideal é: {peso_ideal:.2f}")

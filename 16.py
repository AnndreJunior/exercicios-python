salario_bruto = float(input("Informe seu salário bruto: "))
imposto_sindical_porcentagem = 0.03


def porcentagem_do_inss(salario_bruto: float) -> float:
    if salario_bruto <= 1412:
        return 0.075
    if salario_bruto <= 2666.68:
        return 0.09
    if salario_bruto <= 4000.03:
        return 0.12
    return 0.14


def porcentagem_do_imposto_de_renda(salario_bruto: float):
    if salario_bruto <= 2112:
        return 0
    if salario_bruto <= 2826.65:
        return 0.075
    if salario_bruto <= 3751.05:
        return 0.15
    if salario_bruto <= 4664.68:
        return 0.225
    return 0.275


taxa_inss = salario_bruto * porcentagem_do_inss(salario_bruto)
taxa_imposto_de_renda = salario_bruto * porcentagem_do_imposto_de_renda(salario_bruto)
salario_liquido = salario_bruto - taxa_inss - taxa_imposto_de_renda

option = input("Deseja incluir o imposto sindical? [s/n]").lower()
if option == "s":
    imposto_sindical = salario_bruto * imposto_sindical_porcentagem
    salario_liquido -= imposto_sindical

print(f"Salário líquido: R${salario_liquido:.2f}")

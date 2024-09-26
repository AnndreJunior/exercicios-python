dias = int(input("Quantos dias você atrasou?\nDias: "))
taxa = 0

if dias <= 5:
    taxa = 2
elif dias >= 6 and dias <= 10:
    taxa = 3
elif dias >= 11 and dias <= 15:
    taxa = 4
else:
    taxa = 6

print(f"Você pagará R${taxa:.2f}")

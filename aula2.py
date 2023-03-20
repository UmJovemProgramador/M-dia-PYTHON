nota1 = float(input("Digite a 1º nota: "))
nota2 = float(input("Digite a 2º nota: "))
nota3 = float(input("Digite a 2º nota: "))

media = (nota1+nota2+nota3) / 3

if  media >=0 and media < 5:
    print(f"Reprovado com a média {media:.2f} seu conceito é INSUFICIENTE")

elif media >= 5 and media < 7:

    print(f"Aprovado com a média {media:.2f} seu conceito é REGULAR")

elif media >= 7 and media < 9:

    print(f"Aprovado com a média {media:.2f} seu conceito é BOM")

elif media >= 9 and media <= 10:

    print(f"Aprovado com a média {media:.2f} seu conceito é EXCELENTE")

else:

    print("Média inválida")

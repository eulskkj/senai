import os
os.system("clear")

primeira_nota = float(input("Digite sua primeira nota: "))
segunda_nota = float(input("Digite sua segunda nota: "))
media = primeira_nota + segunda_nota / 2


if media > 9 == 9:
    resultado = ("A")
elif media > 7.5 < 9:
    resultado = ("B")
elif media >6 < 7.5:
    resultado = ("C")
elif media > 4 < 6:
    resultado = ("D")
elif media < 4:
    resultado = ("E")
print(f"Primeira nota: {primeira_nota} ")
print(f"Segunda nota: {segunda_nota} ")
print(f"Média: {media} ")
print(f"Resultado: {resultado}")    






















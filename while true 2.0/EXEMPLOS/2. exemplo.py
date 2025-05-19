import os
os.system (" cls || clear")

contador = 0
continua = 's'

while continua == 's':
    # comandos a seres repitidos
    print("Repentindo...")

    continua = input("Tecle 's' se deseja continuar: ").strip().lower()

    contador += 1

if contador == 0:
    print("O bloco NÃO foi repetido.")
else:
    print (f"O bloco foi repetido {contador} vezes")








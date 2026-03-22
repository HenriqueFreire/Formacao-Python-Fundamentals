numero = -1

while numero % 2 == 0:
    numero = int(input("Informe um número:"))

    if numero == 10:
        break

    print(numero)

else:
    print("Saiu do loop")

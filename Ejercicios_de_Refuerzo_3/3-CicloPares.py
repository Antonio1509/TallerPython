# crea un ciclo en el que me muestre los numeros pares desde 0 hasta un valor ingresado por teclado

limite = int(input("Ingresa un número: "))

for i in range(0, limite + 1, 2):
    print(i)
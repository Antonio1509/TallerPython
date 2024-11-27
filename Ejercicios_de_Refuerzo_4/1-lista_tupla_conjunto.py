# crea una lista, una tupla y un conjunto e intenta acceder a sus datos

mi_lista = [10, 20, 30]
mi_tupla = (40, 50, 60)
mi_conjunto = {70, 80, 90}

print("Lista, primer elemento:", mi_lista[0])  # Acceso válido
print("Tupla, segundo elemento:", mi_tupla[1])  # Acceso válido

print("Conjunto completo:", mi_conjunto)

for elemento in mi_conjunto:
    print("Elemento del conjunto:", elemento)
# Ejercicio 1: Crear una lista con los números del 1 al 100 que sean múltiplos de 4

num_mult_4 = list(range(4, 101, 4))
print("Ejercicio 1:", num_mult_4)

# Ejercicio 2: Crear lista con cinco elementos y mostrar el penúltimo

mis_elementos = ["libro", "computadora", "café", "música", "python"]
penultimo = mis_elementos[-2]
print("Ejercicio 2:", penultimo)

# Ejercicio 3: Crear lista vacía, agregar 3 palabras con append
lista_vacia = []
lista_vacia.append("hola")
lista_vacia.append("mundo")
lista_vacia.append("python")
print("Ejercicio 3:", lista_vacia)

# Ejercicio 4: Reemplazar segundo y último valor de la lista animales
animales = ["perro", "gato", "conejo", "pez"]
print("Ejercicio 4: Lista original", animales)
animales[1] = "loro"    
animales[-1] = "oso"    
print("             Lista actualizada:", animales)

# Ejercicio 5: Analizar el programa dado
# El programa hace lo siguiente:

# 1. Crea una lista llamada numeros con los valores [8, 15, 3, 22, 7]
numeros = [8, 15, 3, 22, 7]

# 2. Encuentra el valor máximo de la lista con max(numeros), en este caso 22
# 3. Elimina ese valor máximo de la lista con remove()
numeros.remove(max(numeros))

# 4. Imprime la lista modificada
print("Ejercicio 5:", numeros)

# Ejercicio 6: Crea una lista con numeros del 10 al 30 (incluido) con saltos de 5 
# y mostrar dos primeros

numeros_saltos = list(range(10, 31, 5))
#se realiza Slicing para obtener primeros dos elementos
dos_primeros = numeros_saltos[:2]
#se imprime la lista con los 2 primeros numeros
print("Ejercicio 6:", dos_primeros)

# Ejercicio 7: Reemplazar dos valores centrales de lista autos
autos = ["sedan", "polo", "suran", "gol"]

# Reemplaza "polo" (índice 1)
autos[1] = "ford"

# Reemplaza "suran" (índice 2)
autos[2] = "chevrolet"
print("Ejercicio 7:", autos)

# Ejercicio 8: Crear lista vacía llamada "dobles" y agregar dobles de 5, 10, 15 con append
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("Ejercicio 8:", dobles)

# Ejercicio 9> Dada  la  lista  “compras”,  cuyos  elementos  
# representan  los  productos  comprados  por diferentes clientes

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
print("Ejercicio 9: Lista compras original:", compras)

# a) Agregar "jugo" al tercer cliente (índice 2)
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# Buscamos el índice de "fideos"
indice_fideos = compras[1].index("fideos") 

# Reemplazamos el valor
compras[1][indice_fideos] = "tallarines"   

# c) Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan")

# d) Imprimir la lista resultante por pantalla

print("             Lista compras modificada> ", compras)

# Ejercicio 10: Crear lista anidada con estructura específica
lista_anidada = [
    15,                      # Posicion lista_anidada[0]
    True,                    # Posicion lista_anidada[1]
    [25.5, 57.9, 30.6],      # Posicion lista_anidada[2] lista dentro de lista
    False                    # Posicion lista_anidada[3]
]
print("Ejercicio 10:", lista_anidada)
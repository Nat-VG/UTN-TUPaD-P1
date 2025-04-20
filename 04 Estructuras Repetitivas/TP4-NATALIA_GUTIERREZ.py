print("1 Programa que imprime en pantalla todos los números enteros desde 0 hasta 100, uno por linea")

range(101) #porque va de 0 a 100
for numero in range(101):  
   print(numero)




print("2- Programa que pide al usuario un número entero y muestra la cantidad de dígitos que contiene.")

# # Se pide número al usuario
numero = input("Ingrese un número entero y yo calculare la cantidad de dígitos que contiene: ")
#Usamos len para determinar su longitud
cant_digitos = len(numero)
print(f"El número {numero} tiene {cant_digitos} dígitos.")



print("3- Programa que suma numeros comprendido entre dos valores excluyendo esos dos valores")

# #Se pide número inicial al usuario

numero_ini = int(input("Ingrese el primer número: "))
numero_fin = int(input("Ingrese el ultimo número: "))
if numero_ini > numero_fin:
   numero_ini, numero_fin = numero_fin, numero_ini

# Calculamos la suma usando un bucle
suma = 0
for numero in range(numero_ini + 1, numero_fin):
   suma += numero
print(f"La suma de los números entre {numero_ini} y {numero_fin}, excluyéndolos, es: {suma}")



print("4-Elabora un programa que permita al usuario ingresar números enteros y los sume en....")
# #secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0

suma = 0
print ("Programa que suma numeros enteros ingresados por el usuario - Ingrese 0 para terminar")

numero = int(input("Ingrese un número entero: ")) # Se pide número al usuario

while numero != 0:
   suma = suma + numero
   numero = int(input("Ingrese  otro número entero: ")) #Se repite el pedido 

print (f"La suma total de los numeros ingresados es", suma)




print("5- Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final....")
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número

import random
num_toguess = random.randint(0,9) # Se genera el numero a adivinar
acu_intento = 0 #llevara la cuenta de los intentos realizados

numero = int(input("Hola! Jugamos? Estoy pensando un número entre 0 y 9, Cuál sera?: "))

while numero != num_toguess: #verificamos que el numero no sea igual al adivinado

   numero = int(input("Fallaste!, Ingresa otro número: "))
   acu_intento += 1 #acumulamos la cantidad de intentos

print (f"Correcto! Ese es el número!, lo acertaste en el intento número {acu_intento+1}") #muestra en pantalla la cantidad de intentos en le que se acerto




print("6 Programa que imprime en pantalla todos los números pares entre 0 y 100 ordenados en forma descendente")

for numero in range(100,-1,-1):  #range va de 100 a 0 con paso decreciente en -1
   print(numero)





print(" 7- Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario")

suma = 0
numero = int(input("Ingrese un número para realizar la sumatoria desde 0 hasta el numero ingresado: "))
if numero >= 0:
   for i in range(numero+1): #Iteramos desde el cero al numero ingresado incluido
       suma += i
        
   print (f"La suma total de los numeros ingresados es", suma)
else:
   print ("Por favor ingrese un numero positivo")





print("8 - Contar pares, impares...")
cant_num = 10 #Se puso diez para realizar prueba
contpar = 0
contimpar = 0
contneg = 0
contpos = 0

print(f"Ingresa {cant_num} números enteros: ")

for i in range (cant_num):
   numero = int(input(f"Número {i + 1}: "))  # Solicitar cada número
   if numero > 0:
       contpos += 1
   elif numero < 0:
       contneg += 1

   if numero % 2 == 0:
       contpar += 1
   else:
       contimpar += 1

# Mostrar los resultados
print(f"\nResultados:")
print(f"Cantidad de números pares: {contpar}")
print(f"Cantidad de números impares: {contimpar}")
print(f"Cantidad de números positivos: {contpos}")
print(f"Cantidad de números negativos: {contneg}")




print("9- Suma de numeros")
cantidad = 5  # Permite cambiar para probar
suma = 0

print(f"Ingrese {cantidad} números enteros:")
for i in range(cantidad): #el for suma hasta que se ingrese la cantidad establecia en la variable
    num = int(input(f"Número {i + 1}: "))
    suma += num

media = suma / cantidad #Se calcula la media y abajo muestra el resultado
print(f"La media de los {cantidad} números es: {media:.2f}")





print("10- Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario")

# Pedimos al usuario un número entero positivo
numero = int(input("Ingresa un número entero positivo: "))

# Se Crea una variable para guardar el número invertido
numero_invertido = 0

# Invertimos el número usando divisiones y multiplicaciones
while numero > 0:
    # Obtener el último dígito del número
    ultimo_digito = numero % 10
    
    # Agregar el último dígito al número invertido
    numero_invertido = (numero_invertido * 10) + ultimo_digito
    
    # Quitar el último dígito del número original
    numero = numero // 10

# /Se muestra el resultado
print("El número invertido es:", numero_invertido)
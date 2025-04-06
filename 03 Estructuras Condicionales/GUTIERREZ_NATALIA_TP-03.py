#1-Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 

#Se solicita el ingreso de su edad al usuario
edad=int(input("Señor usuario, ingrese su Edad:"))
#se evalua si es mayor de edad
if edad >= 18:
   print("Es mayor de edad")

#2-Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
#((mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
#mensaje “Desaprobado”. 

#Se solicita el ingreso de la nota al usuario
nota=float(input("Ingrese su nota:"))

#Se evalua si fue aprobado con un valor mayor o igual a 6
if nota >= 6:
    print("Usted está aprobado")
else:
    print("Lamentablemente ha desaprobado")

# 3-Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
#operador de módulo (%) en Python para evaluar si un número es par o impar

#Solicitamos al usuario el ingreso del numero 
numero=int(input("Ingrese un numero par: "))

#Se evalua de acuerdo al modulo
if numero % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print ("Por favor ingrese un numero par")

# 4-Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
#siguientes categorías pertenece: Niño/a: menor de 12 años.Adolescente: mayor o igual que 12 años y menor que 18 años. 
# Adulto/a joven: mayor o igual que 18 años y menor que 30 años. Adulto/a: mayor o igual que 30 años

#Solicitamos al usuario el ingreso de su edad 
edad=int(input("Ingrese su edad: "))

#Se evalua la edad
if edad < 12:
    print("Sos un niño/a")
elif edad < 18: 
    print("Sos un adolescente")
else:
    print ("Usted es una persona adulta")

#5-Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
#como una lista o un string. 

#Solicitamos al usuario el ingreso de la contraseña
pasw = input("Ingrese una contraseña (debe tener entre 8 y 14 caracteres):")

#verificamos que cumpla las condiciones
if 8 <= len(pasw) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")    

#6-Calculo de moda, mediana y media a partir de numeros aleatorios

#Importamos las librerias a utilizar
from statistics import mode, median, mean
import random

# Generamos la lista de 50 números aleatorios entre 1 y 100
num_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calculamos moda, mediana y media
moda = mode(num_aleatorios)
mediana = median(num_aleatorios)
media = mean(num_aleatorios)

# Determinamos el tipo de sesgo
if media > mediana and mediana > moda:
    sesgo = "Sesgo positivo o a la derecha"
elif media < mediana and mediana < moda:
    sesgo = "Sesgo negativo o a la izquierda"
else:
    sesgo = "Sin sesgo (distribución simétrica)"

# Impresion de resultados
print(f"Lista generada: {num_aleatorios}")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
#Imprimimos la media con formado de 2 decimales
print(f"Media: {media:.2f}")
print(f"\nResultado: {sesgo}")

#7-Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

#Se pide ingreso de palabra o frase al usuario
palabra = input("Ingrese una frase o palabra:")

#Se definen las vocales
vocales = ('a','e','i','o', 'u', 'A','E','I','O','U')

#Verificamos la ultima letra del texto ingresado, si no se ingresa nada no emite error
if palabra[-1:] in vocales:
    print("palabra"+"!")
else:
    print (palabra)

#8-Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee

nombre=input("Ingrese su nombre:")
opcion=input("1- Para ver su nombre en MAYUSCULAS, 2- Para ver su nombre en minúsculas, 3- Para ver su nombre con la Primera letra en Mayúsculas: ")

# Trabajamos de acuerdo a la opción
if opcion == '1':
# Convertir a mayúsculas
    resultado = nombre.upper() 
elif opcion == '2':
# Convertir a minúsculas
    resultado = nombre.lower()  
elif opcion == '3':
# Primera letra mayúscula
    resultado = nombre.title()  
else:
    resultado = "Opción no válida. No se modificó el nombre."

# Imprimir el resultado
print("Resultado:", resultado)


#9- Escribir un programa que pida al usuario la magnitud de un terremoto...

#Pedimos al usuario que ingrese la magnitud del terremoto en una variable float

intensidad_sismo = float(input("Ingrese la magnitud del sismo en la escala de Richter: "))

if intensidad_sismo < 3:
    clasificacion = "Sismo Muy leve (imperceptible)"
elif 3 <= intensidad_sismo < 4:
    clasificacion = "Sismo leve (ligeramente perceptible)"
elif 4 <= intensidad_sismo < 5:
    clasificacion = "Sismo moderado (sentido por personas, sin daños)"
elif 5 <= intensidad_sismo < 6:
    clasificacion = "Sismo fuerte (daños en estructuras débiles)"
elif 6 <= intensidad_sismo < 7:
    clasificacion = "Sismo muy fuerte (daños significativos)"
else:
    clasificacion = "Gran terremoto (daños graves a gran escala)"

print(f"Para una magnitud de {intensidad_sismo}, el sismo se clasifica como: {clasificacion}")

#10- Utilizando la información aportada en la siguiente tabla sobre las estaciones del año...

#Solicitamos al usuario que ingrese en que hemisferio se encuentra
hemisferio = input("Ingrese el hemisferio en el que se encuentra(N para Norte o S para Sur): ").upper()

#Solicitamos que ingrese el mes y el año en el que se encuentra
mes = int(input("Ingrese el mes en el que se encuentra (1-12): "))
dia = int(input("Ingrese el dia en el que se encuentra: (1-31):"))

#Realizamos los calculos de acuerdo a la tabla y establecemos las estaciones para el Hemisferio Norte

if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
    estacion_N = "Invierno"
elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
    estacion_N = "Primavera"
 
elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
    estacion_N = "Verano"
else:
    estacion_N = "Otoño"

#Verificamos en que Hemisferio se encuentra el usuario y si es el SUR cambiamos por las estaciones opuestas

if hemisferio == "N":
    estacion = estacion_N
    hemisferio = "Norte"
elif estacion_N == "Invierno":
    estacion = "Verano"
    hemisferio = "Sur"
elif estacion_N == "Verano":
    estacion = "Invierno"
    hemisferio = "Sur"
elif estacion_N == "Otoño":
    estacion = "Primavera"
    hemisferio = "Sur"
elif estacion_N == "Primavera":
    estacion = "Otoño"
    hemisferio = "Sur"

print(f"\n Usted se encuentra en el Hemisferio {hemisferio} en la estación {estacion}" )

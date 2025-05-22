#  1 - Funcion que imprime mensaje "Hola Mundo"
def imprimir_hola_mundo():
    print ("Hola Mundo!")
# ---------------------------------------------
# 2 - Funcion saludo personalizado
def saludar_usuario(nombre):
    return (f"Hola {nombre}!")
# ---------------------------------------------
# 3 - Funcion informacion_personal
def informacion_personal(nombre,apellido,edad,residencia):
    print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")    
# ---------------------------------------------
# 4 - Calculo de area y radio
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio
# ---------------------------------------------
# 5 - Convertir segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600
# ---------------------------------------------
# 6 - Tabla de multiplicar
def tabla_multiplicar(numero):
    for i in range (1,11):
        print (f"{numero} x {i} = {numero * i}")

# ---------------------------------------------
# 7 - Operaciones basicas
def operaciones_basicas(a,  b):
   
    suma = a + b
    resta = a - b
    producto = a * b
    division = a / b
    return (suma,resta,producto,division) #devuelve la tupla solicitada

# ---------------------------------------------
# 8 - Calculo de IMC
def calcular_imc(peso, altura):
    return (peso / (altura ** 2))

# ---------------------------------------------
# 9 - Convertir Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# ---------------------------------------------
# 10 - Calcular promedio de 3 numeros
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# **********PROGRAMA PRINCIPAL**************
import math
# PUNTO 1
print ("------------------------------- 1")
imprimir_hola_mundo()
# PUNTO 2
print ("-------------------------------2")
nombre = input("Ingrese su nombre:")
print (saludar_usuario(nombre))
# PUNTO 3
print ("-------------------------------3")
nombre = input("Ingresa tu nombre:")
apellido = input("Ingresa tu apellido: ")
edad = int(input("Ingresa tu edad: "))
residencia = input("Ingresa tu lugar de residencia: ")
informacion_personal(nombre, apellido, edad,residencia)
#  PUNTO 4
print ("-------------------------------4")
radio = float(input("Vamos a calcular el area y el perimetro de un ciculo, ingrese el radio: "))
print (f"El area del ciculo es:{calcular_area_circulo(radio):.2f}")
print (f"El perimetro del circulo es:{calcular_perimetro_circulo(radio):.2f}")
#  PUNTO 5
print ("-------------------------------5")
segundos = int(input("Ingrese los segundos para calcular su equivalente en horas:"))
print (f"{segundos} equivalen a {segundos_a_horas(segundos):.2f} horas")
#  PUNTO 6
print ("-------------------------------6")       
numero = int(input("Ingrese un numero y mostrare su tabla de multiplicar: "))
tabla_multiplicar(numero)
#  PUNTO 7
print ("-------------------------------7")  
a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero (debe ser distinto de cero): "))
while b == 0:
    b = float(input("El segundo numero no puede ser cero, intente de nuevo: "))
resultados = operaciones_basicas(a, b)
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]:.2f}")
#  PUNTO 8
print ("-------------------------------8")  
peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"El indice de Masa Corporal (IMC) es: {imc:.2f}")
#  PUNTO 9
print ("-------------------------------9") 
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
print(f"{celsius}°C equivalen a {celsius_a_fahrenheit(celsius):.2f} en °F")
#  PUNTO 10
print ("-------------------------------10") 
a = float(input("Ingresa el primer numero: "))
b = float(input("Ingresa el segundo numero: "))
c = float(input("Ingresa el tercer numero: "))
print(f"El promedio es: {calcular_promedio(a, b, c):.2f}")
# 1-Muestra "Hola Mundo!" en la pantalla.
print("Hola Mundo!")

# 2-Solicita al usuario que ingrese su nombre y lo saluda
nombre = input("Por favor, ingresa tu nombre: ")
print(f"Hola {nombre}!")

# 3-Solicita al usuario que ingrese su nombre, apellido, edad y lugar de residencia,
#muestra una oración con lo ingresado
nombre = input("Por favor, ingresa tu nombre: ")
apellido = input("Por favor, ingresa tu apellido: ")
edad = input("Por favor, ingresa tu edad: ")
residencia = input("Por favor, ingresa tu lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# 4-Se ingresa el radio de un círculo y calcula su área y perímetro.

radio = float(input("Ingresa el radio del círculo: "))
pi = 3.1416
#área del círculo (A = pi * r^2)
area = pi * (radio ** 2)

#perímetro del círculo (P = 2 * pi * r)
perimetro = 2 * pi * radio

print(f"El área del círculo es: {area:.2f}")

# 5- Se ingresa cantidad en segundos y se convierte a horas
segundos = int(input("Ingresa la cantidad de segundos: "))
horas = segundos / 3600

print(f"{segundos} segundos equivalen a {horas:.2f} horas")

# Se ingresa un número y se imprime su tabla de multiplicar usando una cadena multilínea.
numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))
print(f"""
Tabla de multiplicar del {numero}:
{numero} x 1 = {numero * 1}
{numero} x 2 = {numero * 2}
{numero} x 3 = {numero * 3}
{numero} x 4 = {numero * 4}
{numero} x 5 = {numero * 5}
{numero} x 6 = {numero * 6}
{numero} x 7 = {numero * 7}
{numero} x 8 = {numero * 8}
{numero} x 9 = {numero * 9}
{numero} x 10 = {numero * 10}
""")
# 7-Se solicita al usuario dos números enteros distintos de 0 y realiza las operaciones básicas

num1 = int(input("Ingresa el primer número (distinto de 0): "))
num2 = int(input("Ingresa el segundo número (distinto de 0): "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print(f"La suma de {num1} y {num2} es: {suma}")
print(f"La resta de {num1} y {num2} es: {resta}")
print(f"La multiplicación de {num1} y {num2} es: {multiplicacion}")
print(f"La división de {num1} entre {num2} es: {division:.2f}")

#8-Solicitar altura y peso del usuario para calcular su masa corporal
peso = float(input("Ingrese su peso en Kg: "))
altura = float(input("Ingrese su altura en metros: "))
masa_corp = peso / (altura**2)
print(f"Su indice de masa corporal es: {masa_corp:.2f}")

# 9- Solicita al usuario una temperatura en grados Celsius y la convierte a Fahrenheit

celsius = float(input("Ingresa la temperatura en grados Celsius (°C): "))
fahrenheit = (9 / 5) * celsius + 32
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

#10- Se solicita al usuario 3 números y se calcula su promedio
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

promedio = (num1 + num2 + num3) / 3

print(f"El promedio de {num1}, {num2} y {num3} es: {promedio:.2f}")
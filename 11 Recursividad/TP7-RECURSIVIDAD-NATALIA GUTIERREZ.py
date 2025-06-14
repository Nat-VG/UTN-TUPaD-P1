# Funcion factorial recursivo
def factorial(n):
    #Caso Base
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# 2) Fibonacci recursivo
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# 3) Funcion calculo de Potencia con recursividad 
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente-1)

# 4) Decimal a binario recursivo (como string)
def decimal_a_binario(n):
    if n < 2:
        return str(n)
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
    
# 5) Palíndromo 
def es_palindromo(palabra):
    # la palabra debe estar sin espacios ni tildes
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# 6) Suma dígitos recursiva (s/convertir a string)
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)

# 7) Contar bloques en una pirámide
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n-1)

# 8) Contar cuantas veces aparece un dígito dentro de un número
def contar_digito(numero, digito):
    # Caso base: número de un solo dígito
    if numero < 10:
        if numero == digito:
            return 1 
        else:
            return 0
    
    # Verificar el último dígito y sumar de forma recursiva
    if numero % 10 == digito:
       return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

print("*" * 30)
print("1 - FACTORIAL")
print("*" * 30)
num = int(input("Ingrese un número para calcular su factorial de todos los numeros hasta el ingresado: "))
for i in range(1, num + 1):
    print(f"El factorial del número {i} es: {factorial(i)}")

print("*" * 30)
print("2 - FIBONACCI")
print("*" * 30)

posicion = int(input("Ingresa hasta qué posición quieres ver la serie de Fibonacci "))
print(f"\nMostrando la serie de Fibonacci hasta la posicion {posicion}:")
for i in range(posicion + 1):
        print(f"En la posicion F({i}) = {fibonacci(i)}")

print("*" * 30)
print("3 - POTENCIA")
print("*" * 30)

print("\nPOTENCIA: Prueba con los numeros 5 y 3 ===> Potencia 5^3:", potencia(5, 3))

print("*" * 30)
print("4 - DECIMAL A BINARIO / EL USUARIO INGRESA EL NUMERO A CONVERTIR")
print("*" * 30)

numero = int(input("\nIngresa un número decimal positivo (0 para salir): "))
print(f"El numero {numero} en binario es {decimal_a_binario(numero)}")

print("*" * 30)
print("5 - ES O NO PALINDROMO?")
print("*" * 30)

texto = input("Ingrese una palabra (sin espacios ni tildes): ").lower()
if es_palindromo(texto):
    print(f"'{texto}' SÍ es un palíndromo")
else:
    print(f"'{texto}' NO es un palíndromo")

print("*" * 30)
print("6 - SUMA DE DIGITOS DE UN NUMERO")
print("*" * 30)

numero = int(input("Ingrese un número entero positivo: "))

# Validar que el número sea positivo
while numero < 0:
    print("¡Error! Debe ingresar un número positivo.")
    numero = int(input("Ingrese un número entero positivo: "))
resultado = suma_digitos(numero)
print(f"La suma de los dígitos de {numero} es: {resultado}")

print("*" * 30)
print("7 - PIRAMIDE con BLOQUES")
print("*" * 30)

entrada_valida = False
while not entrada_valida:
        try:
            base = int(input("Ingrese cantidad de bloques para la base (debe ser entero y mayor que cero): "))
            if base > 0:
                entrada_valida = True
            else:
                print("¡Debe ser positivo!")
        except ValueError:
            print("¡Error! Entrada Inválida.")

total = contar_bloques(base)

print(f"\nDetalle de la pirámide:")
print(f"Bloques en la base: {base}")
print(f"Total de bloques necesarios: {total}")

print("*" * 30)
print("8-CUANTAS VECES APARECE EL DIGITO INGRESADO EN UN NUMERO DADO")
print("*" * 30)


# Validamos que se ingrese un num positivo
num_valido = False
while not num_valido:
    try:
        num = int(input("Ingrese un número positivo: "))
        if num >= 0:
            num_valido = True
        else:
            print("¡Debe ser positivo!")
    except ValueError:
        print("Error: Ingrese un número válido")

# Validación para el dígito
dig_valido = False
while not dig_valido:
    try:
        digito = int(input("Ingrese dígito a buscar (0-9): "))
        if 0 <= digito <= 9:
            dig_valido = True
        else:
            print("¡Debe ser entre 0 y 9!")
    except ValueError:
        print("Error: Ingrese un dígito válido")

# Calcular y mostrar resultado
total = contar_digito(num, digito)
print(f"\n El dígito {digito} aparece {total} veces en {num}")
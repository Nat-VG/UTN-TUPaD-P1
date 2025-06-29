################################################################
# PUNTO 1: Añadir nuevas frutas al diccionario precios_frutas
print("\n=== PUNTO 1 ===")
print("Añadir las frutas Naranja, Manzana y Pera con sus precios al diccionario")

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
print("\nValores iniciales del diccionario:")
print(precios_frutas)

# Añadir nuevas frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("\nDiccionario con valores actualizados:")
print(precios_frutas)
input("\nPresione Enter para continuar...")

################################################################
# PUNTO 2: Actualizar precios
print("\n=== PUNTO 2 ===")

print("\nDiccionario con precios originales:")
print(precios_frutas)

# Actualizar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("\nDiccionario después de actualizar precios:")
print(precios_frutas)
input("\nPresione Enter para continuar...")

################################################################
# PUNTO 3: Crear lista solo con nombres de frutas
print("\n=== PUNTO 3 ===")
print("Crear una lista que contenga solo los nombres de las frutas-sin precios")

lista_frutas = list(precios_frutas.keys())
print("\nLista de frutas:")
print(lista_frutas)
input("\nPresione Enter para continuar...")

################################################################
# PUNTO 4: Números telefónicos
print("\n=== PUNTO 4 ===")
print("Almacenar y consultar 5 números telefónicos")

contactos = {}
print("\nIngrese 5 contactos:")
for i in range(5):
    nombre = input(f"Nombre del contacto {i+1}: ")
    numero = input(f"Teléfono de {nombre}: ")
    contactos[nombre] = numero

nombre_consulta = input("\nIngrese nombre a consultar: ")
if nombre_consulta in contactos:
    print(f"Teléfono de {nombre_consulta}: {contactos[nombre_consulta]}")
else:
    print("Contacto no encontrado")
input("\nPresione Enter para continuar...")

################################################################
# PUNTO 5: Análisis de palabras en frase
print("\n=== PUNTO 5 ===")
print("Analizar una frase para mostrar palabras únicas y su frecuencia")

frase = input("\nIngrese una frase: ")
palabras = frase.split()

# Se utiliza set para encontrar Palabras únicas
unicas = set(palabras)
print("\nPalabras únicas:")
print(unicas)

# Se realiza el recuento de palabras
recuento = {}
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1

print("\nRecuento de palabras:")
print(recuento)
input("\nPresione Enter para continuar...")

################################################################
# PUNTO 6: Promedio
print("\n=== PUNTO 6 ===")
print("Calcular promedio de 3 notas de 3 alumnos")

alumnos = {}
for i in range(3):
    nombre = input(f"\nNombre del alumno {i+1}: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Nota {j+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

# Mostrar promedios
print("\nPromedios:")
for nombre, notas in alumnos.items():
    promedio = sum(notas)/3
    print(f"{nombre}: {promedio:.2f}")
input("\nPresione Enter para continuar...")

################################################################
# PUNTO 7: Operaciones con conjuntos de estudiantes
print("\n=== PUNTO 7 ===")
# Conjuntos de legajos de estudiantes que aprobaron 
aprobados_p1 = {101, 102, 105, 107, 110}  # Legajos que aprobaron Parcial 1
aprobados_p2 = {102, 103, 105, 108, 110}  # Legajos que aprobaron Parcial 2
    
print("\nESTUDIANTES (por legajo) QUE APROBARON:")
print(f"• Parcial 1: {aprobados_p1}")
print(f"• Parcial 2: {aprobados_p2}")
    
# Intersección: aprobaron ambos parciales
aprobados_ambos = aprobados_p1 & aprobados_p2
print("\n1. APROBARON AMBOS PARCIALES:")
print(f"Legajos: {aprobados_ambos}")

# Diferencia simétrica: aprobaron solo uno
aprobados_solo_uno = aprobados_p1 ^ aprobados_p2
print("\n2. APROBARON SOLO UN PARCIAL:")
print(f"Legajos: {aprobados_solo_uno}")

# Detalle de qué parcial aprobó cada uno
solo_p1 = aprobados_p1 - aprobados_p2
solo_p2 = aprobados_p2 - aprobados_p1
print(f"  - Solo Parcial 1: {solo_p1}")
print(f"  - Solo Parcial 2: {solo_p2}")

# Unión: aprobaron al menos uno
aprobados_totales = aprobados_p1 | aprobados_p2
print("\n3. APROBARON AL MENOS UN PARCIAL:")
print(f"Total legajos: {aprobados_totales}")

input("\nPresione Enter para continuar...") 

################################################################
# PUNTO 8: stock de productos
print("\n=== PUNTO 8 ===")
print("Operaciones con el Stock de los productos")

stock = {"Lápiz": 50, "Cuaderno": 30, "Goma": 20}
print("\nStock inicial:")
print(stock)

# Modificar stock
producto = input("\nProducto a consultar/modificar: ")
if producto in stock:
    print(f"Stock actual: {stock[producto]}")
    opcion = input("¿Agregar unidades? (s/n): ")
    if opcion.lower() == 's':
        unidades = int(input("Unidades a agregar: "))
        stock[producto] += unidades
        print(f"Nuevo stock: {stock[producto]}")
else:
    print("Producto no existe")
    opcion = input("¿Crear producto? (s/n): ")
    if opcion.lower() == 's':
        unidades = int(input("Stock inicial: "))
        stock[producto] = unidades
        print(f"{producto} agregado con stock {unidades}")

print("\nStock final:")
print(stock)
input("\nPresione Enter para continuar...")

################################################################
# PUNTO 9: Agenda
print("\n=== PUNTO 9 ===")
print("Consultar agenda de actividades por día y hora")

agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés"
}

print("\nEventos actuales:")
for (dia, hora), evento in agenda.items():
    print(f"{dia} {hora}: {evento}")

# Consultar evento
dia = input("\nDía a consultar: ")
hora = input("Hora a consultar: ")
evento = agenda.get((dia, hora), "No hay eventos")
print(f"\nEvento el {dia} a las {hora}: {evento}")
input("\nPresione Enter para continuar al PUNTO 10...")

################################################################
# PUNTO 10: Invertir diccionario países-capitales
print("\n=== PUNTO 10 ===")
print("Invertir diccionario de países y capitales")

paises = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Brasil": "Brasilia"}
print("\nDiccionario original:")
print(paises)

# Invertir diccionario
capitales = {capital: pais for pais, capital in paises.items()}
print("\nDiccionario invertido:")
print(capitales)

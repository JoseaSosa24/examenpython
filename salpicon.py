# Función para ingresar los datos de una fruta
def ingresar_fruta():
    id_fruta = input("ID de la fruta: ")
    nombre_fruta = input("Nombre de la fruta: ")
    precio_unitario = float(input("Precio Unitario de la fruta: $"))
    cantidad = int(input("Cantidad de la fruta: "))
    return {
        "ID": id_fruta,
        "Nombre": nombre_fruta,
        "Precio Unitario": precio_unitario,
        "Cantidad": cantidad
    }

# Función para calcular el costo total del salpicón
def calcular_costo_total(frutas):
    costo_total = 0
    for fruta in frutas:
        costo_total += fruta["Precio Unitario"] * fruta["Cantidad"]
    return costo_total

# Función para encontrar la fruta más barata
def encontrar_fruta_mas_barata(frutas):
    return min(frutas, key=lambda fruta: fruta["Precio Unitario"])

# Función para encontrar la fruta más cara
def encontrar_fruta_mas_cara(frutas):
    return max(frutas, key=lambda fruta: fruta["Precio Unitario"])

# Función para mostrar todas las frutas ordenadas de mayor a menor costo
def mostrar_frutas_ordenadas(frutas):
    frutas_ordenadas = sorted(frutas, key=lambda fruta: fruta["Precio Unitario"], reverse=True)
    print("\nFrutas ordenadas de mayor a menor costo:")
    for fruta in frutas_ordenadas:
        print(f"{fruta['Nombre']} - Precio: ${fruta['Precio Unitario']}")

# Lista para almacenar las frutas
frutas = []

# Pedimos al usuario cuántas frutas quiere ingresar
n = int(input("¿Cuántas frutas quieres agregar? "))

# Ingresamos los datos de cada fruta
for i in range(n):
    print(f"\nIngresa los datos de la fruta {i + 1}:")
    fruta = ingresar_fruta()
    frutas.append(fruta)

# Calculamos el costo total del salpicón
costo_total = calcular_costo_total(frutas)

# Encontramos la fruta más barata y la más cara
fruta_mas_barata = encontrar_fruta_mas_barata(frutas)
fruta_mas_cara = encontrar_fruta_mas_cara(frutas)

# Mostramos los resultados
print(f"\nCosto total del salpicón: ${costo_total}")
print(f"La fruta más barata es {fruta_mas_barata['Nombre']} con un precio de ${fruta_mas_barata['Precio Unitario']}")
print(f"La fruta más cara es {fruta_mas_cara['Nombre']} con un precio de ${fruta_mas_cara['Precio Unitario']}")

# Mostramos todas las frutas ordenadas de mayor a menor costo
mostrar_frutas_ordenadas(frutas)

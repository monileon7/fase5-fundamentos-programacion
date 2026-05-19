# Nombre del estudiante: Mónica León
# Grupo: [213022]
# Programa: Fase 5 - Evaluación Final POA "Inventario sala de sistemas"
# Código fuente: autoría propia

#Bienvenida al empleado
print("¡Bienvenido al sistema de inventario!")
print("")


# ==========================================
# FASE 5 - FUNDAMENTOS DE PROGRAMACIÓN
# INVENTARIO SALA DE SISTEMAS
# ==========================================

# MATRIZ
# [Código, Nombre, Stock Actual, Stock Mínimo]

inventario = [
    ["FDCP1", "Mouse USB", 3, 10],
    ["FDCP2", "Teclado", 8, 10],
    ["FDCP3", "Cable HDMI", 2, 5],
    ["FDCP4", "Monitor", 6, 4],
    ["FDCP5", "Diademas", 1, 6]
]


# ==========================================
# FUNCIÓN PARA CALCULAR PEDIDO
# ==========================================

def calcular_pedido(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0


# ==========================================
# CICLO PRINCIPAL
# ==========================================

opcion = "1"

while opcion == "1":

    print("\n========================================")
    print(" INVENTARIO SALA DE SISTEMAS")
    print("========================================")

    # MOSTRAR PRODUCTOS DISPONIBLES
    print("\nLISTA DE ARTÍCULOS:\n")

    for articulo in inventario:
        print("Código:", articulo[0], "| Artículo:", articulo[1])

    # PEDIR CÓDIGO
    codigo_buscar = input("\nIngrese el código del artículo: ")

    encontrado = False

    # BUSCAR ARTÍCULO
    for articulo in inventario:

        codigo = articulo[0]
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]

        if codigo_buscar == codigo:

            encontrado = True

            cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

            print("\n========== RESULTADO ==========")
            print("Artículo:", nombre)
            print("Stock actual:", stock_actual)
            print("Stock mínimo:", stock_minimo)

            if cantidad_pedir > 0:
                print("Cantidad a solicitar:", cantidad_pedir)
                print("Estado: REQUIERE REABASTECIMIENTO")
            else:
                print("Cantidad a solicitar: 0")
                print("Estado: STOCK SUFICIENTE")

    # SI NO EXISTE EL CÓDIGO
    if encontrado == False:
        print("\nEl código ingresado no existe.")

    # NUEVA CONSULTA
    print("\n¿Desea realizar otra consulta?")
    print("1. Sí")
    print("2. No")

    opcion = input("Seleccione una opción: ")


print("\nPrograma finalizado correctamente.")

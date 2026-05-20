# Nombre del estudiante: Mónica León
# Grupo: [213022]
# Programa: Fase 5 - Evaluación Final POA "Inventario sala de sistemas"
# Código fuente: autoría propia


print("¡Bienvenido al sistema de inventario!\n")

inventario = [
    ["FDCP1", "Mouse USB", 3, 10],
    ["FDCP2", "Teclado", 8, 10],
    ["FDCP3", "Cable HDMI", 2, 5],
    ["FDCP4", "Monitor", 6, 4],
    ["FDCP5", "Diademas", 1, 6]
]

def calcular_pedido(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0


opcion = "2"

while opcion != "3":

    print("\n========================================")
    print(" INVENTARIO SALA DE SISTEMAS")
    print("========================================")

    print("\nLISTA DE ARTÍCULOS:\n")

    for articulo in inventario:
        print("Código:", articulo[0], "| Artículo:", articulo[1])

    print("\n1. Actualizar inventario")
    print("2. Consultar producto")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    # ======================================
    # OPCIÓN 1: ACTUALIZAR INVENTARIO
    # ======================================
    if opcion == "1":

        codigo_buscar = input("\nIngrese el código del producto a actualizar: ")
        encontrado = False

        for articulo in inventario:

            if articulo[0] == codigo_buscar:
                encontrado = True

                print("Producto encontrado:", articulo[1])
                print("Stock actual:", articulo[2])

                nuevo_stock = int(input("Ingrese el nuevo stock actual: "))

                articulo[2] = nuevo_stock

                print("\n✔ Inventario actualizado correctamente.")
                break

        if not encontrado:
            print("\n❌ Código no encontrado.")

    # ======================================
    # OPCIÓN 2: CONSULTA
    # ======================================
    elif opcion == "2":

        codigo_buscar = input("\nIngrese el código del artículo: ")
        encontrado = False

        for articulo in inventario:

            codigo, nombre, stock_actual, stock_minimo = articulo

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

        if not encontrado:
            print("\n❌ El código ingresado no existe.")

print("\nPrograma finalizado correctamente.")


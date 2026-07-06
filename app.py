import modulo as m


def opcion_menu():
    print("----------- MENÚ PRINCIPAL -----------")
    print("1. Stock por categoría")
    print("2. Buscar productos por rango de precio")
    print("3. Actualizar precio")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Mostrar productos")
    print("7. Salir")
    print("--------------------------------------")


def stock_categoria(productos, inventario):
    categoria = str(input("Ingrese la categoría: ")).strip()
    while not m.validar_categoria(categoria):
        print("Error, no puede ser un texto vacío")
        categoria = str(input("Ingrese la categoría: ")).strip()
    m.stock_categoria(categoria, productos, inventario)


def buscar_por_precio(productos, inventario):
    if len(productos) == 0:
        print("No se encuentra registro de productos en la BD")
        return

    while True:
        try:
            precio_min = int(input("Ingrese precio mínimo: "))
            if precio_min > 0:
                break
            print("Error, no puede ser un número negativo")
        except:
            print("Error, debe ser un número entero")

    while True:
        try:
            precio_max = int(input("Ingrese precio máximo: "))
            if precio_max >= precio_min:
                break
            print("Error, el número debe ser igual o mayor al precio mínimo")
        except:
            print("Error, debe ser un número entero")
    m.buscar_precio(precio_min, precio_max, productos, inventario)


def actualizar_precio(productos):
    if len(productos) == 0:
        print("No se encuentran productos para actualizar")
        return

    continuar = "S"
    while continuar == "S":
        codigo = str(input("Ingrese el código del producto: ")).strip()

        if m.buscar_codigo(codigo, productos):
            while True:
                try:
                    nuevo_precio = int(input("Ingrese el nuevo precio: "))
                    while not m.validar_precio(nuevo_precio):
                        print("Error, debe ser un número mayor a 0")
                        nuevo_precio = int(input("Ingrese el nuevo precio: "))
                    break
                except:
                    print("Error, debe ser un número")

            m.actualizar_precio(codigo, nuevo_precio, productos)
            print("... precio actualizado!")
        else:
            print("No existe ese código")

        continuar = str(input("Desea actualizar otro producto? (S/N): "))


def main():
    productos = {
        "P101": ["Cuaderno", "Papelería", 2490, True],
        "P102": ["Lápiz", "Papelería", 590, True],
        "P103": ["Botella", "Accesorios", 6990, False],
        "P104": ["Mochila", "Accesorios", 24990, True],
    }

    inventario = {
        "P101": [30, 15],
        "P102": [120, 50],
        "P103": [0, 10],
        "P104": [8, 25],
    }

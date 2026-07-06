def buscar_diccionario(codigo, diccionario):
    codigo_busc = codigo.strip()
    for llave in diccionario:
        if llave.strip() == codigo_busc:
            return llave
    return None


def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if 1 <= opcion <= 7:
                return opcion
            print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe ser una opción válida")


# ------ Funciones de validación ---


def validar_vendidos(vendidos):
    if vendidos >= 0:
        return True
    else:
        return False


def validar_nombre_vacio(nombre):
    if len(nombre.strip()) > 0:
        return True
    else:
        return False


def validar_codigo(codigo, productos):
    if len(codigo.strip()) == 0:
        return False

    for llave in productos:
        if llave.lower() == codigo.lower():
            return False

    return True


def validar_categoria(categoria):
    if len(categoria.strip()) > 0:
        return True
    else:
        return False


def validar_precio(precio):
    if precio > 0:
        return True
    else:
        return False


def validar_disponible(opcion):
    if opcion.strip().upper() in ["S", "N"]:
        return True
    else:
        return False


def validar_stock(stock):
    if stock >= 0:
        return True
    else:
        return False


# ------------------------
def buscar_codigo(codigo, productos):
    for llave in productos:
        if llave.lower() == codigo.lower():
            return True
    return False


def stock_categoria(categoria, productos, inventario):
    total_stock = 0
    encontrados = 0

    for codigo in productos:
        if productos[codigo][1].lower() == categoria.lower():
            encontrados += 1
            total_stock += inventario[codigo][0]

    if encontrados == 0:
        print(f"\n No hay productos registrados en la categoría '{categoria}'")
    else:
        print(f"\n El stock total de la categoría '{categoria}' es: {total_stock}")

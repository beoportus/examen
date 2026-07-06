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


# ------ Funciones de validación -----


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


def buscar_precio(precio_min, precio_max, productos, inventario):
    resultados = []

    for codigo in productos:
        nombre = productos[codigo][0]
        precio = productos[codigo][2]
        stock = inventario[codigo][0]

        if precio_min <= precio <= precio_max and stock > 0:
            resultados.append([nombre, codigo])

    if len(resultados) == 0:
        print(f"\n No se encontraron productos entre ${precio_min} y ${precio_max}")
        return

    resultados()
    for nombre, codigo in resultados:
        print(f"{nombre} {codigo}")


def actualizar_precio(codigo, nuevo_precio, productos):
    for llave in productos:
        if llave == codigo:
            productos[llave][2] = nuevo_precio
            return True
        return False


def agregar_producto(
    codigo,
    nombre,
    categoria,
    precio,
    disponible,
    stock,
    vendidos,
    productos,
    inventario,
):
    if not validar_codigo(codigo, productos):
        return False

    producto = [nombre, categoria, precio, disponible]
    productos[codigo] = producto

    stock_producto = [stock, vendidos]
    inventario[codigo] = stock_producto

    return True


def eliminar_producto(codigo, productos, inventario):
    llave_real = None
    for llave in productos:
        if llave == codigo:
            llave_real = llave
            break

    if llave_real is None:
        return False

    del productos[llave_real]
    del inventario[llave_real]
    return True


def mostrar_productos(productos, inventario):
    if len(productos) == 0:
        print("\n No hay productos registrados")
        return

    for codigo in productos:
        nombre = productos[codigo][0]
        categoria = productos[codigo][1]
        precio = productos[codigo][2]
        disponible = productos[codigo][3]
        stock = inventario[codigo][0]
        vendidos = inventario[codigo][1]

        print(f"""
                CODIGO: {codigo}
                --------------------------
                Nombre: {nombre}
                Categoría: {categoria}
                Precio: ${precio}
                Disponible: {disponible}
                Stock: {stock}
                Vendidos: {vendidos}
                --------------------------""")

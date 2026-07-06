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


def validar_nombre_vacio(nombre):
    if len(nombre.strip()) > 0:
        return True
    else:
        print("Error, no puede ser un texto vacío")
        return False

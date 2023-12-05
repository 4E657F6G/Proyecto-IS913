def identificar_tipo_linea(linea):
    linea = linea.strip()

    if linea.startswith("if "):
        return "Sentencia if"
    elif linea.startswith("while "):
        return "Ciclo while"
    elif "=" in linea:
        return "Declaración de variable"
    else:
        return "Tipo no identificado"

# Ejemplo de uso
archivo_ruta = "../../tests/input/archivo.py"

with open(archivo_ruta, "r") as archivo:
    for numero_linea, linea in enumerate(archivo, start=1):
        tipo = identificar_tipo_linea(linea)
        if tipo != "Tipo no identificado":
            print(f"Línea {numero_linea}: {tipo}")
        
import os
class FileManager:

    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, "r") as file:
            return file.read()

    def create_file(self, file_name, content):
        with open(file_name, "w") as file:
            file.write(content)

lector = FileManager("../../tests/input/archivo.py")
contenido = lector.read_file()
lector.create_file("../../tests//output/archivo_copia.py", contenido)

#implementar lógica para que le asigne el nombre del archivo al nuevo archivo y clase en java
def obtener_nombre_archivo(ruta_archivo):
    nombre_archivo, extension = os.path.splitext(ruta_archivo)
    return nombre_archivo

ruta_archivo = "../../tests/input/archivo.py"

nombre_archivo = obtener_nombre_archivo(ruta_archivo)

print(nombre_archivo)


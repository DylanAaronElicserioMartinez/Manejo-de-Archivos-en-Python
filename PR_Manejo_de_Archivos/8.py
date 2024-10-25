print(" ")
print("Dylan Aaron ELicserio Martínez 3°W #Control:1179")
print(" ")
import os

# Verificar si el archivo "demofile.txt" existe
if os.path.exists("Act7.txt"):
    # Si existe, eliminar el archivo
    os.remove("Act7.txt")
    print("El archivo 'Act7.txt' ha sido eliminado.")
else:
    # Si no existe, imprimir un mensaje
    print("El archivo 'Act7.txt' no existe.")

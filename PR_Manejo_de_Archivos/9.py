print(" ")
print("Dylan Aaron ELicserio Martínez 3°W #Control:1179")
print(" ")
import os

# Intentar eliminar la carpeta "myfolder"
try:
    os.rmdir("myfolder")
    print("La carpeta 'myfolder' ha sido eliminada.")
except FileNotFoundError:
    print("La carpeta 'myfolder' no existe.")
except OSError:
    print("La carpeta 'myfolder' no está vacía.")
except Exception as e:
    print(f"Ocurrió un error: {e}")

# Imprimir un espacio en blanco
print(" ")
# Imprimir la información del estudiante
print("Dylan Aaron Elicserio Martínez 3°W #Control: 1179")
# Imprimir un espacio en blanco
print(" ")
# Abrir el archivo "Act4.txt" en modo lectura
Actividad4 = open("Act4.txt", "r")
# Leer y mostrar los primeros 5 caracteres del archivo
print(Actividad4.read(5))
# Cerrar el archivo después de la lectura
Actividad4.close()

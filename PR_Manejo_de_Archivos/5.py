print(" ")
print("Dylan Aaron ELicserio Martínez 3°W #Control:1179")
print(" ")
# Abrir el archivo en modo anexar
Act5 = open("Act5.txt", "a")
#ingresa la palabra que quieras ingresar al archivo
palabra=input("Ingresa la palabra a agregar:")
# Escribir en el archivo
Act5.write(palabra)
# Cerrar el archivo
Act5.close()
# Abrir el archivo en modo lectura para mostrar el contenido actualizado
Funcion = open("Act5.txt", "r")
print(Funcion.read())
# Cerrar el archivo después de leer
Funcion.close()

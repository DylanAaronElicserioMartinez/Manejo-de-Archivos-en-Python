print(" ")
print("Dylan Aaron ELicserio Martínez 3°W #Control:1179")
print(" ")
# Abrir el archivo en modo escribir (sobrescribir)
Act6 = open("Act6.txt", "w")
#ingresa la palabra que quieras ingresar al archivo
palabra=input("ingresa la palabra a agregar:")
# Escribir nuevo contenido en el archivo
Act6.write(palabra)
# Cerrar el archivo
Act6.close()
# Abrir el archivo en modo lectura para mostrar el nuevo contenido
Funcion = open("Act6.txt", "r")
print(Funcion.read())
# Cerrar el archivo después de leer
Funcion.close()

# Manejo-de-Archivos-en-Python
Actividad en clase


#Codigo 1

NO HAY SOLO ES UN DOCUMENTO DE TEXTO

![image](https://github.com/user-attachments/assets/b5365197-fe6d-4123-aadc-ca97603e7163)

#Codigo 2

# Imprimir un espacio en blanco

print(" ")

# Imprimir la información del estudiante

print("Dylan Aaron Elicserio Martínez 3°W #Control: 1179")

# Imprimir un espacio en blanco

print(" ")

# Abrir el archivo "Act1.txt" en modo lectura

Act2 = open("Act1.txt", "r")

# Leer y mostrar el contenido del archivo

print(Act2.read())

# Cerrar el archivo después de la lectura

Act2.close()

![image](https://github.com/user-attachments/assets/a4c34288-1879-4442-ba69-0151a4a1cb93)

![image](https://github.com/user-attachments/assets/3d20b42a-0a4b-4f6e-95d8-1dbecf6efc45)

#Codigo 3

# Imprimir un espacio en blanco

print(" ")

# Imprimir la información del estudiante

print("Dylan Aaron Elicserio Martínez 3°W #Control: 1179")

# Imprimir un espacio en blanco

print(" ")

# Abrir el archivo "Act1.txt" desde una ruta específica en modo lectura

Act3 = open("E:\\3W_Elicserio\\HTML\\PR_Manejo_de_Archivos\\Act1.txt", "r")

# Leer y mostrar el contenido del archivo

print(Act3.read())

# Cerrar el archivo después de la lectura

Act3.close()

![image](https://github.com/user-attachments/assets/cbece10a-7be3-4d01-aed3-b77ba9b2fb48)

![image](https://github.com/user-attachments/assets/e5d6b03a-fa32-4f81-ae34-7541a00c9831)

#Codigo 4

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

![image](https://github.com/user-attachments/assets/f4709c43-0955-4d92-b0ad-1c05a2a46f33)

![image](https://github.com/user-attachments/assets/3af22f10-b1fd-4b56-b894-6d5b715935ea)

![image](https://github.com/user-attachments/assets/4c472ede-1bdf-45d0-ac1d-f3f25ef9f492)

#Codigo 5

print(" ")

print("Dylan Aaron ELicserio Martínez 3°W #Control:1179")

print(" ")

# Abrir el archivo en modo anexar

Act5 = open("Act5.txt", "a")

#ingresa la palabra que quieras ingresar al archivo

palabra=input("Ingresa la palabra a agregar:")

# Escribir en el archivo

Act5.write(palabra

# Cerrar el archivo

Act5.close()

# Abrir el archivo en modo lectura para mostrar el contenido actualizado

Funcion = open("Act5.txt", "r")

print(Funcion.read())

# Cerrar el archivo después de leer

Funcion.close()

![image](https://github.com/user-attachments/assets/9adeb5b4-da87-4742-aff2-f3f5e786ba93)

![image](https://github.com/user-attachments/assets/1ff1e947-6822-40d6-92c9-7d7f9f5cc5ac)

![image](https://github.com/user-attachments/assets/9e32f813-c214-4e98-9ed9-ec07477fc1d0)

#Codigo 6

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

![image](https://github.com/user-attachments/assets/61930375-89be-4b14-ae68-02aeb2ef01ea)

![image](https://github.com/user-attachments/assets/57d71738-13a9-4ec7-81b9-79f80cbef50a)

#Codigo 7

print(" ")

print("Dylan Aaron ELicserio Martínez 3°W #Control:1179")

print(" ")

import os

os.remove("Act7.txt")

![image](https://github.com/user-attachments/assets/7110480b-f6c7-4eb3-8bf4-36ee32ae1247)

![image](https://github.com/user-attachments/assets/2bc6506b-013b-4cdc-b831-49ea2c8c6ee7)

#Codigo 8

print(" ")

print("Dylan Aaron ELicserio Martínez 3°W #Control:1179")

print(" ")

import os

# Verificar si el archivo "Act7.txt" existe

if os.path.exists("Act7.txt"):

    # Si existe, eliminar el archivo
    
    os.remove("Act7.txt")
    
    print("El archivo 'Act7.txt' ha sido eliminado.")
    
else:

    # Si no existe, imprimir un mensaje
    
    print("El archivo 'Act7.txt' no existe.")

![image](https://github.com/user-attachments/assets/135ee583-f5ff-4b09-8ace-047c8e9b3216)

![image](https://github.com/user-attachments/assets/198d1943-a027-4975-881d-77eeb82dc032)

#Codigo 9

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

![image](https://github.com/user-attachments/assets/b792209b-4430-4199-a772-9169459d7bab)

![image](https://github.com/user-attachments/assets/6b2000a9-ffe8-4b69-8e16-2a9d2448c01b)

![image](https://github.com/user-attachments/assets/4708b9b8-29bc-4107-a7c9-e52b2ceea060)

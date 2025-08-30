from pathlib import Path
import csv

siguiente = True
respuesta = ""
datos = []

while siguiente:
    cedula = input("Ingrese la cédula: ")
    nombre = input("Ingrese el nombre: ")
    saldo = float(input("Ingrese el saldo: "))

    Path("salida").mkdir(exist_ok=True)
    with open("archivo.csv", "a", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        lector = csv.reader(f)
         
        escritor.writerow([cedula, nombre, saldo])

    print("¿Hay otro en la fila? 1 = no - otro numero = si")
    respuesta = input()   

    if respuesta == "1":   
        siguiente = False
    else:
        siguiente = True
    
    with open("archivo.csv", "r", newline="", encoding="utf-8") as f:
        lector = csv.reader(f)
        next(lector) 

        for fila in lector:
            saldo = float(fila[2])
            if saldo > 50:
                datos.append([fila[0], fila[1], float(fila[2])])

print("Matriz de datos:", datos)

with open("archivo.csv", mode="r", encoding="utf-8") as f:
    todo = f.read()        # leer todo

with open("archivo.csv", "r", encoding="utf-8") as f:
    for linea in f:        # iterar línea a línea (eficiente)
        print(linea.strip())

# Otras utilidades
f = open("archivo.csv", "r", encoding="utf-8")
try:
    primero = f.readline()     # una línea
    resto = f.readlines()      # lista de líneas
finally:
    f.close()

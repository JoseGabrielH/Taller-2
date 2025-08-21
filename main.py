from pathlib import Path  # <-- ojo, te faltaba importar Path

siguiente = True
respuesta = ""

while siguiente:
    cedula = input("Ingrese la cédula: ")
    nombre = input("Ingrese el nombre: ")
    saldo = float(input("Ingrese el saldo: "))

    Path("salida").mkdir(exist_ok=True)
    with open("salida/reporte.txt", "w", encoding="utf-8") as f:
        f.write("Cedula\n")
        f.writelines([cedula])
        f.write("Nombre\n")
        f.writelines([nombre])
        f.write("Saldo\n")
        f.writelines([saldo])

    print("¿Hay otro en la fila? 1 = no - otro numero = si")
    respuesta = input()   

    if respuesta == "1":   
        siguiente = False
    else:
        siguiente = True

with open("archivo.txt", mode="r", encoding="utf-8") as f:
    todo = f.read()        # leer todo

with open("archivo.txt", "r", encoding="utf-8") as f:
    for linea in f:        # iterar línea a línea (eficiente)
        print(linea.strip())

# Otras utilidades
f = open("archivo.txt", "r", encoding="utf-8")
try:
    primero = f.readline()     # una línea
    resto = f.readlines()      # lista de líneas
finally:
    f.close()

import os

class F:
    
    def escribir(self, archivo, diccionario):
        archivo_existe = os.path.isfile(archivo)
    
        with open(archivo, "a", encoding="utf-8") as f:
            if not archivo_existe: 
                encabezados = ",".join(diccionario.keys())
                f.write(encabezados + "\n")
            
            valores = ",".join(str(v) for v in diccionario.values())
            f.write(valores + "\n")
            
    def leer(self, filename):
        if not os.path.isfile(filename):
            print("El archivo no existe todavía.")
            return []
        with open(filename, "r", encoding="utf-8") as f:
            lineas = [line.strip() for line in f]
            for l in lineas:
                print(l)
            return lineas
                
    def eliminar(self, filename, id):
        if not os.path.isfile(filename):
            print("No existe el archivo:", filename)
            return
        with open(filename, "r", encoding="utf-8") as f:
            lineas = f.readlines()
        newList = []
        headers = lineas[0]
        newList.append(headers)
        
        for l in lineas[1:]:
            arr = l.strip().split(',')
            if str(arr[0]) == str(id):  
                arr[-1] = "0" 
                l = ",".join(arr) + "\n"
            newList.append(l)
        
        self.write_array(filename, newList)
        
    def write_array(self, filename, lista):
        with open(filename, "w", encoding="utf-8") as f:
            for l in lista:
                f.write(l)
                
    def sequential_search_csv(self, filename, value):
        if not os.path.isfile(filename):
            return -1
        with open(filename, "r", encoding="utf-8") as file:
            for i, line in enumerate(file):
                campos = line.strip().split(",")
                if value in campos:
                    return i
        return -1

siguinete = True
f = F()

while siguinete:
    print()
    print("***** Opciones del menú *****")
    print("1. Registrar un cliente.")
    print("2. Listar clientes.")
    print("3. Eliminar un cliente.")
    print("4. Registrar un producto.")
    print("5. Listar pedidos de un cliente.")
    print("6. Guardar una venta.")
    print("7. Listar las ventas realizadas por cliente.")
    print("8. Salir.")
    print("-----------------------------")
    opcion = int(input("Ingrese la opción: "))
    print("-----------------------------")
    
    if opcion == 1:
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        telefono = input("Telefono: ")
        id = input("Id: ")
        people = {"ID": id, "Nombre": nombre, "Apellido": apellido, "Telefono": telefono, "Estado": "1"}
        f.escribir("people.csv", people)
        
    elif opcion == 2:
        print("\n--------- Lista de clientes ---------")
        f.leer("people.csv")
        print("-------------------------------------")
        
    elif opcion == 3:
        id_ = input("ID del cliente que desea eliminar: ")
        f.eliminar("people.csv", id_)
        print("* Cliente eliminado (Estado = 0) *")
            
    elif opcion == 4:
        id_p = input("Ingrese el ID del pedido: ")
        id_c = input("Ingrese el ID del cliente: ")
        nombre_p = input("Ingrese el nombre del producto: ")
        precio = input("Ingrese el precio del producto: ")
        cantidad = input("Ingrese la cantidad: ")
        pedido = {"ID pedido": id_p, "ID cliente": id_c, "Producto": nombre_p, "Precio": precio, "Cantidad": cantidad, "Estado": "1"}
        f.escribir("pedidos.csv", pedido)
         
    elif opcion == 5:
        id_c = input("Ingrese el ID del cliente para listar pedidos: ")
        if not os.path.isfile("pedidos.csv"):
            print("No hay pedidos registrados.")
        else:
            print(f"\n--- Pedidos del cliente {id_c} ---")
            with open("pedidos.csv", "r", encoding="utf-8") as file:
                for line in file.readlines()[1:]:
                    arr = line.strip().split(",")
                    if arr[1] == id_c:  
                        print(line.strip())
    
    elif opcion == 6:
        id_c_v = input("ID del cliente: ")
        id_p = input("ID de la venta: ")
        nombre_p_v = input("Nombre del producto: ")
        precio = float(input("Precio unitario: "))
        cantidad_p_v = int(input("Cantidad: "))
        
        
        resultado = f.sequential_search_csv("people.csv", id_c_v)
        if resultado != -1:
            venta = {"ID venta": id_p, "ID cliente": id_c_v, "Producto": nombre_p_v, "Precio": precio, "Cantidad": cantidad_p_v, "Estado": "1"}
            f.escribir("ventas.csv", venta)
            print("Venta registrada.")
        else:
            print("Cliente no encontrado o inactivo.")
    
    elif opcion == 7:
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        if not os.path.isfile("ventas.csv"):
            print("No hay ventas registradas.")
        else:
            print(f"\n--- Ventas de {nombre_cliente} ---")
            total = 0
            with open("ventas.csv", "r", encoding="utf-8") as file:
                for line in file.readlines()[1:]:
                    arr = line.strip().split(",")
                    id_c, prod, precio, cantidad, estado = arr[1], arr[2], float(arr[3]), int(arr[4]), arr[5]
                    with open("people.csv", "r", encoding="utf-8") as clientes:
                        for c in clientes.readlines()[1:]:
                            arr_c = c.strip().split(",")
                            if arr_c[0] == id_c and arr_c[1] == nombre_cliente and arr_c[-1] == "1":
                                subtotal = precio * cantidad
                                print(f"Id_producto{id_p} | Cantidad: {cantidad} | Precio: {precio} | Subtotal: {subtotal} | Cliente: {id_c}")
                                total += subtotal
            print(f"Total de ventas: {total}")
    
    elif opcion == 8:
        print("Saliendo del sistema...")
        siguinete = False
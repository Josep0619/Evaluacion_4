Productos = {}
def Agregar_Producto(Lst_Productos: dict, Codigo: str, Datos: list) -> bool:
    Nombre, Precio = Datos
    Codigo = input("Ingrese código del producto: ").strip().lower()
    if Codigo in Lst_Productos:
        print("Ya se encuentra registrado este")
        return False
    else:
        Nombre = input("Ingrese el nombre del producto")
        try:
            Precio = int(input("Ingrese un precio para el producto"))
            if Precio <= 0:
                print("Este dato es negativo, ingrese un dato numerico entero positivo")
                return False
        except ValueError:
            print("Dato invalido, ingrese datos que sean solo numericos y no otro")
            return False
        else:
            Lst_Productos[Codigo]={"Nombre": Nombre, "Precio": Precio}
            print("Producto agregado correctamente")
            return True

def Listar_Productos(Lst_Productos: dict) -> None:
    if Codigo not in Lst_Productos:
        print("No existen productos en su diccionario")
        return
    print("\nListado de Productos")
    for Codigo, Datos in Productos.items():
        print(f"{Codigo} - {Datos['Nombre']} - {Datos['Precio']}")
        
def Buscar_Productos(Productos: dict) -> None:
    Codigo = input("Ingrese código del producto: ").strip().upper()
    if Codigo in Productos:
        Prod = Productos[Codigo]
        print(f"Producto encontrado:  {Codigo} - {Prod['nombre']} - {Prod['precio']}")
    else:
        print("Producto no encontrado")
        
def Eliminar_Producto(Productos: dict) -> None:
    Codigo = input("Ingrese código del productoa eliminar: ").strip().upper()
    if Codigo in Productos:
        del Productos[Codigo]
        print("Producto Eliminado Correctamente")
    else:
        print("Producto no encontrado")
        
def main():
    while True:
        print("_"*50)
        print("Menu De Productos")
        print("_"*50)
        print("1.-Agregar Nuevos Productos")
        print("2.-Mostrar Todos Los Productos")
        print("3.-Buscar Producto")
        print("4.-Eliminar Producto")
        print("5.-Salir Del Programa")
        Op = input("Ingrese una Opcion del Menu: ")
        if Op == "1":
            Agregar_Producto(Productos)
        elif Op == "2":
            Listar_Productos(Productos)
        elif Op == "3":
            Buscar_Productos(Productos)
        elif Op == "4":
            Eliminar_Producto(Productos)
        elif Op == "5":
            print("Saliendo del programa")
            break
        else:
            print("Opcion Invalida")

if __name__ == "__main__":
    main()    
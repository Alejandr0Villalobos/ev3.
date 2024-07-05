import os 
import json
productos = [
"Café Americano",
"Té Chai",
"Croissant",
"Jugo Naranja",
"Panini de Pavo y Queso",
"Pastel de Zanahoria",
"Espresso Doble",
"Ba;do de Frutas",
"Muffin",
"Ensalada",
"Chocolate Caliente",
"Tarta de Frambuesa",
"Sándwich de Huevo",
"Galletas de Avena",
"Frappé de Caramelo"
]



def menu_principal():
    os.system("cls")
    print("1. Asignar montos")
    print("2. Ver estadisticas")
    print("3. Salir del programa")

def opcion_principal():
    opcionPrincipal = 0
    try:
        opcionPrincipal = int(input("Ingrese una de las opciones > "))
    except:
        pass
    if opcionPrincipal < 1 or opcionPrincipal > 3:
        input("Opcion no valida, presione enter para volver a intentarlo > ")
    else:
        return opcionPrincipal
    
def asignar_montos():
    print("___ASIGNAR VALORES___")
  



def ver_estadisticas():
    os.system("cls") 
    print("___ESTADISTICAS___")
    print("1. Producto con valor mas alto")
    print("2. Producto con valor del IVA mas bajo")
    print("3. Promedio del valor de los productos")
    print("4. Media geografica del valor de los productos")
    print("5. Volver a menu principal")
    opcionEstadisticas = 0
    try:
        opcionEstadisticas = int(input("Ingrese una de las opciones > "))
    except:
        pass

    if opcionEstadisticas < 1 or opcionEstadisticas > 5:
        input("Opcion no valida, presione enter para volver a intentarlo > ")
    else:
        return opcionEstadisticas
    
    
def inicio_programa():
    while True:
        menu_principal()
        opcionPrincipal = opcion_principal()
        if opcionPrincipal == 1:
            asignar_montos()
        elif opcionPrincipal == 2:
            while True:
                ver_estadisticas()
                opcionEstadisticas = ver_estadisticas()
                if opcionEstadisticas == 1:
                    print("Producto con valor mas alto")
                elif opcionEstadisticas == 2:
                    print("Producto con valor del IVA mas bajo")
                elif opcionEstadisticas == 3:
                    print("Promedio del valor de los productos")
                elif opcionEstadisticas == 4:
                    print("Media geografica del valor de los productos")
                elif opcionEstadisticas == 5:
                    print("Volver a menu principal")
                    return inicio_programa()
                
        elif opcionPrincipal == 3:
            os.system("cls")
            print("Cerrando programa...")
            return
        input()


if __name__ == "__main__":
    inicio_programa()
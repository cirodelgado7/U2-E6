from ClaseFechaHora import FechaHora
from ClaseMenuFechaHora import Menu

if __name__ == '__main__':
    r1 = FechaHora(30, 12, 2020, 14, 30, 00)
    r2 = FechaHora(30, 12, 2020, 14, 30, 00)
    r1.Mostrar()
    r2.Mostrar()
    r3 = r1 + r2
    r3.Mostrar()
    menu = Menu()
    salir = False
    while not salir:
        print("\n-----------------Menu--------------------")
        print("1 - Sumar")
        print("2 - Restar")
        print("3 - Comparar")
        print("4 - Salir")
        op = int(input('Ingrese una opcion: '))
        menu.opcion(op, r1, r2)
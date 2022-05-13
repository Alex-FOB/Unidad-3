from Menu import menu

from Ramos import ramo

from Flores import flor

def test():
    unaFlor = flor(1, 'Rosa', 'Rojo', 'Linda pero espinosa')
    unRamo = ramo('mediano', unaFlor, 6)
    print(unRamo)
    otraFlor = flor(2, 'Loto', 'Blanca', 'Flor hermosa oriental')
    unRamo.addFlor(otraFlor, 3)
    print(unRamo)
if __name__ == '__main__':
    if(str(input('¿Desea testear?: ')).lower() == 'si'):
        test()
    else:
        band = False
        interfaz = menu()
        while not band:
            print('1.- Registrar ramo\n2.- Mostrar las flores mas vendidas\n3.- Mostrar tipo de ramo\n4.- Salir')
            try:
                op = int(input('Opcion: '))
                interfaz.opcion(op)
                band = op == 4
            except ValueError:
                interfaz.error()
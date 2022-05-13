from Facultad import facultad

from Menu import menu

def test():
    lista = [1, 1, 'Licenciatura en Ciencias de la Computacion', 'Licenciado en Ciencias de la Computacion', 'Diez Semestres', 'Grado']
    unaFacultad = facultad(1, 'Facultad de Ciencias Exactas, Fisicas y Naturales', 'Av. Ignacio de la Roza 590 (O)', 'Rivadavia, SanJuan', '0264-4222065') #faltaria el indice y la lista
    print(unaFacultad)
    #NOTA: debido a como está hecho el __init__ de Facultad no se puede enviar "lista"
    #por ende, solamente se comprueba la creación de una Facultad
if __name__ == '__main__':
    if(str(input('¿Desea testear? ')).lower() == 'si'):
        test()
    else:
        band = False
        inter = menu()
        while not band:
            print('1.- Buscar facultad\n2.- Buscar carrera\n3.- Mostrar facultades\n4.- Salir')
            try: #intenta hacer el cast, si da error imprime ERROR
                op = int(input('Opcion: '))
                inter.opcion(op)
                band = op == 4
            except ValueError:
                inter.error()
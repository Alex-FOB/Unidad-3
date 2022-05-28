import csv

from Menu import menu

from Arreglo import arreglo

from CalefactorGas import gas

from CalefactorElectrico import electrico

def lecturaElectricos(coleccion):
    band = False
    with open('Ejercicio 4/calefactor-electrico.csv') as archi: #abre el archivo
        reader = csv.reader(archi, delimiter = ';')
        for fila in reader:
            if(band == False):
                band = True
            else:
                unCalefactor = electrico(fila[0], fila[1], fila[2], None, None) #se crea una instancia
                coleccion.addCalefactor(unCalefactor) #se añade la instancia creada
    archi.close()
    #return coleccion
def lecturaGas(coleccion):
    band = False
    with open('Ejercicio 4/calefactor-a-gas.csv') as archi: #abre el archivo
        reader = csv.reader(archi, delimiter = ';')
        for fila in reader:
            if(band == False):
                band = True
            else:
                unCalefactor = gas(fila[0], fila[1], None, fila[2], fila[3]) #se crea una instancia
                coleccion.addCalefactor(unCalefactor) #se añade la instancia creada
    archi.close()
    #return coleccion
if __name__ == '__main__':
    if(str(input('¿Desea testear? ')).lower() == 'si'):
        pass
    else:
        interfaz = menu()
        coleccion = arreglo()
        try:
            dim = int(input('Ingrese cantidad de calefactores: '))
            coleccion.modDim(dim)
            lecturaElectricos(coleccion) #coleccion = lecturaElectricos(coleccion)
            lecturaGas(coleccion) #coleccion = lecturaGas(coleccion)
            #coleccion.mostrar()
            interfaz.setArreglo(coleccion) #se le pasa una referencia de Arreglo al Menu
            band = False
            while not band:
                print('1.- Menor consumo de gas\n2.- Consumo electrico\n3.- Calefactores de menor consumo\n4.- Salir')
                try:
                    op = int(input('Opcion: '))
                    interfaz.opcion(op)
                    band = op == 4
                except ValueError:
                    interfaz.error()
        except ValueError:
            interfaz.error()
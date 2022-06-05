from zope.interface import Interface

class interfazDirector(Interface):
    def modificarBasico(cuil, nuevoBasico):
        pass
    def modificarPorcentajePorCargo(cuil, nuevoProcentaje):
        pass
    def modificarPorcentajePorCategoria(cuil, nuevoPorcentaje):
        pass
    def modificarImporteExtra(cuil, nuevoImporteExtra):
        pass

    #NOTA: se reemplaza el dni por el cuil, ya que los agentes no se le registran el dni
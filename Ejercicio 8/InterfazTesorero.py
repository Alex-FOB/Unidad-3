from zope.interface import Interface

class interfazTesorero(Interface):
    def gastosSueldoPorEmpleado(cuil):
        pass
    
    #DATO: se reemplaza el dni por el cuil, ya que los agentes no se le registran el dni
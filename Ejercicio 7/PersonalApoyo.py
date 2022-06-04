from Agente import agente

class personalApoyo(agente):
    __categoria = None
    def __init__(self, cuil, ape, nom, sueldo, antiguedad, categoria):
        super().__init__(cuil, ape, nom, sueldo, antiguedad)
        try:
            self.__categoria = int(categoria)
        except ValueError:
            self.__categoria = None
    def __str__(self):
        return '{}\n    Categoria: {}'.format(super().__str__(), self.__categoria)
    def getCategoria(self):
        return self.__categoria
    def toJson(self):
        diccionario = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                cuil = super().getCuil(),
                ape = super().getApe(),
                nom = super().getNom(),
                sueldo = super().getSueldo(),
                antiguedad = super().getAntiguedad(),
                categoria = self.__categoria
            )
        )
        return diccionario
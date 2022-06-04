from Docente import docente

from Investigador import investigador

class docenteInvestigador(docente, investigador):
    __categoria = None #categoria en el programa de incentivos de investigacion
    __importeExtra = None
    def __init__(self, cuil, ape, nom, sueldo, antiguedad, area, tipo, carrera, cargo, catedra, categoria, importeExtra):
        try:
            super().__init__(cuil, ape, nom, sueldo, antiguedad, area, tipo, carrera, cargo, catedra, categoria, importeExtra)
            self.__categoria = str(categoria).upper()
            self.__importeExtra = float(importeExtra)
        except ValueError:
            self.__importeExtra = 0
    def __str__(self): 
        return '{}\n    Categoria: {:20} Importe extra: ${}'.format(super().__str__(), self.__categoria, self.__importeExtra)
    def getCategoria(self):
        return self.__categoria
    def getImporteExtra(self):
        return self.__importeExtra
    def toJson(self):
        diccionario = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                cuil = super().getCuil(),
                ape = super().getApe(),
                nom = super().getNom(),
                sueldo = super().getSueldo(),
                antiguedad = super().getAntiguedad(),
                area = super().getArea(),
                tipo = super().getTipo(),
                carrera = super().getCarrera(),
                cargo = super().getCargo(),
                catedra = super().getCatedra(),
                categoria = self.__categoria,
                importeExtra = self.__importeExtra
            )
        )
        return diccionario
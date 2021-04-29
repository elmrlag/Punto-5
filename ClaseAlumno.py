class Alumno:
    __nombre=""
    __año = 0
    __division= 'A'
    __inasistencias = -1
    cdadMaxInas = 21
    cdadTotalClases = 5
    def __init__(self, nombre, año, division, inasistencias):
        if isinstance(nombre, str):
            self.__nombre=nombre
        if isinstance(año, str):
            self.__año=año
        if isinstance(division, str):
            self.__division=division
        if isinstance(inasistencias, str):
            self.__inasistencias=inasistencias
    def getAño(self):
        return self.__año
    def getDiv(self):
        return self.__division
    def getInas(self):
        return self.__inasistencias
    def getNomb(self):
        return self.__nombre
    @classmethod
    def setcdadMaxInas(cls, nuevaCdad):
        if isinstance(nuevaCdad,int):
            cls.cdadMaxInas=nuevaCdad
        else:
            print("error en la entrada de datos")
    @classmethod
    def getcdadMasInas(cls):
        return cls.cdadMaxInas
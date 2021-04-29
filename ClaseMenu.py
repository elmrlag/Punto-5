from ClaseAlumno import Alumno

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher= {1:self.opcion1, 2:self.opcion2, 3:self.salir}
    def opcion(self, opc, listaAlumnos):
        func = self.__switcher.get(opc, lambda: print("Opcion invalida"))
        func(listaAlumnos)
    def opcion1(self, listaAlumnos):
        a=int(input("ingrese el año: "))
        d= input("ingrese la division: ")
        print("alumno\tporcentaje")
        for alum in listaAlumnos:
            if alum.getAño() == a and alum.getDiv() == d:
                print("%s\t%1.2f" % (alum.getNomb(), alum.getInas()/Alumno.cdadMaxInas*100))
    def opcion2(self, listaAlumnos):
        nuevaCdad=int(input("ingrese la nueva cantidad de insasistencias: "))
        Alumno.setcdadMaxInas(nuevaCdad)
        print("la nueva cantidad es : {}".format(Alumno.getcdadMasInas()))
    def salir(self, listaAlumnos):
        pass
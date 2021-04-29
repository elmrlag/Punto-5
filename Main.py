from ClaseAlumno import Alumno
from ClaseMenu import Menu
from csv import reader
import os


def test():
    print("creacion de alumno")
    n=input("ingrese el nombre: ")
    a=int(input("ingrese el año: "))
    d=input("ingrese la division: ")
    i= int(input("ingrese las inasistencias"))
    al= Alumno(n,a,d,i)
    print("Datos de alumnoTest; ")
    print("{} {} {} {}".format( al.getNomb(), al.getAño(), al.getDiv(), al.getInas()))
    print("Datos de clase Alumno: ")
    print("Cantidad maxima de inasistencias: {}".format(Alumno.getcdadMasInas()))
    cdadNueva= int(input("ingrese la nueva cantidad de inasistencias: "))
    Alumno.setcdadMaxInas(cdadNueva)
    print("Cantidad maxima inasistencias{}".format( Alumno.getcdadMasInas()))
    os.system("pause")
    os.system("cls")

if __name__ == "__main__":
    testing=int(input("Desea invocar test()? 1 para si, 0 para no:"))
    if testing==1:
        test()
listaAlumnos=[]
archivo = open("Asis.csv")
iterador = reader(archivo, delimiter=',')
for fila in iterador:
    alumno=Alumno(fila[0], int(fila[1]), fila[2], int(fila[3]))
    listaAlumnos.append(alumno)
opc = 0
menu= Menu()
while opc != 3:
    print ("Menu de opciones")
    print("Seleccione la opcion deseada")
    print("1. Mostrar  porcentaje de inasitencias maximas por año y division dados")
    print("2. modificar cantidad maxima de inasistencias permitidas")
    print("3. salir")
    opc= int(input())
    menu.opcion(opc,listaAlumnos)
    os.system("pause")
    os.system("cls")

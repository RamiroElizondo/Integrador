import csv 
import numpy
from ClaseCama import Cama
from Integrador.ClaseMedicamento import Medicamento


class ManejadorCama:
    __listaobjetos: Medicamento

    def __init__(self):
        with open("Integrador\medicamentos.csv", 'r') as archivo:
            lista: list[Cama] = []
            reader = csv.reader(archivo,delimiter=';')
            next(reader,None)
            for linea in reader:
                print(linea)
                objeto = Cama(int(linea[0]),int(linea[1]),bool(linea[2]),linea[3],linea[4],linea[5],linea[6])
                lista.append(objeto)
            self.__listaobjetos = numpy.array(lista,dtype=Cama)
    
    def buscarMostrar(self, nombre, fecha):
        i = 0
        while  i < len(self.__listaobjetos) and nombre != self.__listaobjetos[i].getnya():
            i += 1
        else:
            if len(self.__listaobjetos):
                self.__listaobjetos[i].setFechaAlta(fecha)
                self.__listaobjetos[i].mostrarPaciente()
            else: 
                print('Paciente no encontrado'.center(30, '-'))




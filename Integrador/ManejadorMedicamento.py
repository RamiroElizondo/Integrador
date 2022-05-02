import csv
from ClaseMedicamento import Medicamento


class ManejadorMedicamento:
    __listaobjetos: list[Medicamento]
    def __init__(self):
        self.__listaobjetos = []

    def CargaM(self):
        with open("Integrador\medicamentos.csv", 'r') as archivo:
            reader = csv.reader(archivo,delimiter=(';'))
            next(reader,None)
            for linea in reader:
                objeto = Medicamento(int(linea[0]),int(linea[1]),str(linea[2]),str(linea[3]),str(linea[4]),str(linea[5]),int(linea[6]))
                self.__listaobjetos.append(objeto)
    
    def mostrar(self):
        for objeto in self.__listaobjetos:
            print('Medicamento/Monodroga \t\tPresentacion \t\tCantidad \t\tPrecio')
            print('%s %5s %5s %5d %5d'% objeto.getMedicamento(), objeto.getMonodroga(), objeto.getPresentacion(), objeto.getCantidad(), objeto.getPrecio())

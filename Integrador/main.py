from ManejadorCama import ManejadorCama
from ManejadorMedicamento import ManejadorMedicamento


if __name__ == '__main__':
    manejadorC = ManejadorCama()
    manejadorM = ManejadorMedicamento()
    manejadorC.CargaC()
    manejadorM.CargaM()
    nombre = input('Ingrse Nombre Y Apellido de un paciente: ')
    fechaA = input('Ingrese Fecha de Alta: ')
    manejadorC.buscarMostrar(nombre, fechaA)

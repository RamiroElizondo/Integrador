class Medicamento:
    __idCama:int = 0
    __idMedicamento:int = 0
    __nombreM:str = ""
    __monodroga:str = ""
    __presentacion:str = ""
    __cantidadAplicada:str = ""
    __precioTotal:int = ""

    def __init__(self, idCama:int, idMedicamento:int, nombreC:str, monodroga:str, presentacion:str, cantidadAplicada:str, precioTotal:int):
        self.__idCama = idCama
        self.__idMedicamento = idMedicamento
        self.__nombreC = nombreC
        self.__monodroga = monodroga
        self.__presentacion = presentacion
        self.__cantidadAplicada = cantidadAplicada
        self.__precioTotal = precioTotal

    def getMedicamento(self):
        return self.__nombreM
    
    def getMonodroga(self):
        return self.__monodroga

    def getPresentacion(self):
        return self.__presentacion
    
    def getCantidad(self):
        return self.__cantidadAplicada
    
    def getPrecio(self):
        return self.__precioTotal
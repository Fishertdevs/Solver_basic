class File():
    def __init__(self) -> None:
        self.__RUTA='Estados/matrices.txt'
    
    def traerNodos(self)->list:
        datos=[]
        try:
            with open(self.__RUTA,"r") as fr:
                aux=fr.readlines()
                for x in aux:
                    datos.append(x.replace('\n','').split(':'))
        except FileNotFoundError as e:
            print(f'Error al traer arvhivo: {e}')
        return datos
import nodo

class ASC():

    def __init__(self,inicial,final) -> None:
        self.nodoInicial=inicial
        self.nodoMeta=final
        self.abierto=[]
        self.cerrado=[]

    def pintar(self, tablero)->None:
        for i in tablero:print(i[0], " ", i[1], " ", i[2])

    def actualizarPesos(self, lista, pp)->list:
        for i in lista:i.peso = pp + i.prof + i.peso
        return lista
    
    def busqueda(self)->None:
        nodosGenerados=0
        self.abierto.append(nodo.Nodo(self.nodoInicial,None,0,'Inicio',0))
        actual=self.abierto[0]
        while len(self.abierto)>0 and actual.estado!=self.nodoMeta:
            actual=self.abierto.pop(0)
            print("Regla aplicada: ", actual.regla)
            print("Peso: ", actual.peso)
            self.pintar(actual.estado)
            if actual not in self.cerrado:
                self.cerrado.append(actual)
                sucesores=actual.hallarSucesores(actual,self.nodoMeta)
                sucesores=self.actualizarPesos(sucesores,actual.peso)
                metaInSucesores=False
                nSuc=len(sucesores)
                nodosGenerados+=nSuc
                for i in sucesores:
                    if i.estado==self.nodoMeta:
                        metaInSucesores=True
                        actual=i
                        print("Regla aplicada: ", actual.regla)
                        print("Peso: ", actual.peso)
                        self.pintar(actual.estado)
                if nSuc>0 and not metaInSucesores:
                    sorted(sucesores,key=lambda x:x.peso)
                    self.abierto=sucesores+self.abierto
        print("---------------------------------")
        print("La cantidad de nodos generados es: ", nodosGenerados)
        if actual.estado==self.nodoMeta:
            print("Se ha encontrado la solucion y es: ")
            sol = []
            while actual.padre != None:
                sol.insert(0, actual)
                actual = actual.padre
            for i in range(len(sol)):
                print("Mover a ", sol[i].regla)
                self.pintar(sol[i].estado)
        else:print("No se encontro la solucion")
        
        # Calcular y mostrar distancia Manhattan al objetivo
        nodo_helper = nodo.Nodo(None, None, 0, None, 0)
        distancia_manhattan = nodo_helper.calcularHeuristica(actual.estado, self.nodoMeta)
        print(f"Distancia Manhattan al objetivo: {distancia_manhattan}")

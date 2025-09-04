import nodo


class BPP:
    def __init__(self, inicial, final, profundidad):
        self.nodoInicial = inicial
        self.nodoMeta = final
        self.nProf = profundidad
        self.abierto = []
        self.cerrado = []

    def pintar(self, tablero):
        for i in range(3):
            print(tablero[i][0], " ", tablero[i][1], " ", tablero[i][2])

    def busqueda(self):
        nodosGenerados = 0
        self.abierto.append(nodo.Nodo(self.nodoInicial, None, 0, "Inicio",0))
        actual = self.abierto[0]
        while len(self.abierto) != 0 and actual.estado != self.nodoMeta:
            actual = self.abierto.pop(0)
            print("Regla aplicada: ", actual.regla)
            print("Nivel: ", actual.prof)
            self.pintar(actual.estado)
            if (actual not in self.cerrado) and actual.prof < self.nProf:
                self.cerrado.append(actual)
                sucesores = actual.hallarSucesores(actual,self.nodoMeta)
                metaInSucesores = False
                nSuc = len(sucesores)
                nodosGenerados += nSuc
                for i in range(nSuc):
                    if sucesores[i].estado == self.nodoMeta:
                        metaInSucesores = True
                        actual = sucesores[i]
                        print("Regla aplicada: ", actual.regla)
                        print("Nivel: ", actual.prof)
                        self.pintar(actual.estado)
                if nSuc != 0 and not metaInSucesores:
                    for k in range(nSuc - 1, -1, -1):
                        self.abierto.insert(0, sucesores[k])
        print("---------------------------------")
        print("La cantidad de nodos generados es: ", nodosGenerados)
        if actual.estado == self.nodoMeta:
            print("Se ha encontrado la solucion y es: ")
            sol = []
            while actual.padre != None:
                sol.insert(0, actual)
                actual = actual.padre
            for i in range(len(sol)):
                print("Mover a ", sol[i].regla)
                self.pintar(sol[i].estado)
        else:
            print("No se encontro la solucion")
        
        # Calcular y mostrar distancia Manhattan al objetivo
        nodo_helper = nodo.Nodo(None, None, 0, None, 0)
        distancia_manhattan = nodo_helper.calcularHeuristica(actual.estado, self.nodoMeta)
        print(f"Distancia Manhattan al objetivo: {distancia_manhattan}")

import nodo

class BPA:
    def __init__(self, inicial, final):
        self.nodoInicial = inicial
        self.nodoMeta = final
        self.abierto = []
        self.cerrado = []
    
    def pintar(self, tablero):
        for i in range(3):
            print(tablero[i][0], " ", tablero[i][1], " ", tablero[i][2])
    
    def busqueda(self):
        nodosGenerados = 0
        self.abierto.append(nodo.Nodo(self.nodoInicial, None, 0, "Inicio", 0))
        actual = self.abierto[0]
        
        while len(self.abierto) != 0 and actual.estado != self.nodoMeta:
            actual = self.abierto.pop(0)  # Se extrae el primer nodo (FIFO)
            print("Regla aplicada: ", actual.regla)
            print("Nivel: ", actual.prof)
            self.pintar(actual.estado)
            
            if actual not in self.cerrado:
                self.cerrado.append(actual)
                sucesores = actual.hallarSucesores(actual, self.nodoMeta)
                nodosGenerados += len(sucesores)
                
                for sucesor in sucesores:
                    if sucesor.estado == self.nodoMeta:
                        actual = sucesor
                        print("Regla aplicada: ", actual.regla)
                        print("Nivel: ", actual.prof)
                        self.pintar(actual.estado)
                        break  # Se encontró la meta
                    self.abierto.append(sucesor)  # Se agregan al final (cola FIFO)
        
        print("---------------------------------")
        print("La cantidad de nodos generados es: ", nodosGenerados)
        
        if actual.estado == self.nodoMeta:
            print("Se ha encontrado la solución y es: ")
            sol = []
            while actual.padre is not None:
                sol.insert(0, actual)
                actual = actual.padre
            for paso in sol:
                print("Mover a ", paso.regla)
                self.pintar(paso.estado)
        else:
            print("No se encontró la solución")
        
        # Calcular y mostrar distancia Manhattan al objetivo
        nodo_helper = nodo.Nodo(None, None, 0, None, 0)
        distancia_manhattan = nodo_helper.calcularHeuristica(actual.estado, self.nodoMeta)
        print(f"Distancia Manhattan al objetivo: {distancia_manhattan}")
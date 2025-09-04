import copy


class Nodo:
    def __init__(self, estado, padre, profundidad, regla, peso):
        self.estado = estado
        self.padre = padre
        self.prof = profundidad
        self.regla = regla
        self.peso = peso

    def buscaPosicion(self, tablero, val):
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == val:
                    return i, j
        return None, None

    def estaEnPadre(self, nodito):
        esta = False
        aux = nodito.padre
        while aux.padre != None:
            if nodito.estado == aux.estado:
                esta = True
            aux = aux.padre
        return esta

    def calcularHeuristica(self,nodo,meta):
        h=0
        for ficha in range(9):
            i,j = self.buscaPosicion(nodo,ficha)
            x,y = self.buscaPosicion(meta,ficha)
            if i is not None and j is not None and x is not None and y is not None:
                htmp = abs(i-x)+abs(j-y)
                h+=htmp
        return h
    
    ##Reglas 1->Derecha 2->Izquierda 3->Arriba 4->Abajo
    def moverA(self, nodoPadre):
        movimientos = []
        i, j = self.buscaPosicion(nodoPadre.estado, 0)
        if i is None or j is None:
            return []
        if j != 2:
            nodoHijo = copy.deepcopy(nodoPadre)
            nodoHijo.estado[i][j] = nodoHijo.estado[i][j + 1]
            nodoHijo.estado[i][j + 1] = 0
            nodoHijo.padre = nodoPadre
            nodoHijo.prof = nodoPadre.prof + 1
            nodoHijo.regla = "Derecha"
            if not self.estaEnPadre(nodoHijo):
                movimientos.append(nodoHijo)
        if j != 0:
            nodoHijo = copy.deepcopy(nodoPadre)
            nodoHijo.estado[i][j] = nodoHijo.estado[i][j - 1]
            nodoHijo.estado[i][j - 1] = 0
            nodoHijo.padre = nodoPadre
            nodoHijo.prof = nodoPadre.prof + 1
            nodoHijo.regla = "Izquierda"
            if not self.estaEnPadre(nodoHijo):
                movimientos.append(nodoHijo)
        if i != 0:
            nodoHijo = copy.deepcopy(nodoPadre)
            nodoHijo.estado[i][j] = nodoHijo.estado[i - 1][j]
            nodoHijo.estado[i - 1][j] = 0
            nodoHijo.padre = nodoPadre
            nodoHijo.prof = nodoPadre.prof + 1
            nodoHijo.regla = "Arriba"
            if not self.estaEnPadre(nodoHijo):
                movimientos.append(nodoHijo)
        if i != 2:
            nodoHijo = copy.deepcopy(nodoPadre)
            nodoHijo.estado[i][j] = nodoHijo.estado[i + 1][j]
            nodoHijo.estado[i + 1][j] = 0
            nodoHijo.padre = nodoPadre
            nodoHijo.prof = nodoPadre.prof + 1
            nodoHijo.regla = "Abajo"
            if not self.estaEnPadre(nodoHijo):
                movimientos.append(nodoHijo)
        return movimientos

    def hallarSucesores(self, nodoPadre,nodoMeta):
        lista = self.moverA(nodoPadre)
        for i in range(len(lista)):
            lista[i].peso=self.calcularHeuristica(lista[i].estado,nodoMeta)
        return lista

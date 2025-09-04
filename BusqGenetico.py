import random
import copy
import nodo

class AG:
    def __init__(self, inicial, final):
        self.nodoInicial = inicial
        self.nodoMeta = final
        self.poblacion_size = 100
        self.generaciones = 500
        self.tasa_mutacion = 0.1
        self.tasa_cruce = 0.8
        
    def pintar(self, tablero):
        for i in range(3):
            print(tablero[i][0], " ", tablero[i][1], " ", tablero[i][2])
    
    def generar_individuo_aleatorio(self):
        """Genera un estado aleatorio del puzzle"""
        numeros = list(range(9))
        random.shuffle(numeros)
        individuo = []
        for i in range(3):
            fila = []
            for j in range(3):
                fila.append(numeros[i*3 + j])
            individuo.append(fila)
        return individuo
    
    def fitness(self, individuo):
        """Calcula el fitness usando la distancia Manhattan inversa"""
        nodo_helper = nodo.Nodo(None, None, 0, None, 0)
        distancia = nodo_helper.calcularHeuristica(individuo, self.nodoMeta)
        # Invertir la distancia para que menor distancia = mayor fitness
        return 1.0 / (1.0 + distancia)
    
    def seleccion_torneo(self, poblacion, fitness_values):
        """Selección por torneo de tamaño 3"""
        torneo_size = 3
        mejor_individuo = None
        mejor_fitness = -1
        
        for _ in range(torneo_size):
            idx = random.randint(0, len(poblacion) - 1)
            if fitness_values[idx] > mejor_fitness:
                mejor_fitness = fitness_values[idx]
                mejor_individuo = copy.deepcopy(poblacion[idx])
        
        return mejor_individuo
    
    def cruce_pmx(self, padre1, padre2):
        """Cruce PMX (Partially Matched Crossover) adaptado para 8-puzzle"""
        # Convertir matrices a listas planas
        p1_flat = [item for fila in padre1 for item in fila]
        p2_flat = [item for fila in padre2 for item in fila]
        
        # Puntos de cruce aleatorios
        punto1 = random.randint(0, 7)
        punto2 = random.randint(punto1 + 1, 8)
        
        # Crear hijos
        hijo1 = [-1] * 9
        hijo2 = [-1] * 9
        
        # Copiar segmento entre puntos de cruce
        for i in range(punto1, punto2 + 1):
            hijo1[i] = p2_flat[i]
            hijo2[i] = p1_flat[i]
        
        # Llenar el resto evitando duplicados
        for i in range(9):
            if i < punto1 or i > punto2:
                # Para hijo1
                valor = p1_flat[i]
                while valor in hijo1:
                    idx = p2_flat.index(valor)
                    if punto1 <= idx <= punto2:
                        valor = p1_flat[idx]
                    else:
                        break
                hijo1[i] = valor
                
                # Para hijo2
                valor = p2_flat[i]
                while valor in hijo2:
                    idx = p1_flat.index(valor)
                    if punto1 <= idx <= punto2:
                        valor = p2_flat[idx]
                    else:
                        break
                hijo2[i] = valor
        
        # Convertir de vuelta a matrices 3x3
        def lista_a_matriz(lista):
            matriz = []
            for i in range(3):
                fila = []
                for j in range(3):
                    fila.append(lista[i*3 + j])
                matriz.append(fila)
            return matriz
        
        return lista_a_matriz(hijo1), lista_a_matriz(hijo2)
    
    def mutacion_intercambio(self, individuo):
        """Mutación por intercambio de dos posiciones aleatorias"""
        if random.random() < self.tasa_mutacion:
            # Seleccionar dos posiciones aleatorias
            pos1_i, pos1_j = random.randint(0, 2), random.randint(0, 2)
            pos2_i, pos2_j = random.randint(0, 2), random.randint(0, 2)
            
            # Intercambiar valores
            individuo[pos1_i][pos1_j], individuo[pos2_i][pos2_j] = \
                individuo[pos2_i][pos2_j], individuo[pos1_i][pos1_j]
        
        return individuo
    
    def es_solucion(self, individuo):
        """Verifica si el individuo es la solución"""
        for i in range(3):
            for j in range(3):
                if individuo[i][j] != self.nodoMeta[i][j]:
                    return False
        return True
    
    def busqueda(self):
        print("Iniciando Algoritmo Genético...")
        print("Parámetros:")
        print(f"- Tamaño de población: {self.poblacion_size}")
        print(f"- Generaciones máximas: {self.generaciones}")
        print(f"- Tasa de mutación: {self.tasa_mutacion}")
        print(f"- Tasa de cruce: {self.tasa_cruce}")
        print()
        
        # Inicializar población
        poblacion = []
        
        # Agregar el estado inicial
        poblacion.append(copy.deepcopy(self.nodoInicial))
        
        # Generar resto de la población aleatoriamente
        for _ in range(self.poblacion_size - 1):
            poblacion.append(self.generar_individuo_aleatorio())
        
        mejor_fitness_global = -1
        mejor_individuo_global = None
        generaciones_sin_mejora = 0
        
        for generacion in range(self.generaciones):
            # Calcular fitness de toda la población
            fitness_values = []
            for individuo in poblacion:
                fitness_val = self.fitness(individuo)
                fitness_values.append(fitness_val)
                
                # Verificar si es solución
                if self.es_solucion(individuo):
                    print(f"¡SOLUCIÓN ENCONTRADA EN GENERACIÓN {generacion}!")
                    print("Estado final encontrado:")
                    self.pintar(individuo)
                    print(f"Fitness: {fitness_val:.6f}")
                    return
                
                # Actualizar mejor global
                if fitness_val > mejor_fitness_global:
                    mejor_fitness_global = fitness_val
                    mejor_individuo_global = copy.deepcopy(individuo)
                    generaciones_sin_mejora = 0
                else:
                    generaciones_sin_mejora += 1
            
            # Mostrar progreso cada 50 generaciones
            if generacion % 50 == 0:
                promedio_fitness = sum(fitness_values) / len(fitness_values)
                print(f"Generación {generacion}: Mejor fitness = {mejor_fitness_global:.6f}, Promedio = {promedio_fitness:.6f}")
                print("Mejor individuo actual:")
                self.pintar(mejor_individuo_global)
                print()
            
            # Parada temprana si no hay mejora en 100 generaciones
            if generaciones_sin_mejora > 100:
                print(f"Parada temprana en generación {generacion} (sin mejora en 100 generaciones)")
                break
            
            # Crear nueva población
            nueva_poblacion = []
            
            # Elitismo: mantener el mejor individuo
            nueva_poblacion.append(copy.deepcopy(mejor_individuo_global))
            
            # Generar resto de la población
            while len(nueva_poblacion) < self.poblacion_size:
                # Selección
                padre1 = self.seleccion_torneo(poblacion, fitness_values)
                padre2 = self.seleccion_torneo(poblacion, fitness_values)
                
                # Cruce
                if random.random() < self.tasa_cruce:
                    try:
                        hijo1, hijo2 = self.cruce_pmx(padre1, padre2)
                    except:
                        # Si falla el cruce, usar padres originales
                        hijo1, hijo2 = copy.deepcopy(padre1), copy.deepcopy(padre2)
                else:
                    hijo1, hijo2 = copy.deepcopy(padre1), copy.deepcopy(padre2)
                
                # Mutación
                hijo1 = self.mutacion_intercambio(hijo1)
                hijo2 = self.mutacion_intercambio(hijo2)
                
                # Agregar a nueva población
                nueva_poblacion.append(hijo1)
                if len(nueva_poblacion) < self.poblacion_size:
                    nueva_poblacion.append(hijo2)
            
            poblacion = nueva_poblacion
        
        # Si no se encontró solución exacta, mostrar la mejor aproximación
        print(f"No se encontró solución exacta en {self.generaciones} generaciones.")
        print(f"Mejor fitness alcanzado: {mejor_fitness_global:.6f}")
        print("Mejor aproximación encontrada:")
        self.pintar(mejor_individuo_global)
        
        nodo_helper = nodo.Nodo(None, None, 0, None, 0)
        distancia_final = nodo_helper.calcularHeuristica(mejor_individuo_global, self.nodoMeta)
        print(f"Distancia Manhattan al objetivo: {distancia_final}")
from os import system
import BusqAmplitud
import BusqProfundidad
import AscColina
import BusqAAsterisco
import BusqGenetico
import Archivos

class Main():
    def __init__(self) -> None:
        self.def_Nodos()
        self.menu()


    def def_Nodos(self)->None:
        self.__ESTINICIAL=[]
        self.__ESTFINAL=[]
        aux=Archivos.File().traerNodos()
        for i in aux:
            if i[0].lower()=='inicial':
                for j in i[1].split(','):self.__ESTINICIAL.append(list(map(lambda x:int(x),j.split(' '))))
            elif i[0].lower()=='final':
                for j in i[1].split(','):self.__ESTFINAL.append(list(map(lambda x:int(x),j.split(' '))))
        self.__ESTINICIAL=tuple(self.__ESTINICIAL)
        self.__ESTFINAL=tuple(self.__ESTFINAL)

    def pintar(self,tablero)->None:
        for i in range(3):
            print(tablero[i][0], " ", tablero[i][1], " ", tablero[i][2])


    def menu(self)->None:
        con = True
        while con:
            ##try:
                print("----------------------------------")
                print("--------- MENU PRINCIPAL ---------")
                print("----------------------------------")
                print("Estado Inicial: ")
                self.pintar(self.__ESTINICIAL)
                print("Estado Final: ")
                self.pintar(self.__ESTFINAL)
                print("1: Cambiar Estado Inicial")
                print("2: Cambiar Estado Final")
                print("3: Busqueda en Amplitud")
                print("4: Busqueda por Profundidad")
                print("5: Ascenso Colina")
                print("6: A*")
                print("7: Algoritmo Genético")
                print("0: Terminar")
                opc = int(input("Elija una opcion: "))
                if opc == 1:
                    for i in range(3):
                        for j in range(3):
                            self.__ESTINICIAL[i][j] = 0
                    for i in range(3):
                        for j in range(3):
                            print("Numero en posicion ", i, ",", j, ": ")
                            self.__ESTINICIAL[i][j] = int(input("-> "))
                            self.pintar(self.__ESTINICIAL)
                    system("cls")
                elif opc == 2:
                    for i in range(3):
                        for j in range(3):
                            self.__ESTFINAL[i][j] = 0
                    for i in range(3):
                        for j in range(3):
                            print("Numero en posicion ", i, ",", j, ": ")
                            self.__ESTFINAL[i][j] = int(input("-> "))
                            self.pintar(self.__ESTFINAL)
                    system("cls")
                elif opc == 3:
                    if self.__ESTINICIAL!=self.__ESTFINAL:
                        system("cls")
                        print("--- BUSQUEDA EN AMPLITUD ---")
                        x=BusqAmplitud.BPA(self.__ESTINICIAL,self.__ESTFINAL)
                        x.busqueda()
                    else:
                        print("¡El estado inicial es igual al estado meta!")
                elif opc == 4:
                    if self.__ESTINICIAL!=self.__ESTFINAL:
                        system("cls")
                        print("--- BUSQUEDA PROFUNDIDAD ---")
                        pro=int(input("Digite el nivel de profundidad: "))
                        x=BusqProfundidad.BPP(self.__ESTINICIAL,self.__ESTFINAL,pro)
                        x.busqueda()
                    else:
                        print("¡El estado inicial es igual al estado meta!")
                elif opc == 5:
                    if self.__ESTINICIAL!=self.__ESTFINAL:
                        system("cls")
                        print("--- ASCENSO COLINA ---")
                        AscColina.ASC(self.__ESTINICIAL,self.__ESTFINAL).busqueda()
                    else:
                        print("¡El estado inicial es igual al estado meta!")
                elif opc == 6:
                    if self.__ESTFINAL!=self.__ESTINICIAL:
                        system("cls")
                        print("--- A* ---")
                        z=BusqAAsterisco.AA(self.__ESTINICIAL,self.__ESTFINAL)
                        z.busqueda()
                    else:
                        print("¡El estado inicial es igual al estado meta!")
                elif opc == 7:
                    if self.__ESTFINAL!=self.__ESTINICIAL:
                        system("cls")
                        print("--- ALGORITMO GENÉTICO ---")
                        ag=BusqGenetico.AG(self.__ESTINICIAL,self.__ESTFINAL)
                        ag.busqueda()
                    else:
                        print("¡El estado inicial es igual al estado meta!")
                elif opc == 0:
                    con = False
                else:
                    print("Opcion Incorrecta, intente de nuevo")
        print("¡¡¡ APLICACION FINALIZADA !!!")

if __name__=='__main__':
    Main()

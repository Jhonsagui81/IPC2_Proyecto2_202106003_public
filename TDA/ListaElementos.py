from TDA.Nodo import NodoElementos
from tkinter import messagebox as MessageBox

class ListaElementos:
    def __init__(self):
        self.Inicio = None
        self.Final = None 
        self.Limite = 0
    
    def IncertarElemento(self, numero_atomico, simbolo, nombre):
        NuevoNodo = NodoElementos(numero_atomico,simbolo,nombre,)
        if self.Inicio == None:
            self.Inicio = NuevoNodo
            self.Final = NuevoNodo
            print("Elemento asignador exitoso ")
            self.Limite += 1
        else:
            Actual = self.Inicio
            bandera = False
            while Actual != None:
                if NuevoNodo.ObtenerNombre().lower() == Actual.ObtenerNombre().lower() or NuevoNodo.Obtner_Atomico() == Actual.Obtner_Atomico() or NuevoNodo.ObtenerSimbolo()  == Actual.ObtenerSimbolo():
                    MessageBox.showinfo("Alerta","EL elemento ya existe, No se guardara")
                    bandera = True
                    Actual = Actual.Siguiente
                else:
                    Actual = Actual.Siguiente
            if bandera == False:
                self.Limite += 1
                self.Final.AsignarSiguiente(NuevoNodo)
                self.Final = NuevoNodo
                print("Elemento aisgnado exitodo else")

    def Existe(self, elemento):
        Aux = self.Inicio
        while Aux != None:
            if Aux.ObtenerSimbolo() == elemento:
                return True
            else:
                Aux = Aux.Siguiente
        return False

    def OrdenarElementos(self):
        Bandera = True
        numero = 1
        while Bandera:
            Actual = self.Inicio
            Anterior = None
            Bandera = False
            numero += 1
            while Actual != None:
                if Actual.Siguiente != None:
                    if Actual.Obtner_Atomico() > Actual.Siguiente.Obtner_Atomico():
                        #Si entramos acá, quiere decir que el siguiente nodo es menor al actual
                        Bandera = True
                        if Actual == self.Inicio:
                            #Si entramos acá quiere decir que el elemento desordenado es el primero
                            self.Inicio = Actual.Siguiente
                            Actual.Siguiente = self.Inicio.Siguiente
                            self.Inicio.Siguiente = Actual
                        else:
                            #Si entramos acá quiere decir que el elemento desordenado no es el primero
                            Anterior.Siguiente = Actual.Siguiente
                            Actual.Siguiente = Actual.Siguiente.Siguiente
                            Anterior.Siguiente.Siguiente = Actual
                Anterior = Actual
                Actual = Actual.Siguiente

    def Impimir(self):
        Retorno = "NO.ATOMICO"+"\t\t\t"+"SIMBOLO"+"\t\t\t"+"ELEMENTO"+"\n\n"
        if self.Inicio == None:
            return "La lista está vacía."
        Auxiliar = self.Inicio
        while Auxiliar != None:
            Retorno += str(Auxiliar.Obtner_Atomico())+"\t\t\t"+str(Auxiliar.ObtenerSimbolo())+"\t\t\t"+str(Auxiliar.ObtenerNombre())+"\n"
            if Auxiliar.Siguiente != None:
                Retorno += "\n"
            Auxiliar = Auxiliar.Siguiente
        return Retorno

    def NoAtomico(self, simbolo):
        Aux = self.Inicio
        while Aux != None:
            if Aux.ObtenerSimbolo() == simbolo:
                return Aux.Obtner_Atomico()
            Aux = Aux.Siguiente
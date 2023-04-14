from TDA.Nodo import *

class trabajo:
    def __init__(self):
        self.Inicio = None
        self.Final = None

    def Insertar(self, id, lista_elementos):
        NuevoNodo = NodoTrabajo(id,lista_elementos)
        if self.Inicio == None:
            self.Inicio = NuevoNodo
            self.Final = NuevoNodo

        else:
            self.Final.AsignarSiguiente(NuevoNodo)
            self.Final = NuevoNodo

    def buscarPin(self, simbolo):
        Auxiliar = self.Inicio
        cont_listas = 0
        while Auxiliar != None:
            cont_listas += 1
            if Auxiliar.ObtenerListaElementos().buscarELemetoPorPin1(simbolo):
                return cont_listas
            Auxiliar = Auxiliar.Siguiente

    def Impimir(self):
        Auxiliar = self.Inicio
        print("listas trabajo almacenadas:")
        while Auxiliar != None:
            s = Auxiliar.ObtenerListaElementos().Impimir()
            print(s)
            Auxiliar = Auxiliar.Siguiente

    def ObtenerLista(self):
        Aux = self.Inicio
        while Aux != None:
            pass

    def ClonarLista(self):
        clon_trabajo = trabajo()
        Auxiliar = self.Inicio
        while Auxiliar != None:
            clon_trabajo.Insertar(1 , Auxiliar.ObtenerListaElementos())
            Auxiliar = Auxiliar.Siguiente
        return clon_trabajo

    def EliminarNodoInicio(self, pin):
        contador = 0
        Aux = self.Inicio
        while Aux != None:
            contador += 1
            if contador == pin:
                Aux.ObtenerListaElementos().eliminarNodoInicio()
                break
            Aux = Aux.Siguiente

    def ElementoInicialXPin(self, pin):
        Contador = 0
        Aux = self.Inicio
        while Aux != None:
            Contador += 1
            if Contador == pin:
                return Aux.ObtenerListaElementos().PrimerNodo()
            Aux = Aux.Siguiente

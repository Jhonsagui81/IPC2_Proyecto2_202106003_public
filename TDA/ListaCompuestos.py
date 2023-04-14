from TDA.Nodo import NodoCompuestos
from tkinter import messagebox as MessageBox

class ListaCompuestos:
    def __init__(self):
        self.Inicio = None
        self.Final = None 
        self.Limite = 0
    
    def Insertar(self, nombre, lista_elementos):
        if lista_elementos.Estado():
            NuevoNodo = NodoCompuestos(nombre, lista_elementos)
            if self.Inicio == None:
                self.Inicio = NuevoNodo
                self.Final = NuevoNodo
                self.Limite +=1
                print("ASIGNO COMPUESTO if")
            else:
                Actual = self.Inicio
                bandera = False
                while Actual != None:
                    if NuevoNodo.ObtenerNOmbre == Actual.ObtenerNOmbre():
                        MessageBox.showinfo("Alerta","EL compuesto ya existe, No se guardara")
                        bandera = True
                        Actual = Actual.Siguiente
                    else:
                        Actual = Actual.Siguiente
                if bandera == False:
                    self.Limite += 1
                    self.Final.AsignarSiguiente(NuevoNodo)
                    self.Final = NuevoNodo
                    print("Elemento aisgnado exitodo else")
        else:
            MessageBox.showinfo("ERROR","Compuesto con problema NO FUE ALMACENADO")

    def CompuestooLista(self):
        Retorno = "COMPUESTO"+"\t\t\t\t\t"+"FORMULA"+"\n\n"
        if self.Inicio == None:
            return "La lista está vacía."
        Auxiliar = self.Inicio
        while Auxiliar != None:
            texto = Auxiliar.ObtenerListaElementos().ElementosCompuesto()
            Retorno += str(Auxiliar.ObtenerNOmbre())+"\t\t\t\t\t"+str(texto)
            if Auxiliar.Siguiente != None:
                Retorno += "\n"
            Auxiliar = Auxiliar.Siguiente
        
        return Retorno

    def Compuestos(self):
        Texto = ""
        Auxiliar = self.Inicio
        while Auxiliar != None:
            Texto += str(Auxiliar.ObtenerNOmbre())+","
            Auxiliar = Auxiliar.Siguiente
        
        return Texto[0:-1]

    def BuscarCompuesto(self, name):
        Auxiliar = self.Inicio
        while Auxiliar != None:
            if name == Auxiliar.ObtenerNOmbre():
                cadenaElementos = Auxiliar.ObtenerListaElementos()
                return cadenaElementos
            Auxiliar = Auxiliar.Siguiente

    def CantidadCOmpuestos(self):
        return self.Limite

    def CompuestoIndice(self, id):
        Auxiliar = self.Inicio
        cont = 0
        while Auxiliar != None:
            cont += 1
            if cont == id:
                return Auxiliar.ObtenerNOmbre()
            Auxiliar = Auxiliar.Siguiente
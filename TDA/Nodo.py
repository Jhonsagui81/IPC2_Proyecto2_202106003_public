from TDA.Data import *

class NodoElementos:
    def __init__(self, numero_atomico, simbolo, nombre):
        self.nuevoNodo = Elementos(numero_atomico, simbolo, nombre)
        self.Siguiente = None
    
    def AsignarSiguiente(self, Nodo):
        self.Siguiente = Nodo
    def Obtner_Atomico(self):
        return self.nuevoNodo.ObtenerAtomico()
    def ObtenerSimbolo(self):
        return self.nuevoNodo.ObtenerSimbolo()
    def ObtenerNombre(self):
        return self.nuevoNodo.ObtenerNombre()
    
class NodoMaquinas:
    def __init__(self, id, nombre, numero_pines, numero_elementos, lista_pines):
        self.Maquina = Maquina(id, nombre, numero_pines, numero_elementos, lista_pines)
        self.Siguiente = None

    def AsignarSiguiente(self, Nodo):
        self.Siguiente = Nodo

    def ObtenerId(self):
        return self.Maquina.ObtenerId()
    
    def ObtenerNombre(self):
        return self.Maquina.ObtenerNombre()
    
    def ObtenerNOPines(self):
        return self.Maquina.ObtenerNumeroPines()
    
    def ObtenerNOElementos(self):
        return self.Maquina.ObtenerNumeroElementos()
    
    def ObtenerListaPines(self):
        return self.Maquina.ObtenerListaPinas()

class NodoPinesElementos:
    def __init__(self, simbolo):
        self.PinElementos = ElementosPin(simbolo)
        self.Siguiente = None
        self.Anterior = None
    
    def AsignarSiguiente(self, Nodo):
        self.Siguiente = Nodo
        
    def ObtenerSimbolo(self):
        return self.PinElementos.ObtenerSimbolo()
    
class NodoCompuestos:
    def __init__(self, nombre, lista_compuestos):
        self.Compuesto = Compuestos(nombre, lista_compuestos)
        self.Siguiente = None
    
    def AsignarSiguiente(self, Nodo):
        self.Siguiente = Nodo

    def ObtenerNOmbre(self):
        return self.Compuesto.ObtenerNombre()
    
    def ObtenerListaElementos(self):
        return self.Compuesto.ObtenerListaElementos()
    
class NodoListaElemtCompuesto:
    def __init__(self, simbolo):
        self.ListaEleCompuesto = ElementosCompuesto(simbolo)
        self.Siguiente = None
    
    def AsignarSiguiente(self, Nodo):
        self.Siguiente = Nodo

    def ObtenerSimbolo(self):
        return self.ListaEleCompuesto.ObtenerSimbolo()

class NodoExtraElemtCompuesto:
    def __init__(self, id, simbolo):
        self.ListaEleExtraCompuesto = ElementosExtraCompuesto(id, simbolo)
        self.Siguiente = None
    
    def AsignarSiguiente(self, Nodo):
        self.Siguiente = Nodo

    def ObtenerSimbolo(self):
        return self.ListaEleExtraCompuesto.ObtenerSimbolo()

    def ObtenerId(self):
        return self.ListaEleExtraCompuesto.ObtenerId()

class NodoPines:
    def __init__(self, id, lista_elementos):
        self.Pin = Pin(id,lista_elementos)
        self.Siguiente = None

    def AsignarSiguiente(self, Nodo):
        self.Siguiente = Nodo

    def ObtenerId(self):
        return self.Pin.ObtenerId()
    
    def ObtenerListaElementos(self):
        return self.Pin.ObtenesListaElementos()

class NodoTrabajo:
    def __init__(self, id, elementos):
        self.trabajo = listaTrabajo(id,elementos)
        self.Siguiente = None

    def AsignarSiguiente(self, Nodo):
        self.Siguiente = Nodo

    def ObtenerId(self):
        return self.trabajo.ObtenerId()
    
    def ObtenerListaElementos(self):
        return self.trabajo.ObtenesListaElementos()

class NodoInstrucciones:
    def __init__(self, EstadoActual, pin, posicionX, Accion, simbolo, grafico):
        self.Instruccion = Instruccion(EstadoActual,pin,posicionX, Accion, simbolo, grafico)
        self.Siguiente = None

    def AsignarSiguiente(self, nodo):
        self.Siguiente = nodo
    def ObtenerEstadoActual(self):
        return self.Instruccion.ObtenerEstadoActual()
    def ObtenerPin(self):
        return self.Instruccion.ObtenerPin()
    def ObtenerPosicion(self):
        return self.Instruccion.ObtenerPosicioX()
    def ObtenerAccion(self):
        return self.Instruccion.ObtenerAccion()
    def ObtenerSimbol(self):
        return self.Instruccion.ObtenerSimbolo()
    def ObtenerGrafico(self):
        return self.Instruccion.ObtenerGrafico()

class NodoDesglozado:
    def __init__(self, maquina, lista_pin):
        self.InstrucionesDesglozadas = IntruccionesDesglozadas(maquina, lista_pin)
        self.Siguiente = None

    def AsignarSiguiente(self, Nodo):
        self.Siguiente = Nodo
    def ObtenerNombreMaquina(self):
        return self.InstrucionesDesglozadas.ObtenerNOmbreMaquina()
    def ObtenerLista_pines(self):
        return self.InstrucionesDesglozadas.ObtenerListaPin()
        
class Elementos:
    def __init__(self, numero_atomico, simbolo, nombre):
        self.numero_atomico = numero_atomico
        self.simbolo = simbolo
        self.nombre = nombre
    
    def ObtenerAtomico(self):
        return self.numero_atomico
    def ObtenerSimbolo(self):
        return self.simbolo
    def ObtenerNombre(self):
        return self.nombre

class Maquina:
    def __init__(self, id, nombre, numero_pines, numero_elementos, lista_pines):
        self.id = id 
        self.nombre = nombre 
        self.numero_pines = numero_pines
        self.numero_elementos = numero_elementos
        self.lista_pines = lista_pines
        
    def ObtenerId(self):
        return self.id 
    def ObtenerNombre(self):
        return self.nombre
    def ObtenerNumeroPines(self):
        return self.numero_pines
    def ObtenerNumeroElementos(self):
        return self.numero_elementos
    def ObtenerListaPinas(self):
        return self.lista_pines


class ElementosPin:
    def __init__(self, simbolo):
        self.simbolo = simbolo 

    def ObtenerSimbolo(self):
        return self.simbolo

class Compuestos:
    def __init__(self, nombre, lista_elementos):
        self.nombre = nombre
        self.lista_elementos = lista_elementos

    def ObtenerNombre(self):
        return self.nombre
    def ObtenerListaElementos(self):
        return self.lista_elementos

class ElementosCompuesto:
    def __init__(self, simbolo):
        self.simbolo = simbolo

    def ObtenerSimbolo(self):
        return self.simbolo

class ElementosExtraCompuesto:
    def __init__(self, id, simbolo):
        self.simbolo = simbolo
        self.id = id

    def ObtenerSimbolo(self):
        return self.simbolo

    def ObtenerId(self):
        return self.id

class Pin:
    def __init__(self, id, lista_elementos):
        self.id = id 
        self.lista_elementos = lista_elementos

    def ObtenerId(self):
        return self.id
    def ObtenesListaElementos(self):
        return self.lista_elementos

class listaTrabajo:
    def __init__(self, id, elemento):
        self.id = id 
        self.elemento = elemento

    def ObtenerId(self):
        return self.id
    def ObtenesListaElementos(self):
        return self.elemento

class Instruccion:
    def __init__(self, EstadoActual, pin, posicionX, Accion, simbolo, grafico):
        self.EstadoActual = EstadoActual
        self.pin = pin
        self.posicionX = posicionX
        self.accion = Accion
        self.simbolo = simbolo
        self.grafico = grafico

    def ObtenerEstadoActual(self):
        return self.EstadoActual
    def ObtenerPin(self):
        return self.pin
    def ObtenerPosicioX(self):
        return self.posicionX
    def ObtenerAccion(self):
        return self.accion
    def ObtenerSimbolo(self):
        return self.simbolo
    def ObtenerGrafico(self):
        return self.grafico

class IntruccionesDesglozadas:
    def __init__(self, maquina, lista_pines):
        self.maquina = maquina
        self.lista_pin = lista_pines

    def ObtenerNOmbreMaquina(self):
        return self.maquina
    def ObtenerListaPin(self):
        return self.lista_pin
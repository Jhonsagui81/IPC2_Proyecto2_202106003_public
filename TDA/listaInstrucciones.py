from TDA.Nodo import *
import os
class Instrucciones:

    def __init__(self):
        self.Inicio = None
        self.Final = None
        self.limite = 0

    def Insertar(self, EstadoActual, pin, posicionX, Accion, simbolo, texto):
        NuevoNodo = NodoInstrucciones(EstadoActual, pin, posicionX, Accion, simbolo, texto)
        if self.Inicio == None:
            self.Inicio = NuevoNodo
            self.Final = NuevoNodo
            self.limite += 1
        else:
            self.Final.AsignarSiguiente(NuevoNodo)
            self.Final = NuevoNodo
            self.limite += 1

    def PosicionXPin(self, pin):
        Auxiliar = self.Inicio
        while Auxiliar != None:
            if Auxiliar.ObtenerPin() == pin:
                posicion = Auxiliar.ObtenerPosicion()
            Auxiliar = Auxiliar.Siguiente
        return posicion

    def Tiempo(self):
        Aux = self.Inicio
        while Aux != None:
            tiempo = Aux.ObtenerEstadoActual()
            Aux = Aux.Siguiente
        return tiempo

    def Impimir(self):
        Retorno = "La lista tiene: ["
        if self.Inicio == None:
            return "La lista está vacía."
        Auxiliar = self.Inicio
        while Auxiliar != None:
            Retorno += "SEGUNFO:"+str(Auxiliar.ObtenerEstadoActual())+" - Accion"+str(Auxiliar.ObtenerAccion())+" - posicion"+str(Auxiliar.ObtenerPosicion())
            if Auxiliar.Siguiente != None:
                Retorno += ", "
            Auxiliar = Auxiliar.Siguiente
        Retorno += "]"
        return Retorno

    def GenerarGrafica(self, elementosxPin, pines, compuesto):
        titulo = '''bgcolor="cyan"''' 
        texto = ""
        texto = "digraph {\n"
        texto += "\ttb1 [\n"
        texto += "\t\tshape=plaintext\n"
        texto += "\t\tlabel=<\n"
        texto += "\t\t\t<table border='0' cellborder='1' color='black' cellspacing='0'>\n"
        texto += "\t\t\t\t<tr>\n"
        tiempo = self.Tiempo()
        #crea el titulo 
        texto += "\t\t\t\t\t<td "+titulo+" colspan="'"'+str(tiempo+1)+'"'">Instrucciones para construir Compuesto "+str(compuesto)+" </td>\n"
        texto += "\t\t\t\t</tr>\n"
        texto += "\t\t\t\t<tr>\n"
        texto += "\t\t\t\t\t<td> </td>\n"
        #itera para la fila de segundos 
        for fila1 in range(int(tiempo)):
            texto += "\t\t\t\t\t<td>Segundo "+str(fila1+1)+"</td>\n"
        texto += "\t\t\t\t</tr>\n"
        #itera por la cantidad de pines
        for x in range(int(pines)):
            texto += "\t\t\t\t<tr>\n"
            Auxiliar = self.Inicio
            #itera por la cantidad de acciones en el pin
            while Auxiliar != None:
                if int(x+1) == int(Auxiliar.ObtenerPin()):
                    texto += "\t\t\t\t\t<td>"+str(Auxiliar.ObtenerAccion())+"</td>\n"
                Auxiliar = Auxiliar.Siguiente
            texto += "\t\t\t\t</tr>\n"
        texto += "\t\t\t\t<tr>\n"
        texto += "\t\t\t\t\t<td colspan="'"'+str(tiempo+1)+'"'"> </td>\n"
        texto += "\t\t\t\t</tr>\n"
        #Crear la tablas desglzadas
        text = self.devolverTexto()
        texto += text
        

        texto += "\t\t\t</table>\n"
        texto += "\t>];\n"
        texto += "}\n"
        file = open("/home/jhonatan/Descargas/grafica_instrucciones.dot", "w")
        file.write(texto)
        file.close()
        os.system("dot -Tpdf /home/jhonatan/Descargas/grafica_instrucciones.dot -o  /home/jhonatan/Descargas/grafica_instrucciones.pdf")

    def devolverTexto(self):
        texto = self.Final.ObtenerGrafico()
        return texto

    def AsifnarColorPin(self, numeroPin):
        if numeroPin == 1:
            return '''bgcolor="#43c05e"'''
        elif numeroPin == 2:
            return '''bgcolor="#cbe129"''' 
        elif numeroPin == 3:
            return '''bgcolor="#20c59a"''' 
        elif numeroPin == 4:
            return '''bgcolor="#cf5696"''' 
        elif numeroPin == 5:
            return '''bgcolor="#08f3e9"''' 
        elif numeroPin == 6:
            return '''bgcolor="#cbe129"''' 
        elif numeroPin == 7:
            return '''bgcolor="#cbe129"''' 
        elif numeroPin == 8:
            return '''bgcolor="#cbe129"''' 
        elif numeroPin == 9:
            return '''bgcolor="#cbe129"''' 
        elif numeroPin == 10:
            return '''bgcolor="#cbe129"''' 
        elif numeroPin == 11:
            return '''bgcolor="#cbe129"''' 

    def DevolverAccion(self, segundo, pin):
        Auxiliar = self.Inicio
        while Auxiliar != None:
            if Auxiliar.ObtenerEstadoActual() == segundo and Auxiliar.ObtenerPin() == pin:
                return Auxiliar.ObtenerAccion()
            Auxiliar = Auxiliar.Siguiente
from TDA.Nodo import *
from tkinter import messagebox as MessageBox
from TDA.listaElementostrabajo import trabajo
from TDA.listaInstrucciones import Instrucciones

class ListaPines:

    def __init__(self, pines):
        self.Inicio = None
        self.Final = None
        self.aprobacion = True
        self.limite = 0
        self.Pines = pines
    
    def Insertar(self, id, lista_elementos):
        NuevoNodo = NodoPines(id,lista_elementos)
        if self.Inicio == None:
            self.Inicio = NuevoNodo
            self.Final = NuevoNodo
            self.limite +=1
            print("se almaceno pin 1  if")
        else:
            Aux = self.Inicio
            banderin = False
            while Aux != None:
                if Aux.ObtenerListaElementos().CompararListas(NuevoNodo.ObtenerListaElementos()):
                    self.aprobacion = False
                    MessageBox.showinfo("Error!","HAY ELEMENTOS REPETIDOS ENTRE PINES  ")
                    banderin = True
                    return
                else: 
                    Aux = Aux.Siguiente
            if banderin == False:
                self.limite +=1
                self.Final.AsignarSiguiente(NuevoNodo)
                self.Final = NuevoNodo
                print("se almaceno pin 2  else")

    def validacionElementes(self):
        self.AproMax()
        Aux = self.Inicio
        while Aux != None:
            if Aux.ObtenerListaElementos().Estado():
                if self.aprobacion:
                    return True
                else:
                    return False
            else:
                return False
            
    def AproMax(self):
        if self.limite > self.Pines  or self.limite < self.Pines:
            self.aprobacion = False

    def DibujoPines(self, listaElementos):
        texto = ""
        estilo = '''bgcolor="#3498db"'''
        estilo2 = '''bgcolor="green"'''
        Auxiliar = self.Inicio
        while Auxiliar != None:
            texto += "\t\t\t\t<tr "+estilo2+">\n"
            texto += "\t\t\t\t\t<td "+estilo+">"+"Pin "+str(Auxiliar.ObtenerId())+"</td>\n"
            text = Auxiliar.ObtenerListaElementos().GraficaElementos(listaElementos)
            texto += text
            texto += "\t\t\t\t</tr>\n"
            Auxiliar = Auxiliar.Siguiente
        return texto

    def AnalizarCOmpues(self, lista_compuesto):
        Auxiliar = self.Inicio
        estado = True
        contadorCoincidencia = 0
        coincidencia = lista_compuesto.maximoELementosCOmpuesto()
        print("Total compuesto: "+str(coincidencia))
        while Auxiliar != None:
            contadorCoincidencia += Auxiliar.ObtenerListaElementos().AnalizarCompuesto(lista_compuesto)
            Auxiliar = Auxiliar.Siguiente
        print("El total de coincidencia logradas: "+str(contadorCoincidencia))
        if contadorCoincidencia == coincidencia:
            estado = True
        else:
            estado = False
        return estado

    def GenerarListaTrabajo(self, lista_compuesto):
        Auxiliar = self.Inicio
        lista_trabajo = trabajo()
        while Auxiliar != None:
            Auxiliar.ObtenerListaElementos().ElementosTrabajo(lista_compuesto, lista_trabajo, Auxiliar.ObtenerId())
            Auxiliar = Auxiliar.Siguiente
            
        #Recorrer de nuevo los pines
        return lista_trabajo

    def LogicaPinesGeneral(self, clon_compuesto, lista_trabajo):
        #Contador de iteraciones y posicion
        contador_posicion = 0
        contador_segundos = 0
        #Lista de intrucciones 
        lista_Instrucciones = Instrucciones()
        #Estado Inicial
        AuxIns = self.Inicio
        texto = ""
        while AuxIns != None:
            lista_Instrucciones.Insertar(contador_segundos, AuxIns.ObtenerId(),contador_posicion, str("Pin "+str(AuxIns.ObtenerId())), str("Pin "+str(AuxIns.ObtenerId())), texto)
            AuxIns = AuxIns.Siguiente

        #Segundo 1 
        contador_segundos += 1
        contador_posicion += 1
        AuxS1 = self.Inicio
        while AuxS1 != None:
            lista_Instrucciones.Insertar(contador_segundos, AuxS1.ObtenerId(),contador_posicion, "Avanza", "xd", texto)
            AuxS1 = AuxS1.Siguiente
        #Preguntar que pin tiene el elemento a trabajar - LOGICA    
        while True:
            if clon_compuesto.PrimerNodo() == None:
                break
            simbolo = clon_compuesto.PrimerNodo()
            numeroPin = lista_trabajo.buscarPin(simbolo) #retorna numero de pin
            contadorPin = 0 
            #va otro ciclo posiblemente 
            contador_segundos += 1
            Auxiliar = self.Inicio
            while Auxiliar != None:
                contadorPin +=1  #indica el numero de pin 
                #buscar el primer simbolo que se trabajara por pin 
                simboloXpin = lista_trabajo.ElementoInicialXPin(contadorPin)
                if contadorPin == numeroPin:
                    Auxiliar.ObtenerListaElementos().logica(simbolo, lista_Instrucciones, lista_trabajo,clon_compuesto, contador_posicion,contador_segundos, contadorPin, texto,Auxiliar.ObtenerListaElementos())
                else:
                    Auxiliar.ObtenerListaElementos().logicaPinSecundario(simboloXpin, lista_Instrucciones,contador_segundos, contadorPin, texto,Auxiliar.ObtenerListaElementos())
                Auxiliar = Auxiliar.Siguiente
        #imprimir resultado
        return lista_Instrucciones

    def LogicaPines(self, clon_compuesto, lista_trabajo, elementXpin):
        #Contador de iteraciones y posicion
        contador_posicion = 0
        contador_segundos = 0
        texto = ""
        #Lista de intrucciones 
        lista_Instrucciones = Instrucciones()

        #Estado Inicial SEGUNDO CERO
        AuxIns = self.Inicio
        titulo = '''bgcolor="red"''' 
        texto += "\t\t\t\t<tr>\n"
        cont = 0
        while AuxIns != None:
            lista_Instrucciones.Insertar(contador_segundos, AuxIns.ObtenerId(),contador_posicion, str("Pin "+str(AuxIns.ObtenerId())), str("Pin "+str(AuxIns.ObtenerId())), "")
            if cont == 0:
                texto += "\t\t\t\t\t<td "+titulo+" colspan="'"'+str(elementXpin+1)+'"'">Estado Inicial </td>\n"
                texto += "\t\t\t\t</tr>\n"
                cont += 1
            texto += "\t\t\t\t<tr>\n"
            color  = self.AsifnarColorPin(AuxIns.ObtenerId())
            texto += "\t\t\t\t\t<td "+color+">"+str("Pin "+str(AuxIns.ObtenerId()))+"</td>\n"
            text = AuxIns.ObtenerListaElementos().GraficaEstadoInicial("Espera", contador_posicion, color)
            texto += text
            texto += "\t\t\t\t</tr>\n"
            AuxIns = AuxIns.Siguiente
        texto += "\t\t\t\t<tr>\n"
        texto += "\t\t\t\t\t<td colspan="'"'+str(elementXpin+1)+'"'"> </td>\n"
        texto += "\t\t\t\t</tr>\n"

        #Segundo 1 
        contador_segundos += 1
        contador_posicion += 1
        AuxS1 = self.Inicio
        texto += "\t\t\t\t<tr>\n"
        cont = 0
        while AuxS1 != None:
            #Insertar datos a la lista de instrucciones
            lista_Instrucciones.Insertar(contador_segundos, AuxS1.ObtenerId(),contador_posicion, "Avanza", "xd", "")
            #Todo relacionado a la grafica
            if cont == 0:
                texto += "\t\t\t\t\t<td "+titulo+" colspan="'"'+str(elementXpin+1)+'"'">Segundo "+str(contador_segundos)+" </td>\n"
                texto += "\t\t\t\t</tr>\n"
                cont += 1
            texto += "\t\t\t\t<tr>\n"
            color  = self.AsifnarColorPin(AuxS1.ObtenerId())
            texto += "\t\t\t\t\t<td "+color+">"+str("Pin "+str(AuxS1.ObtenerId()))+"</td>\n"
            #Llama elementos del pin
            text = AuxS1.ObtenerListaElementos().GraficaEstadoInicial("Avanza", contador_posicion, color)
            texto += text
            texto += "\t\t\t\t</tr>\n"
            AuxS1 = AuxS1.Siguiente
        texto += "\t\t\t\t<tr>\n"
        texto += "\t\t\t\t\t<td colspan="'"'+str(elementXpin+1)+'"'"> </td>\n"
        texto += "\t\t\t\t</tr>\n"

        #Preguntar que pin tiene el elemento a trabajar - LOGICA    
        while True:
            if clon_compuesto.PrimerNodo() == None:
                texto += "\t\t\t\t<tr>\n"
                texto += "\t\t\t\t\t<td colspan="'"'+str(elementXpin+1)+'"'"> </td>\n"
                texto += "\t\t\t\t</tr>\n"
                break
            #elemento y pin a analizar 
            simbolo = clon_compuesto.PrimerNodo()
            numeroPin = lista_trabajo.buscarPin(simbolo) #retorna numero de pin
            contadorPin = 0 
            #va otro ciclo posiblemente 
            contador_segundos += 1
            Auxiliar = self.Inicio
            texto += "\t\t\t\t<tr>\n"
            cont = 0
            while Auxiliar != None:
                #Todo relacionado a la grafica
                if cont == 0:
                    texto += "\t\t\t\t\t<td "+titulo+" colspan="'"'+str(elementXpin+1)+'"'">Segundo "+str(contador_segundos)+" </td>\n"
                    texto += "\t\t\t\t</tr>\n"
                    cont += 1
                #indica el numero de pin 
                contadorPin +=1  
                #buscar el primer simbolo que se trabajara por pin 
                simboloXpin = lista_trabajo.ElementoInicialXPin(contadorPin)
                if contadorPin == numeroPin:
                    text = Auxiliar.ObtenerListaElementos().logicaGrafica(simbolo, lista_Instrucciones, lista_trabajo,clon_compuesto, contador_posicion,contador_segundos, contadorPin, texto, Auxiliar.ObtenerListaElementos())
                    texto += text
                else:
                    text = Auxiliar.ObtenerListaElementos().logicaPinSecundarioGrafica(simboloXpin, lista_Instrucciones, contador_segundos, contadorPin, texto, Auxiliar.ObtenerListaElementos())
                    texto += text
                Auxiliar = Auxiliar.Siguiente
            texto += "\t\t\t\t<tr>\n"
            texto += "\t\t\t\t\t<td colspan="'"'+str(elementXpin+1)+'"'"> </td>\n"
            texto += "\t\t\t\t</tr>\n"
        #imprimir resultado
        lista_Instrucciones.Insertar(contador_segundos, 0,0, "Avanza", "xd", texto)
        return lista_Instrucciones

    def DevolverTexto(self, text):
        texto = text 
        return text

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
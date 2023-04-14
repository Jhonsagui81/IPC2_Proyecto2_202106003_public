from TDA.Nodo import *
from tkinter import messagebox as MessageBox
from TDA.ListElementCompuesto import ListaElemtosCompuestos

class ListaElementPin:

    def __init__(self, id, MaximoElementos):
        self.Inicio = None
        self.Final = None
        self.id = id 
        self.maximo = MaximoElementos
        self.limite = 0
        self.aprobado = True
        self.maquinaCapaz = True
    
    def Insertar(self, simbolo):
        NuevoNodo = NodoPinesElementos(simbolo)
        if self.ExisteElemento(NuevoNodo):
            MessageBox.showinfo("ERROR","Este Elemento ya esta registrado en el pin ")
            self.aprobado = False
            return 
        if self.limite == self.maximo:
            MessageBox.showinfo("ERROR","Supero el numero de elementos soportados")
            self.aprobado = False
            return
        if self.Inicio == None:
            self.Inicio = NuevoNodo
            self.Final = NuevoNodo
            self.limite += 1
            print("agregado exitoso  if")
        else:
            self.Final.Siguiente = NuevoNodo
            NuevoNodo.Anterior = self.Final
            self.Final = NuevoNodo
            self.limite +=1 
            print("agregado exitoso  else")
        ##if validar si se repite elemento en el pin 
        ##validar el numero maximo de elementos 
        ##validar si existe elemento en otro pin 


    def ExisteElemento(self, NuevoNodo):
        if self.Inicio == None:
            return False
        else:
            Aux = self.Inicio
            while Aux != None:
                if NuevoNodo.ObtenerSimbolo() == Aux.ObtenerSimbolo():
                    return True
                else:
                    Aux = Aux.Siguiente
            return False
    
    def CompararListas(self, lista1):
        Auxiliar = self.Inicio
        while Auxiliar != None:
            if lista1.comparar(Auxiliar.ObtenerSimbolo()):
                return True
            else:
                Auxiliar = Auxiliar.Siguiente
        return False

    def comparar(self, sim):
        Aux = self.Inicio
        while Aux != None:
            if Aux.ObtenerSimbolo() == sim:
                return True
            else:
                Aux = Aux.Siguiente
        return False

    def Estado(self):
        self.AproMax()
        return self.aprobado
    
    def AproMax(self):
        if self.limite > self.maximo  or self.limite < self.maximo:
            self.aprobado = False

    def GraficaElementos(self, listaElementos):
        Aux = self.Inicio
        estilo = '''bgcolor="Cyan"'''
        texto = ""
        while Aux != None:
            atomico = listaElementos.NoAtomico(Aux.ObtenerSimbolo())
            texto += "\t\t\t\t\t<td "+estilo+">"+str(Aux.ObtenerSimbolo())+str("   ")+str(atomico)+"</td>\n"
            Aux = Aux.Siguiente
        return texto

    def AnalizarCompuesto(self, lista_compuesto):
        Auxiliar = self.Inicio
        contadorCoincidencia = 0
        while Auxiliar != None:
            if lista_compuesto.buscarELemeto1(Auxiliar.ObtenerSimbolo()):
                contadorCoincidencia += lista_compuesto.buscarELemeto(Auxiliar.ObtenerSimbolo())
                print("En el pin "+str(self.id)+" Existe el elemento: "+str(contadorCoincidencia))
            Auxiliar = Auxiliar.Siguiente
        return contadorCoincidencia

    def ElementosTrabajo(self, lista_compuesto, lista_trabajo, id):
        #lista donde guardara listaElementosTrabajo
        elementosTrabajo = ListaElemtosCompuestos()
        #lista clonada pra filtrar los elementos 
        clon_list_compuesto = lista_compuesto.clonar()
        ranc = clon_list_compuesto.maximoELementosCOmpuesto()
        #filtrado elementos que puede trabahar este pin 
        for se in range(ranc):
            simbolo = clon_list_compuesto.PrimerNodo()
            Auxiliar = self.Inicio
            while Auxiliar != None:
                if simbolo == Auxiliar.ObtenerSimbolo():
                    elementosTrabajo.InsertarNOxml(id, Auxiliar.ObtenerSimbolo())
                    break
                Auxiliar = Auxiliar.Siguiente
            #elimina elemento inicio compuesto 
            clon_list_compuesto.eliminarNodoInicio()
        #Finaliza filtrado
        print("La lista elemento trabajo en pin es: ")
        print(elementosTrabajo.Impimir())
        lista_trabajo.Insertar(self.id, elementosTrabajo)

    def Fusionar(self, clon_compuesto, lista_trabajo, lista_instrucciones, NoPin):
        #recolectar el primer elemento del compuesto
        simbolo = clon_compuesto.PrimerNodo
        if self.Inicio.ObtenerSimbolo() == simbolo:
            lista_instrucciones.Insertar()



        while True:
            if clon_compuesto.PrimerNodo() == None:
                return False
            simbolo = clon_compuesto.PrimerNodo()  #recolecta elemento a analizar 
            lista_trabajo.buscarPin(simbolo) #Se pasa y verifica en que pin esta

    def logica(self, simbolo, lista_Instrucciones, lista_trabajo,clon_compuesto, contador_posicion,contador_segundos, contadorPin, texto, lista_element_pin):
        posicion = lista_Instrucciones.PosicionXPin(contadorPin)
        contadorIteracion = 0
        Auxiliar = self.Inicio
        while Auxiliar != None:
            contadorIteracion +=1
            if contadorIteracion == posicion:
                if Auxiliar.ObtenerSimbolo() == simbolo:
                    lista_Instrucciones.Insertar(contador_segundos, contadorPin, posicion, "Fuciona", Auxiliar.ObtenerSimbolo(), texto)
                    clon_compuesto.eliminarNodoInicio()
                    lista_trabajo.EliminarNodoInicio(contadorPin)
                    break
                else:
                    contador_desicion = 0
                    aux = self.Inicio
                    while aux != None:
                        contador_desicion += 1 
                        if simbolo == aux.ObtenerSimbolo():
                            if contador_desicion < posicion:
                                posicion -= 1
                                lista_Instrucciones.Insertar(contador_segundos, contadorPin, posicion, "Retrocede", Auxiliar.ObtenerSimbolo(),texto)
                            elif contador_desicion > posicion:
                                posicion += 1
                                lista_Instrucciones.Insertar(contador_segundos, contadorPin, posicion, "Avanza", Auxiliar.ObtenerSimbolo(),texto)
                        aux = aux.Siguiente
                    break
            Auxiliar = Auxiliar.Siguiente
        return texto

    def logicaPinSecundario(self, simbolo, lista_Instrucciones,contador_segundos, contadorPin, texto, lista_element_pin):
        if simbolo == None:
            lista_Instrucciones.Insertar(contador_segundos, contadorPin, 0, "Espera", "None", texto)
        posicion = lista_Instrucciones.PosicionXPin(contadorPin)
        contadorIteraciones = 0
        Auxiliar = self.Inicio
        while Auxiliar != None:
            contadorIteraciones += 1
            if contadorIteraciones == posicion:
                if Auxiliar.ObtenerSimbolo() == simbolo:
                    lista_Instrucciones.Insertar(contador_segundos, contadorPin, posicion, "Espera", Auxiliar.ObtenerSimbolo(), texto)
                    break
                else:
                    contador_desicion = 0
                    aux = self.Inicio
                    while aux != None:
                        contador_desicion += 1 
                        if simbolo == aux.ObtenerSimbolo():
                            if contador_desicion < posicion:
                                posicion -= 1
                                lista_Instrucciones.Insertar(contador_segundos, contadorPin, posicion, "Retrocede", Auxiliar.ObtenerSimbolo(), texto)
                            elif contador_desicion > posicion:
                                posicion += 1
                                lista_Instrucciones.Insertar(contador_segundos, contadorPin, posicion, "Avanza", Auxiliar.ObtenerSimbolo(), texto)
                        aux = aux.Siguiente
                    break
            Auxiliar = Auxiliar.Siguiente
        return texto

    #Para graficasr
    def logicaGrafica(self, simbolo, lista_Instrucciones, lista_trabajo,clon_compuesto, contador_posicion,contador_segundos, contadorPin, texto, lista_element_pin):
        textoLogica = ""
        posicion = lista_Instrucciones.PosicionXPin(contadorPin)
        contadorIteracion = 0
        Auxiliar = self.Inicio
        while Auxiliar != None:
            contadorIteracion +=1
            if contadorIteracion == posicion:
                if Auxiliar.ObtenerSimbolo() == simbolo:
                    #Relacionado a la grafica 
                    textoLogica += "\t\t\t\t<tr>\n"
                    color  = self.AsifnarColorPin(contadorPin)
                    textoLogica += "\t\t\t\t\t<td "+color+">"+str("Pin "+str(contadorPin))+"</td>\n"
                    #Llama elementos del pin
                    text = lista_element_pin.GraficaEstadoInicial("Fuciona", posicion, color)
                    textoLogica += text
                    textoLogica += "\t\t\t\t</tr>\n"

                    lista_Instrucciones.Insertar(contador_segundos, contadorPin, posicion, "Fuciona", Auxiliar.ObtenerSimbolo(), "")
                    clon_compuesto.eliminarNodoInicio()
                    lista_trabajo.EliminarNodoInicio(contadorPin)
                    break
                else:
                    contador_desicion = 0
                    aux = self.Inicio
                    while aux != None:
                        contador_desicion += 1 
                        if simbolo == aux.ObtenerSimbolo():
                            if contador_desicion < posicion:
                                posicion -= 1
                                
                                #Relacionado a la grafica 
                                textoLogica += "\t\t\t\t<tr>\n"
                                color  = self.AsifnarColorPin(contadorPin)
                                textoLogica += "\t\t\t\t\t<td "+color+">"+str("Pin "+str(contadorPin))+"</td>\n"
                                #Llama elementos del pin
                                text = lista_element_pin.GraficaEstadoInicial("Retrocede", posicion, color)
                                textoLogica += text
                                textoLogica += "\t\t\t\t</tr>\n"

                                lista_Instrucciones.Insertar(contador_segundos, contadorPin, posicion, "Retrocede", Auxiliar.ObtenerSimbolo(),"")
                            elif contador_desicion > posicion:
                                posicion += 1
                                
                                #Relacionado a la grafica 
                                textoLogica += "\t\t\t\t<tr>\n"
                                color  = self.AsifnarColorPin(contadorPin)
                                textoLogica += "\t\t\t\t\t<td "+color+">"+str("Pin "+str(contadorPin))+"</td>\n"
                                #Llama elementos del pin
                                text = lista_element_pin.GraficaEstadoInicial("Avanza", posicion, color)
                                textoLogica += text
                                textoLogica += "\t\t\t\t</tr>\n"
                                lista_Instrucciones.Insertar(contador_segundos, contadorPin, posicion, "Avanza", Auxiliar.ObtenerSimbolo(),"")
                        aux = aux.Siguiente
                    break
            Auxiliar = Auxiliar.Siguiente
        return textoLogica

    def logicaPinSecundarioGrafica(self, simbolo, lista_Instrucciones,contador_segundos, contadorPin, texto, lista_element_pin):
        textoLogica = ""
        posicion = lista_Instrucciones.PosicionXPin(contadorPin)
        if simbolo == None:
            #Relacionado a la grafica 
            textoLogica += "\t\t\t\t<tr>\n"
            color  = self.AsifnarColorPin(contadorPin)
            textoLogica += "\t\t\t\t\t<td "+color+">"+str("Pin "+str(contadorPin))+"</td>\n"
            #Llama elementos del pin
            text = lista_element_pin.GraficaEstadoInicial("Espera", posicion, color)
            textoLogica += text
            textoLogica += "\t\t\t\t</tr>\n"
            lista_Instrucciones.Insertar(contador_segundos, contadorPin, 0, "Espera", "None", "")
        posicion = lista_Instrucciones.PosicionXPin(contadorPin)
        contadorIteraciones = 0
        Auxiliar = self.Inicio
        while Auxiliar != None:
            contadorIteraciones += 1
            if contadorIteraciones == posicion:
                if Auxiliar.ObtenerSimbolo() == simbolo:
                    #Relacionado a la grafica 
                    textoLogica += "\t\t\t\t<tr>\n"
                    color  = self.AsifnarColorPin(contadorPin)
                    textoLogica += "\t\t\t\t\t<td "+color+">"+str("Pin "+str(contadorPin))+"</td>\n"
                    #Llama elementos del pin
                    text = lista_element_pin.GraficaEstadoInicial("Espera", posicion, color)
                    textoLogica += text
                    textoLogica += "\t\t\t\t</tr>\n"
                    lista_Instrucciones.Insertar(contador_segundos, contadorPin, posicion, "Espera", Auxiliar.ObtenerSimbolo(), "")
                    break
                else:
                    contador_desicion = 0
                    aux = self.Inicio
                    while aux != None:
                        contador_desicion += 1 
                        if simbolo == aux.ObtenerSimbolo():
                            if contador_desicion < posicion:
                                posicion -= 1
                                
                                #Relacionado a la grafica 
                                textoLogica += "\t\t\t\t<tr>\n"
                                color  = self.AsifnarColorPin(contadorPin)
                                textoLogica += "\t\t\t\t\t<td "+color+">"+str("Pin "+str(contadorPin))+"</td>\n"
                                #Llama elementos del pin
                                text = lista_element_pin.GraficaEstadoInicial("Retrocede", posicion, color)
                                textoLogica += text
                                textoLogica += "\t\t\t\t</tr>\n"

                                lista_Instrucciones.Insertar(contador_segundos, contadorPin, posicion, "Retrocede", Auxiliar.ObtenerSimbolo(), "")
                            elif contador_desicion > posicion:
                                posicion += 1
                                #Relacionado a la grafica 
                                textoLogica += "\t\t\t\t<tr>\n"
                                color  = self.AsifnarColorPin(contadorPin)
                                textoLogica += "\t\t\t\t\t<td "+color+">"+str("Pin "+str(contadorPin))+"</td>\n"
                                #Llama elementos del pin
                                text = lista_element_pin.GraficaEstadoInicial("Avanza", posicion, color)
                                textoLogica += text
                                textoLogica += "\t\t\t\t</tr>\n"
                                lista_Instrucciones.Insertar(contador_segundos, contadorPin, posicion, "Avanza", Auxiliar.ObtenerSimbolo(), "")
                        aux = aux.Siguiente
                    break
            Auxiliar = Auxiliar.Siguiente
        return textoLogica

    def GraficaEstadoInicial(self, Accion, contador_posicion, color):
        texto = ""
        fuciona = '''bgcolor="gray"'''
        Aux = self.Inicio
        contPosicion = 0
        while Aux != None:
            contPosicion += 1
            if contPosicion <= contador_posicion:
                if Accion.lower() == "fuciona":
                    if contPosicion == contador_posicion:
                        texto += "\t\t\t\t\t<td "+fuciona+">"+str(Aux.ObtenerSimbolo())+"</td>\n"
                    else:
                        texto += "\t\t\t\t\t<td "+color+">"+str(Aux.ObtenerSimbolo())+"</td>\n"
                else:
                    texto += "\t\t\t\t\t<td "+color+">"+str(Aux.ObtenerSimbolo())+"</td>\n"
            else:
                texto += "\t\t\t\t\t<td>"+str(Aux.ObtenerSimbolo())+"</td>\n"
            Aux = Aux.Siguiente
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
from TDA.Nodo import *
import os
from tkinter import messagebox as MessageBox


class ListaMaquinas:
    def __init__(self):
        self.Inicio = None
        self.Final = None 
        self.Limite = 0
    
    def InsertarMaquina(self, nombre, no_pines, no_elementos, lista_pines):
        if lista_pines.validacionElementes():
            NuevoNodo = NodoMaquinas(self.Limite, nombre, no_pines, no_elementos, lista_pines)
            if self.Inicio == None:
                self.Inicio = NuevoNodo
                self.Final = NuevoNodo
                self.Limite += 1
                print("Se guardo Maquina en if")
            else:
                self.Limite += 1
                self.Final.AsignarSiguiente(NuevoNodo)
                self.Final = NuevoNodo
                print("Se guardo maquina en else")
        else:
            MessageBox.showinfo("Error","Maquina con problema, NO FUE ALMACENADA!")
    
    def Impimir(self):
        Retorno = "La lista tiene: ["
        if self.Inicio == None:
            return "La lista está vacía."
        Auxiliar = self.Inicio
        while Auxiliar != None:
            Retorno += str(Auxiliar.ObtenerNombre())
            if Auxiliar.Siguiente != None:
                Retorno += ", "
            Auxiliar = Auxiliar.Siguiente
        Retorno += "]"
        return Retorno

    def GenerarDibujo(self, listaElementos):
        estilo = '''bgcolor="#c04343"'''
        texto = "digraph {\n"
        texto += "\ttb1 [\n"
        texto += "\t\tshape=plaintext\n"
        texto += "\t\tlabel=<\n"
        texto += "\t\t\t<table border='0' cellborder='1' color='blue' cellspacing='0'>\n"
        Auxiliar = self.Inicio
        while Auxiliar != None:
            texto += "\t\t\t\t<tr>\n"
            texto += "\t\t\t\t\t<td "+estilo+" colspan="'"'+str(Auxiliar.ObtenerNOElementos()+1)+'"'">"+str(Auxiliar.ObtenerNombre())+"</td>\n"
            texto += "\t\t\t\t</tr>\n"
            
            text = Auxiliar.ObtenerListaPines().DibujoPines(listaElementos)
            texto += text

            texto += "\t\t\t\t<tr>\n"
            texto += "\t\t\t\t\t<td colspan="'"'+str("")+str(Auxiliar.ObtenerNOElementos()+1)+'"'"> </td>\n"
            texto += "\t\t\t\t</tr>\n"
            Auxiliar = Auxiliar.Siguiente
        texto += "\t\t\t</table>\n"
        texto += "\t>];\n"
        texto += "}\n"
        file = open("/home/jhonatan/Descargas/grafica_maquinas.dot", "w")
        file.write(texto)
        file.close()
        os.system("dot -Tpdf /home/jhonatan/Descargas/grafica_maquinas.dot -o  /home/jhonatan/Descargas/grafica_maquinas.pdf")


    def AsignarCompuestoOperar(self, lista_compuesto):
        Aux = self.Inicio
        Texto = ""
        while Aux != None:
            estado = Aux.ObtenerListaPines().AnalizarCOmpues(lista_compuesto)
            if estado:
                #Maquina si puede procesar el compuesto 
                #Generar lista de trabajo 
                lista_trabajo = Aux.ObtenerListaPines().GenerarListaTrabajo(lista_compuesto)
                clon_compuesto = lista_compuesto.clonar()
                #Retorna lista de instrucciones
                lista_instrucciones = Aux.ObtenerListaPines().LogicaPinesGeneral(clon_compuesto, lista_trabajo)
                tiempo = lista_instrucciones.Tiempo()
                Texto += str(Aux.ObtenerNombre())+" Tarda "+str(tiempo)+" s"+","
                
                print("Pasos:")
                print(lista_instrucciones.Impimir())
            else:
                #La maquina no puede procesear el compuesto 
                Texto += str(Aux.ObtenerNombre())+" --No puede procesar COmpuesto"+","
            Aux = Aux.Siguiente
        return Texto

    def UsarMaquina(self, maquina, lista_compuesto):
        Auxiliar = self.Inicio
        while Auxiliar != None:
            if Auxiliar.ObtenerNombre() == maquina:
                estado = Auxiliar.ObtenerListaPines().AnalizarCOmpues(lista_compuesto)
                if estado:
                    #Maquina si puede procesar el compuesto 
                    #Generar lista de trabajo 
                    lista_trabajo = Auxiliar.ObtenerListaPines().GenerarListaTrabajo(lista_compuesto)
                    #Clon de la listaCompuesto
                    clon_compuesto = lista_compuesto.clonar()
                    #Logica
                    elementXpin = self.CatidadElementosXpin(maquina)
                    lista_instrucciones = Auxiliar.ObtenerListaPines().LogicaPines(clon_compuesto, lista_trabajo, elementXpin)
                    # lista_instrucciones.InsertarMaquina(Auxiliar.ObtenerNombre(), Auxiliar.ObtenerListaPines())
                    return lista_instrucciones
                else:
                    #La maquina no puede procesear el compuesto 
                    MessageBox.showinfo("Error","Esta Maquina no puede procesar el compuesto!")
            Auxiliar = Auxiliar.Siguiente

    def CantidadPines(self, maquina):
        Auxiliar = self.Inicio
        while Auxiliar != None:
            if Auxiliar.ObtenerNombre() == maquina:
                return Auxiliar.ObtenerNOPines()
            Auxiliar = Auxiliar.Siguiente
    
    def CatidadElementosXpin(self, maquina):
        Auxiliar = self.Inicio
        while Auxiliar != None:
            if Auxiliar.ObtenerNombre() == maquina:
                return Auxiliar.ObtenerNOElementos()
            Auxiliar = Auxiliar.Siguiente

    def CantidadMaquinas(self):
        return self.Limite

    def MaquinaOptima(self, lista_compuesto):
        Aux = self.Inicio
        Tiempo = 0
        contMaquina = 0
        maquina = ""
        while Aux != None:
            contMaquina += 1
            estado = Aux.ObtenerListaPines().AnalizarCOmpues(lista_compuesto)
            if estado:
                #Maquina si puede procesar el compuesto 
                #Generar lista de trabajo 
                lista_trabajo = Aux.ObtenerListaPines().GenerarListaTrabajo(lista_compuesto)
                clon_compuesto = lista_compuesto.clonar()
                #Retorna lista de instrucciones
                lista_instrucciones = Aux.ObtenerListaPines().LogicaPinesGeneral(clon_compuesto, lista_trabajo)
                tiempo = lista_instrucciones.Tiempo()
                
                if contMaquina == 1:
                    Tiempo = tiempo
                    maquina = Aux.ObtenerNombre()
                else:
                    if tiempo <= Tiempo:
                        Tiempo = tiempo
                        maquina = Aux.ObtenerNombre()
                    else:
                        Tiempo = Tiempo
            else:
                Tiempo = 0
                maquina = "No soportado"
            Aux = Aux.Siguiente
        return maquina

    def TiempoOptimo(self, lista_compuesto):
        Aux = self.Inicio
        Tiempo = 0
        contMaquina = 0
        maquina = ""
        while Aux != None:
            contMaquina += 1
            estado = Aux.ObtenerListaPines().AnalizarCOmpues(lista_compuesto)
            if estado:
                #Maquina si puede procesar el compuesto 
                #Generar lista de trabajo 
                lista_trabajo = Aux.ObtenerListaPines().GenerarListaTrabajo(lista_compuesto)
                clon_compuesto = lista_compuesto.clonar()
                #Retorna lista de instrucciones
                lista_instrucciones = Aux.ObtenerListaPines().LogicaPinesGeneral(clon_compuesto, lista_trabajo)
                tiempo = lista_instrucciones.Tiempo()
                
                if contMaquina == 1:
                    Tiempo = tiempo
                    maquina = Aux.ObtenerNombre()
                else:
                    if tiempo <= Tiempo:
                        Tiempo = tiempo
                        maquina = Aux.ObtenerNombre()
                    else:
                        Tiempo = Tiempo
            else:
                Tiempo = 0
            Aux = Aux.Siguiente
        return Tiempo
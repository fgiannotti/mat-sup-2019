import complejo
import modelador as mod
import math
import click

class OperAvanzadas():
    
    debuggear = False
    formaOutput = None

    def __init__(self):
        self.modelador = mod.Modelador()
        
       #Para el calculo de raices n-ésimas de un commplejo voy a tomar la forma polar del complejo y lo voy igualar al
       # [r, 0]. SIendo r la raiz n-esima del modulo y 0 = angulo + 2kpi /n 
    def calcularRaiz(self, numero, rad):
        #Obtengo los numeros en forma polar
        radicando = int(rad)
        if (radicando < 1):
            raise Exception("El radicando ingresado es invalido")
        
        num = self.modelador.crearNumeroString(numero)
        #defino ahora r w como lista vacia para luego almacenar los valores y el arg
        r = (num.modulo) ** (1/radicando)
        w = []
        k = 0
        #print (k)
        while k < (radicando):
            arg = (num.arg + (2*k*math.pi)) / (radicando)
            list = [r,arg]
            w.append(list)
            print ("resultado:" + "["+ str(r) + " ; " + str(arg)+"]")
            k+=1
            

    def potenciar(self,numero, n):
            complejo= self.modelador.crearNumeroString(numero)
            modulo = complejo.modulo ** n
            arg = n * complejo.arg
            print ("Resultado: [" + str(modulo) + " ; " + str(arg) + "]")

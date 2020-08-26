import math
import click

class Funcion():

    tipo = None
    frec = None
    fase = None
    amplitud = None

    def show(self):
        print("Tipo: " + str(self.tipo))
        print("Frecuencia: " + str(self.frec))
        print("Fase: " + str(self.fase))
        print("Amplitud: " + str(self.amplitud))
      
class OperFasores():
    
    debuggear = False
    
    def __init__(self):
        pass
        
    def sumar_fasores(self):
        print("Ingrese los datos de la primera funcion")
        
        f1 = self.ingresar_funcion()
        print("Datos ingresados:")
        f1.show()
        if click.confirm("Estos datos son correctos?"):
            print("Ingrese los datos de la segunda funcion")
            f2 = self.ingresar_funcion()
            if (ingresaMalTipo(f1.tipo) or ingresaMalTipo(f2.tipo)):
                raise Exception("El fasor ingresado no es un sen/cos")
            if (f1.frec != f2.frec):
                print("Ambos fasores deben tener la misma frecuencia angular")
            else:
                tipo = correccionDeFase(f1,f2) #manda ambos a coseno, le suma pi/2 a los que haga falta
                m = calcularM(f1.amplitud,f2.amplitud,f1.fase,f2.fase)
                tita = calcularTita(f1.amplitud,f2.amplitud,f1.fase,f2.fase)
                print("Resultado: " + str(m) + tipo + "(" + str(f1.frec) + ".t + " + str(tita) + ")")
                #se puede escribir en seno sumando pi/2
        #f+g=Mcos(wt+tita)

    def ingresar_funcion(self):
        
        funcion = Funcion()
        funcion.tipo = click.prompt("Indique el tipo de la funcion (sen/cos)", type=str)
        funcion.frec = click.prompt("Ingrese la frecuencia angular (w)", type=float)
        funcion.fase = click.prompt("Ingrese la fase", type=float)
        funcion.amplitud = click.prompt("Ingrese la amplitud", type=float)
        return funcion

def correccionDeFase (f1,f2):
        #sen(t) = cos(t-pi/2)
        tipo = f1.tipo
        if(f1.tipo != f2.tipo):
            tipo = "cos"
            if (f1.tipo == "sen"):
                f1.fase -= math.pi/2
            if (f2.tipo == "sen"):
                f2.fase -= math.pi/2
        return tipo
    
def calcularM (a1,a2,fase1,fase2):
        #m = math.sqrt( (a1+a2*math.cos(phi))**2 + (a2**2)* (math.sin(phi)**2) )
        m = math.sqrt( a1**2 + a2**2 + 2*a1*a2*math.cos(fase1-fase2))
        return m

def calcularTita (a1,a2,fase1,fase2):
    real = a1*math.cos(fase1) + a2*math.cos(fase2)
    imag = a1*math.sin(fase1) + a2*math.sin(fase2)
    tita = math.atan2(imag,real)
    tita = tita % (2*math.pi)
    return tita
def ingresaMalTipo(tipo):
    return (tipo != "cos" and tipo != "sen")
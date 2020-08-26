import math
import enumerados as enums

class Complejo:
    def __init__(self,a,b,tipoIngreso):
        if tipoIngreso == enums.formaIngreso.binomial:
            self.real = a
            self.imag = b
            self.modulo = math.sqrt(self.real*self.real + self.imag*self.imag)
            self.arg = argumento(self,self.real,self.imag)
        else:
            self.modulo = a
            self.arg = b % (2*math.pi)
            self.real = self.modulo * math.cos(self.arg)
            self.imag = self.modulo * math.sin(self.arg)
    
    def mostrar(self):
            print("Binomica: " + str(self.real) + "+" + str(self.imag) + "j")
            print("Polar: [" + str(self.modulo) + ";" + str(self.arg) + "]")
    
def argumento(self,a,b):
        arg = math.atan2(self.imag, self.real)
        return (arg % (math.pi*2))

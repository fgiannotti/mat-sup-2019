import complejo
import enumerados as enums

class Modelador():
    
    debuggear = False
    formaOutput = None
    
    def modelarNumero(self, numero):
    
        print("Soy el modelador y me pidieron que modele " + numero)
    
        z = Modelador.crearNumeroString(self,numero)
    
        Modelador.mostrarNumero(self,z)
    
    #crea un numero complejo a partir de un String
    def crearNumeroString(self, numero):
        
        verificarFormato(numero)
        
        formaIngreso = determinarIngreso(numero[0])
            
        numeros = parsearNumero(numero)
        try:
            a = float(numeros[0])
            b = float(numeros[1])
        except ValueError:
            raise Exception("Debe ingresar un numero")

        z = complejo.Complejo(a,b,formaIngreso)
            
        return z
   
    def mostrarNumero(self, z): #recibe un objeto de clase complejo, y llama a su metodo mostrar
        z.mostrar() 
    
    #recibe dos numeros en formato string y y los devuelve como tupla
    def crearNumeros(self, numero1, numero2):
        num1 = self.crearNumeroString(numero1)
        num2 = self.crearNumeroString(numero2)
        
        return (num1, num2)
        
def parsearNumero (n):
    numeros = n[1:len(n)-1].split(";")
    return numeros

#recibe un caracter, se fija si es parentesis o corchete, retorna un enum tipoIngreso
def determinarIngreso(caracter):
    formaIngreso = None
    
    if(caracter == "("):
        formaIngreso = enums.formaIngreso.binomial
    
    else:
        formaIngreso = enums.formaIngreso.polar

    return formaIngreso

#se fija si se ingresaron corchetes o parentesis y que el numero tenga punto y coma
def verificarFormato(numero):
    caracter = numero[0]
    if(caracter != "(" and caracter != "["):
        raise Exception("Formato incorrecto: tiene que empezar con paréntesis o con corchetes")
       
    if(numero.find(';') == -1):      
        raise Exception("Formato incorrecto: tiene que tener un punto y coma de separador")


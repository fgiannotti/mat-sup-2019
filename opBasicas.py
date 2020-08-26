

import complejo
import enumerados as enums
import modelador as mod
import math
import click

class OperBasicas:
    
    debuggear = False
    formaOutput = None
    
    def __init__(self):
        self.modelador = mod.Modelador()

    def sumar(self, numero1, numero2):
        
        numeros = self.modelador.crearNumeros(numero1, numero2)
        
        parteReal = numeros[0].real + numeros[1].real
        parteIm = numeros[0].imag + numeros[1].imag
        
        mensaje = "Resultado: " + str(parteReal) + " + " + str(parteIm) + " j"
        
        click.secho(mensaje, fg='green')
        
        #print("Resultado: " + str(parteReal) + " + " + str(parteIm) + " j")

    def restar(self, numero1, numero2):

        numeros = self.modelador.crearNumeros(numero1, numero2)
        
        parteReal = numeros[0].real - numeros[1].real
        parteIm = numeros[0].imag - numeros[1].imag        

        mensaje = "Resultado: " + str(parteReal) + " + " + str(parteIm) + " j"
        
        click.secho(mensaje, fg='green')

    def dividir(self, numero1, numero2):
        numeros = self.modelador.crearNumeros(numero1, numero2)
        try:
            modulo = numeros[0].modulo / numeros[1].modulo
        except ZeroDivisionError: 
            raise Exception("No se puede dividir por un numero con modulo 0")

        argumento = numeros[0].arg - numeros[1].arg

        resultado = complejo.Complejo(modulo, argumento, enums.formaIngreso.polar)
        mensaje = "Resultado: " + str(resultado.real) + " + " + str(resultado.imag) + " j"

        click.secho(mensaje, fg='green')
        
    def multiplicar(self, numero1, numero2):
        numeros = self.modelador.crearNumeros(numero1, numero2)
        
        modulo = numeros[0].modulo * numeros[1].modulo
        argumento = numeros[0].arg + numeros[1].arg
        
        resultado = complejo.Complejo(modulo, argumento, enums.formaIngreso.polar) #Va False porque no es forma binomica
        
        mensaje = "Resultado: " + str(resultado.real) + " + " + str(resultado.imag) + " j"

        click.secho(mensaje, fg='green')


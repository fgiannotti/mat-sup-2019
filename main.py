import click
import modelador
import complejo
import opAvanzadas
import opBasicas
import opFasores

@click.group()
@click.option(
    "--debug", "-d", "debug",
    is_flag=True,
    default=False,
    help='Muestra los logs de debug.',
)
@click.pass_context
def main(ctx, debug : bool):
    """ Una super herramienta para jugar con complejos """
    
    ctx.obj["debug"] = debug

@main.command()
@click.argument('numero', type=click.STRING)
@click.pass_context
def modelar(ctx, numero: str):
    """ Modela en formas trigonometrica, binomica y polar. """
    mod = modelador.Modelador()
    
    mod.debuggear = ctx.obj["debug"]
    
    print("Se quiere modelar " + numero)
    
    mod.modelarNumero(numero)

@main.command()
@click.argument('numero1', type=click.STRING)
@click.argument('numero2', type=click.STRING)
@click.pass_context
def sumar(ctx, numero1: str, numero2: str):
    oper = opBasicas.OperBasicas()
    oper.debuggear = ctx.obj["debug"]
    oper.sumar(numero1, numero2)

@main.command()
@click.argument('numero1', type=click.STRING)
@click.argument('numero2', type=click.STRING)
@click.pass_context
def restar(ctx, numero1: str, numero2: str):
    oper = opBasicas.OperBasicas()
    oper.debuggear = ctx.obj["debug"]
    oper.restar(numero1, numero2)
    
@main.command()
@click.argument('numero1', type=click.STRING)
@click.argument('numero2', type=click.STRING)
@click.pass_context
def dividir(ctx, numero1: str, numero2: str):
    oper = opBasicas.OperBasicas()
    oper.debuggear = ctx.obj["debug"]
    oper.dividir(numero1, numero2)
    
@main.command()
@click.argument('numero1', type=click.STRING)
@click.argument('numero2', type=click.STRING)
@click.pass_context
def multiplicar(ctx, numero1: str, numero2: str):
    oper = opBasicas.OperBasicas()
    oper.debuggear = ctx.obj["debug"]
    oper.multiplicar(numero1, numero2)

@main.command(name="elevar-a-la-n")
@click.argument('numero', type=click.STRING)
@click.argument('potencia', type=click.INT)
@click.pass_context
def potenciar(ctx, numero: str, potencia: int):
    """ Ingresar primero numero y luego potencia """
    oper = opAvanzadas.OperAvanzadas()
    oper.debuggear = ctx.obj["debug"]
    oper.potenciar(numero, potencia)
    
@main.command(name="calcular-raiz")
@click.argument('numero', type=click.STRING)
@click.argument('radicando', type=click.INT)
@click.pass_context
def calcularRaiz(ctx, numero: str, radicando: int):
    """ Ingresar primero numero y luego radicando """
    oper = opAvanzadas.OperAvanzadas()
    oper.debuggear = ctx.obj["debug"]
    oper.calcularRaiz(numero,radicando)
    
@main.command(name="sumar-fasores")
@click.pass_context
def sumar_fasores(ctx):
    operador = opFasores.OperFasores()
    operador.debuggear = ctx.obj["debug"]  
    operador.sumar_fasores()
    
	
if __name__ == "__main__":
    main(obj={})

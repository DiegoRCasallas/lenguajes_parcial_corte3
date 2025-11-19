import sys
from antlr4 import *
from GramaticaMatricesLexer import GramaticaMatricesLexer
from GramaticaMatricesParser import GramaticaMatricesParser
from visitante_matrices import VisitanteMatrices

def evaluar_expresion(expresion, visitante=None):
    """Función para evaluar una expresión específica"""
    if visitante is None:
        visitante = VisitanteMatrices()
    
    input_stream = InputStream(expresion)
    lexer = GramaticaMatricesLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GramaticaMatricesParser(stream)
    
    arbol = parser.programa()
    return visitante.visit(arbol)


def ejecutar_prueba():
    """Lee 'pruebas/prueba.py' (ruta relativa) y ejecuta la gramática línea a línea.

    Ignora líneas vacías y comentarios que empiezan con '#'. Mantiene el mismo
    visitante entre líneas para preservar variables.
    """
    import os

    ruta = os.path.join(os.path.dirname(__file__), 'pruebas', 'prueba.py')
    if not os.path.exists(ruta):
        print(f"Archivo de prueba no encontrado: {ruta}")
        return

    visitante = VisitanteMatrices()
    with open(ruta, 'r', encoding='utf-8') as f:
        tiene_contenido = False
        for lineno, raw in enumerate(f, start=1):
            linea = raw.strip()
            if not linea or linea.startswith('#'):
                continue
            tiene_contenido = True
            try:
                print(f"\n[{ruta}:{lineno}] >>> {linea}")
                resultado = evaluar_expresion(linea, visitante)
                print(f"✅ Resultado: {resultado}")
            except Exception as e:
                print(f"❌ Error en {ruta} línea {lineno}: {e}")

        if not tiene_contenido:
            print(f"El archivo de prueba está vacío: {ruta}")



if __name__ == '__main__':
    
    ejecutar_prueba()
    
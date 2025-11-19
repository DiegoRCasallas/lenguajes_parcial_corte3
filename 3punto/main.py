import sys
from antlr4 import *
from GramaticaMatricesLexer import GramaticaMatricesLexer
from GramaticaMatricesParser import GramaticaMatricesParser
from visitante_matrices import VisitanteMatrices

def mostrar_bienvenida():
    print("=" * 60)
    print("        CALCULADORA DE MATRICES - PRODUCTO PUNTO")
    print("=" * 60)
    print("\nComandos disponibles:")
    print("- Definir matriz: A = [[1,2],[3,4]]")
    print("- Producto punto: A * B")
    print("- Suma: A + B")
    print("- Resta: A - B")
    print("- Paréntesis: (A * B) + C")
    print("- Salir: exit, quit o salir")
    print("\nEjemplos:")
    print("  A = [[1,2],[3,4]]")
    print("  B = [[5,6],[7,8]]")
    print("  A * B")
    print("=" * 60)

def principal():
    mostrar_bienvenida()
    visitante = VisitanteMatrices()
    
    while True:
        try:
            # Leer entrada del usuario
            texto = input('\nmatriz> ')
            if texto.lower() in ['exit', 'quit', 'salir']:
                print("¡Hasta luego!")
                break
            if not texto.strip():
                continue
            
            # Crear el stream de entrada
            input_stream = InputStream(texto)
            
            # Crear el lexer y parser
            lexer = GramaticaMatricesLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = GramaticaMatricesParser(stream)
            
            # Parsear y evaluar
            arbol = parser.programa()
            resultado = visitante.visit(arbol)
            
            # Mostrar resultado final
            print(f"🎯 RESULTADO FINAL: {resultado}")
            
        except EOFError:
            break
        except Exception as e:
            print(f"❌ Error: {e}")

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

def ejecutar_ejemplos():
    """Ejecuta ejemplos predefinidos"""
    print("\n" + "=" * 60)
    print("           EJECUTANDO EJEMPLOS")
    print("=" * 60)
    
    visitante = VisitanteMatrices()
    
    ejemplos = [
        "# Ejemplo 1: Matrices 2x2",
        "A = [[1, 2], [3, 4]]",
        "B = [[5, 6], [7, 8]]",
        "A * B",
        
        "# Ejemplo 2: Matrices de diferentes dimensiones",
        "C = [[1, 2, 3], [4, 5, 6]]",
        "D = [[7, 8], [9, 10], [11, 12]]", 
        "C * D",
        
        "# Ejemplo 3: Operaciones combinadas",
        "E = [[2, 0], [1, 3]]",
        "(A * B) + E",
        
        "# Ejemplo 4: Suma y resta",
        "A + B",
        "B - A"
    ]
    
    for ejemplo in ejemplos:
        try:
            if ejemplo.startswith('#'):
                print(f"\n{ejemplo}")
                continue
                
            print(f"\n>>> {ejemplo}")
            resultado = evaluar_expresion(ejemplo, visitante)
            print(f"✅ Resultado: {resultado}")
            
        except Exception as e:
            print(f"❌ Error en ejemplo '{ejemplo}': {e}")

if __name__ == '__main__':
    # Ejecutar ejemplos primero
    ejecutar_ejemplos()
    
    # Luego iniciar el modo interactivo
    print("\n" + "=" * 60)
    print("           MODO INTERACTIVO")
    print("=" * 60)
    principal()
from GramaticaMatricesVisitor import GramaticaMatricesVisitor
from GramaticaMatricesParser import GramaticaMatricesParser
import numpy as np

class Matriz:
    def __init__(self, datos):
        if isinstance(datos, list):
            self.datos = np.array(datos, dtype=float)
        else:
            self.datos = datos
        self.filas, self.columnas = self.datos.shape
    
    def producto_punto(self, otra):
        if self.columnas != otra.filas:
            raise ValueError(f"Dimensiones incompatibles para producto punto: {self.filas}x{self.columnas} * {otra.filas}x{otra.columnas}")
        
        resultado = np.dot(self.datos, otra.datos)
        return Matriz(resultado)
    
    def sumar(self, otra):
        if self.filas != otra.filas or self.columnas != otra.columnas:
            raise ValueError(f"Dimensiones incompatibles para suma: {self.filas}x{self.columnas} + {otra.filas}x{otra.columnas}")
        return Matriz(self.datos + otra.datos)
    
    def restar(self, otra):
        if self.filas != otra.filas or self.columnas != otra.columnas:
            raise ValueError(f"Dimensiones incompatibles para resta: {self.filas}x{self.columnas} - {otra.filas}x{otra.columnas}")
        return Matriz(self.datos - otra.datos)
    
    def __str__(self):
        return str(self.datos.tolist())

class VisitanteMatrices(GramaticaMatricesVisitor):
    def __init__(self):
        self.variables = {}
    
    def visitPrograma(self, ctx: GramaticaMatricesParser.ProgramaContext):
        return self.visit(ctx.expresionMatriz())
    
    def visitDeclaracionMatriz(self, ctx: GramaticaMatricesParser.DeclaracionMatrizContext):
        nombre_variable = ctx.ID().getText()
        matriz = self.visit(ctx.matrizLiteral())
        self.variables[nombre_variable] = matriz
        print(f"Matriz '{nombre_variable}' definida: {matriz}")
        return matriz
    
    def visitAsignacion(self, ctx: GramaticaMatricesParser.AsignacionContext):
        nombre_variable = ctx.ID().getText()
        matriz = self.visit(ctx.expresionMatriz())
        self.variables[nombre_variable] = matriz
        print(f"Matriz '{nombre_variable}' asignada: {matriz}")
        return matriz
    
    def visitProductoPunto(self, ctx: GramaticaMatricesParser.MultiplicacionContext):
        # Procesar multiplicaciones en orden
        resultado = self.visit(ctx.suma(0))
        for i in range(1, ctx.getChildCount(), 2):
            if ctx.getChild(i).getText() == '*':
                siguiente = self.visit(ctx.suma(i // 2))
                resultado = resultado.producto_punto(siguiente)
        return resultado
    
    def visitSumaRestaMatriz(self, ctx: GramaticaMatricesParser.SumaContext):
        resultado = self.visit(ctx.resta(0))
        for i in range(1, ctx.getChildCount(), 2):
            operador = ctx.getChild(i).getText()
            siguiente = self.visit(ctx.resta(i // 2 + 1))
            if operador == '+':
                resultado = resultado.sumar(siguiente)
            elif operador == '-':
                resultado = resultado.restar(siguiente)
        return resultado
    
    def visitParentesis(self, ctx: GramaticaMatricesParser.ParentesisContext):
        return self.visit(ctx.operacionMatriz())
    
    def visitVariableMatriz(self, ctx: GramaticaMatricesParser.VariableMatrizContext):
        nombre_variable = ctx.ID().getText()
        if nombre_variable not in self.variables:
            raise ValueError(f"Variable no definida: '{nombre_variable}'")
        matriz = self.variables[nombre_variable]
        return matriz
    
    def visitLiteralMatriz(self, ctx: GramaticaMatricesParser.LiteralMatrizContext):
        return self.visit(ctx.matrizLiteral())
    
    def visitMatrizLiteral(self, ctx: GramaticaMatricesParser.MatrizLiteralContext):
        filas = []
        for ctx_fila in ctx.fila():
            fila = self.visit(ctx_fila)
            filas.append(fila)
        if not filas:
            raise ValueError("Matriz vacía no permitida")
        matriz = Matriz(filas)
        return matriz
    
    def visitFila(self, ctx: GramaticaMatricesParser.FilaContext):
        fila = [float(numero.getText()) for numero in ctx.NUMERO()]
        if not fila:
            raise ValueError("Fila vacía no permitida")
        return fila

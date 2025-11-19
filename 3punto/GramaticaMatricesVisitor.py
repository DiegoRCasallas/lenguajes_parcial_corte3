# Generated from GramaticaMatrices.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GramaticaMatricesParser import GramaticaMatricesParser
else:
    from GramaticaMatricesParser import GramaticaMatricesParser

# This class defines a complete generic visitor for a parse tree produced by GramaticaMatricesParser.

class GramaticaMatricesVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GramaticaMatricesParser#programa.
    def visitPrograma(self, ctx:GramaticaMatricesParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMatricesParser#expresionMatriz.
    def visitExpresionMatriz(self, ctx:GramaticaMatricesParser.ExpresionMatrizContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMatricesParser#declaracionMatriz.
    def visitDeclaracionMatriz(self, ctx:GramaticaMatricesParser.DeclaracionMatrizContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMatricesParser#asignacion.
    def visitAsignacion(self, ctx:GramaticaMatricesParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMatricesParser#operacionMatriz.
    def visitOperacionMatriz(self, ctx:GramaticaMatricesParser.OperacionMatrizContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMatricesParser#ProductoPunto.
    def visitProductoPunto(self, ctx:GramaticaMatricesParser.ProductoPuntoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMatricesParser#SumaRestaMatriz.
    def visitSumaRestaMatriz(self, ctx:GramaticaMatricesParser.SumaRestaMatrizContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMatricesParser#resta.
    def visitResta(self, ctx:GramaticaMatricesParser.RestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMatricesParser#Parentesis.
    def visitParentesis(self, ctx:GramaticaMatricesParser.ParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMatricesParser#VariableMatriz.
    def visitVariableMatriz(self, ctx:GramaticaMatricesParser.VariableMatrizContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMatricesParser#LiteralMatriz.
    def visitLiteralMatriz(self, ctx:GramaticaMatricesParser.LiteralMatrizContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMatricesParser#matrizLiteral.
    def visitMatrizLiteral(self, ctx:GramaticaMatricesParser.MatrizLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMatricesParser#fila.
    def visitFila(self, ctx:GramaticaMatricesParser.FilaContext):
        return self.visitChildren(ctx)



del GramaticaMatricesParser
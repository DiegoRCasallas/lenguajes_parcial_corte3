# Generated from GramaticaMatrices.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,12,89,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,1,1,1,1,1,1,3,1,
        29,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,5,5,5,44,
        8,5,10,5,12,5,47,9,5,1,6,1,6,1,6,5,6,52,8,6,10,6,12,6,55,9,6,1,7,
        1,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,65,8,8,1,9,1,9,1,9,1,9,5,9,71,8,
        9,10,9,12,9,74,9,9,1,9,1,9,1,10,1,10,1,10,1,10,5,10,82,8,10,10,10,
        12,10,85,9,10,1,10,1,10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,
        0,1,1,0,3,4,85,0,22,1,0,0,0,2,28,1,0,0,0,4,30,1,0,0,0,6,34,1,0,0,
        0,8,38,1,0,0,0,10,40,1,0,0,0,12,48,1,0,0,0,14,56,1,0,0,0,16,64,1,
        0,0,0,18,66,1,0,0,0,20,77,1,0,0,0,22,23,3,2,1,0,23,24,5,0,0,1,24,
        1,1,0,0,0,25,29,3,4,2,0,26,29,3,8,4,0,27,29,3,6,3,0,28,25,1,0,0,
        0,28,26,1,0,0,0,28,27,1,0,0,0,29,3,1,0,0,0,30,31,5,10,0,0,31,32,
        5,1,0,0,32,33,3,18,9,0,33,5,1,0,0,0,34,35,5,10,0,0,35,36,5,1,0,0,
        36,37,3,2,1,0,37,7,1,0,0,0,38,39,3,10,5,0,39,9,1,0,0,0,40,45,3,12,
        6,0,41,42,5,2,0,0,42,44,3,12,6,0,43,41,1,0,0,0,44,47,1,0,0,0,45,
        43,1,0,0,0,45,46,1,0,0,0,46,11,1,0,0,0,47,45,1,0,0,0,48,53,3,14,
        7,0,49,50,7,0,0,0,50,52,3,14,7,0,51,49,1,0,0,0,52,55,1,0,0,0,53,
        51,1,0,0,0,53,54,1,0,0,0,54,13,1,0,0,0,55,53,1,0,0,0,56,57,3,16,
        8,0,57,15,1,0,0,0,58,59,5,5,0,0,59,60,3,8,4,0,60,61,5,6,0,0,61,65,
        1,0,0,0,62,65,5,10,0,0,63,65,3,18,9,0,64,58,1,0,0,0,64,62,1,0,0,
        0,64,63,1,0,0,0,65,17,1,0,0,0,66,67,5,7,0,0,67,72,3,20,10,0,68,69,
        5,8,0,0,69,71,3,20,10,0,70,68,1,0,0,0,71,74,1,0,0,0,72,70,1,0,0,
        0,72,73,1,0,0,0,73,75,1,0,0,0,74,72,1,0,0,0,75,76,5,9,0,0,76,19,
        1,0,0,0,77,78,5,7,0,0,78,83,5,11,0,0,79,80,5,8,0,0,80,82,5,11,0,
        0,81,79,1,0,0,0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,86,
        1,0,0,0,85,83,1,0,0,0,86,87,5,9,0,0,87,21,1,0,0,0,6,28,45,53,64,
        72,83
    ]

class GramaticaMatricesParser ( Parser ):

    grammarFileName = "GramaticaMatrices.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'*'", "'+'", "'-'", "'('", "')'", 
                     "'['", "','", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "NUMERO", "WS" ]

    RULE_programa = 0
    RULE_expresionMatriz = 1
    RULE_declaracionMatriz = 2
    RULE_asignacion = 3
    RULE_operacionMatriz = 4
    RULE_multiplicacion = 5
    RULE_suma = 6
    RULE_resta = 7
    RULE_primaria = 8
    RULE_matrizLiteral = 9
    RULE_fila = 10

    ruleNames =  [ "programa", "expresionMatriz", "declaracionMatriz", "asignacion", 
                   "operacionMatriz", "multiplicacion", "suma", "resta", 
                   "primaria", "matrizLiteral", "fila" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    ID=10
    NUMERO=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresionMatriz(self):
            return self.getTypedRuleContext(GramaticaMatricesParser.ExpresionMatrizContext,0)


        def EOF(self):
            return self.getToken(GramaticaMatricesParser.EOF, 0)

        def getRuleIndex(self):
            return GramaticaMatricesParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = GramaticaMatricesParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.expresionMatriz()
            self.state = 23
            self.match(GramaticaMatricesParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionMatrizContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracionMatriz(self):
            return self.getTypedRuleContext(GramaticaMatricesParser.DeclaracionMatrizContext,0)


        def operacionMatriz(self):
            return self.getTypedRuleContext(GramaticaMatricesParser.OperacionMatrizContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(GramaticaMatricesParser.AsignacionContext,0)


        def getRuleIndex(self):
            return GramaticaMatricesParser.RULE_expresionMatriz

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresionMatriz" ):
                listener.enterExpresionMatriz(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresionMatriz" ):
                listener.exitExpresionMatriz(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresionMatriz" ):
                return visitor.visitExpresionMatriz(self)
            else:
                return visitor.visitChildren(self)




    def expresionMatriz(self):

        localctx = GramaticaMatricesParser.ExpresionMatrizContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expresionMatriz)
        try:
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.declaracionMatriz()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.operacionMatriz()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.asignacion()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionMatrizContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GramaticaMatricesParser.ID, 0)

        def matrizLiteral(self):
            return self.getTypedRuleContext(GramaticaMatricesParser.MatrizLiteralContext,0)


        def getRuleIndex(self):
            return GramaticaMatricesParser.RULE_declaracionMatriz

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracionMatriz" ):
                listener.enterDeclaracionMatriz(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracionMatriz" ):
                listener.exitDeclaracionMatriz(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracionMatriz" ):
                return visitor.visitDeclaracionMatriz(self)
            else:
                return visitor.visitChildren(self)




    def declaracionMatriz(self):

        localctx = GramaticaMatricesParser.DeclaracionMatrizContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracionMatriz)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(GramaticaMatricesParser.ID)
            self.state = 31
            self.match(GramaticaMatricesParser.T__0)
            self.state = 32
            self.matrizLiteral()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GramaticaMatricesParser.ID, 0)

        def expresionMatriz(self):
            return self.getTypedRuleContext(GramaticaMatricesParser.ExpresionMatrizContext,0)


        def getRuleIndex(self):
            return GramaticaMatricesParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = GramaticaMatricesParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(GramaticaMatricesParser.ID)
            self.state = 35
            self.match(GramaticaMatricesParser.T__0)
            self.state = 36
            self.expresionMatriz()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperacionMatrizContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicacion(self):
            return self.getTypedRuleContext(GramaticaMatricesParser.MultiplicacionContext,0)


        def getRuleIndex(self):
            return GramaticaMatricesParser.RULE_operacionMatriz

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacionMatriz" ):
                listener.enterOperacionMatriz(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacionMatriz" ):
                listener.exitOperacionMatriz(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacionMatriz" ):
                return visitor.visitOperacionMatriz(self)
            else:
                return visitor.visitChildren(self)




    def operacionMatriz(self):

        localctx = GramaticaMatricesParser.OperacionMatrizContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_operacionMatriz)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.multiplicacion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GramaticaMatricesParser.RULE_multiplicacion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ProductoPuntoContext(MultiplicacionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaMatricesParser.MultiplicacionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def suma(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaMatricesParser.SumaContext)
            else:
                return self.getTypedRuleContext(GramaticaMatricesParser.SumaContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProductoPunto" ):
                listener.enterProductoPunto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProductoPunto" ):
                listener.exitProductoPunto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProductoPunto" ):
                return visitor.visitProductoPunto(self)
            else:
                return visitor.visitChildren(self)



    def multiplicacion(self):

        localctx = GramaticaMatricesParser.MultiplicacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_multiplicacion)
        self._la = 0 # Token type
        try:
            localctx = GramaticaMatricesParser.ProductoPuntoContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.suma()
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 41
                self.match(GramaticaMatricesParser.T__1)
                self.state = 42
                self.suma()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SumaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GramaticaMatricesParser.RULE_suma

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SumaRestaMatrizContext(SumaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaMatricesParser.SumaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def resta(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaMatricesParser.RestaContext)
            else:
                return self.getTypedRuleContext(GramaticaMatricesParser.RestaContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSumaRestaMatriz" ):
                listener.enterSumaRestaMatriz(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSumaRestaMatriz" ):
                listener.exitSumaRestaMatriz(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSumaRestaMatriz" ):
                return visitor.visitSumaRestaMatriz(self)
            else:
                return visitor.visitChildren(self)



    def suma(self):

        localctx = GramaticaMatricesParser.SumaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_suma)
        self._la = 0 # Token type
        try:
            localctx = GramaticaMatricesParser.SumaRestaMatrizContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.resta()
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==4:
                self.state = 49
                _la = self._input.LA(1)
                if not(_la==3 or _la==4):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 50
                self.resta()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RestaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaria(self):
            return self.getTypedRuleContext(GramaticaMatricesParser.PrimariaContext,0)


        def getRuleIndex(self):
            return GramaticaMatricesParser.RULE_resta

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResta" ):
                listener.enterResta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResta" ):
                listener.exitResta(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResta" ):
                return visitor.visitResta(self)
            else:
                return visitor.visitChildren(self)




    def resta(self):

        localctx = GramaticaMatricesParser.RestaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_resta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.primaria()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimariaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GramaticaMatricesParser.RULE_primaria

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class VariableMatrizContext(PrimariaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaMatricesParser.PrimariaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(GramaticaMatricesParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableMatriz" ):
                listener.enterVariableMatriz(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableMatriz" ):
                listener.exitVariableMatriz(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableMatriz" ):
                return visitor.visitVariableMatriz(self)
            else:
                return visitor.visitChildren(self)


    class ParentesisContext(PrimariaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaMatricesParser.PrimariaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def operacionMatriz(self):
            return self.getTypedRuleContext(GramaticaMatricesParser.OperacionMatrizContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentesis" ):
                listener.enterParentesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentesis" ):
                listener.exitParentesis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentesis" ):
                return visitor.visitParentesis(self)
            else:
                return visitor.visitChildren(self)


    class LiteralMatrizContext(PrimariaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaMatricesParser.PrimariaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def matrizLiteral(self):
            return self.getTypedRuleContext(GramaticaMatricesParser.MatrizLiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralMatriz" ):
                listener.enterLiteralMatriz(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralMatriz" ):
                listener.exitLiteralMatriz(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralMatriz" ):
                return visitor.visitLiteralMatriz(self)
            else:
                return visitor.visitChildren(self)



    def primaria(self):

        localctx = GramaticaMatricesParser.PrimariaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_primaria)
        try:
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                localctx = GramaticaMatricesParser.ParentesisContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.match(GramaticaMatricesParser.T__4)
                self.state = 59
                self.operacionMatriz()
                self.state = 60
                self.match(GramaticaMatricesParser.T__5)
                pass
            elif token in [10]:
                localctx = GramaticaMatricesParser.VariableMatrizContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.match(GramaticaMatricesParser.ID)
                pass
            elif token in [7]:
                localctx = GramaticaMatricesParser.LiteralMatrizContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 63
                self.matrizLiteral()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatrizLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fila(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaMatricesParser.FilaContext)
            else:
                return self.getTypedRuleContext(GramaticaMatricesParser.FilaContext,i)


        def getRuleIndex(self):
            return GramaticaMatricesParser.RULE_matrizLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrizLiteral" ):
                listener.enterMatrizLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrizLiteral" ):
                listener.exitMatrizLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrizLiteral" ):
                return visitor.visitMatrizLiteral(self)
            else:
                return visitor.visitChildren(self)




    def matrizLiteral(self):

        localctx = GramaticaMatricesParser.MatrizLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_matrizLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(GramaticaMatricesParser.T__6)
            self.state = 67
            self.fila()
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 68
                self.match(GramaticaMatricesParser.T__7)
                self.state = 69
                self.fila()
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 75
            self.match(GramaticaMatricesParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaMatricesParser.NUMERO)
            else:
                return self.getToken(GramaticaMatricesParser.NUMERO, i)

        def getRuleIndex(self):
            return GramaticaMatricesParser.RULE_fila

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFila" ):
                listener.enterFila(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFila" ):
                listener.exitFila(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFila" ):
                return visitor.visitFila(self)
            else:
                return visitor.visitChildren(self)




    def fila(self):

        localctx = GramaticaMatricesParser.FilaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_fila)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(GramaticaMatricesParser.T__6)
            self.state = 78
            self.match(GramaticaMatricesParser.NUMERO)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 79
                self.match(GramaticaMatricesParser.T__7)
                self.state = 80
                self.match(GramaticaMatricesParser.NUMERO)
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 86
            self.match(GramaticaMatricesParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






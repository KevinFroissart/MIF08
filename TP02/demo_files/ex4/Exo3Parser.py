# Generated from Exo3.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\b")
        buf.write("\30\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\26\n\3\3\3\2\2\4\2\4\2")
        buf.write("\2\2\30\2\6\3\2\2\2\4\25\3\2\2\2\6\7\5\4\3\2\7\b\7\2\2")
        buf.write("\3\b\3\3\2\2\2\t\n\7\3\2\2\n\13\5\4\3\2\13\f\7\4\2\2\f")
        buf.write("\r\5\4\3\2\r\26\3\2\2\2\16\17\7\5\2\2\17\20\5\4\3\2\20")
        buf.write("\21\7\6\2\2\21\22\5\4\3\2\22\26\3\2\2\2\23\26\7\7\2\2")
        buf.write("\24\26\3\2\2\2\25\t\3\2\2\2\25\16\3\2\2\2\25\23\3\2\2")
        buf.write("\2\25\24\3\2\2\2\26\5\3\2\2\2\3\25")
        return buf.getvalue()


class Exo3Parser ( Parser ):

    grammarFileName = "Exo3.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "CHARS", "WS" ]

    RULE_r = 0
    RULE_expr = 1

    ruleNames =  [ "r", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    CHARS=5
    WS=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(Exo3Parser.ExprContext,0)


        def EOF(self):
            return self.getToken(Exo3Parser.EOF, 0)

        def getRuleIndex(self):
            return Exo3Parser.RULE_r

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterR" ):
                listener.enterR(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitR" ):
                listener.exitR(self)




    def r(self):

        localctx = Exo3Parser.RContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_r)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr()
            self.state = 5
            self.match(Exo3Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Exo3Parser.ExprContext)
            else:
                return self.getTypedRuleContext(Exo3Parser.ExprContext,i)


        def CHARS(self):
            return self.getToken(Exo3Parser.CHARS, 0)

        def getRuleIndex(self):
            return Exo3Parser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = Exo3Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Exo3Parser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 7
                self.match(Exo3Parser.T__0)
                self.state = 8
                self.expr()
                self.state = 9
                self.match(Exo3Parser.T__1)
                self.state = 10
                self.expr()
                pass
            elif token in [Exo3Parser.T__2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 12
                self.match(Exo3Parser.T__2)
                self.state = 13
                self.expr()
                self.state = 14
                self.match(Exo3Parser.T__3)
                self.state = 15
                self.expr()
                pass
            elif token in [Exo3Parser.CHARS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 17
                self.match(Exo3Parser.CHARS)
                pass
            elif token in [Exo3Parser.EOF, Exo3Parser.T__1, Exo3Parser.T__3]:
                self.enterOuterAlt(localctx, 4)

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






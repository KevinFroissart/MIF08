# Generated from Example2.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\7")
        buf.write("\31\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5")
        buf.write("\3\17\n\3\3\3\3\3\3\3\7\3\24\n\3\f\3\16\3\27\13\3\3\3")
        buf.write("\2\3\4\4\2\4\2\2\2\30\2\6\3\2\2\2\4\16\3\2\2\2\6\7\5\4")
        buf.write("\3\2\7\b\7\3\2\2\b\t\7\2\2\3\t\3\3\2\2\2\n\13\b\3\1\2")
        buf.write("\13\f\7\6\2\2\f\17\b\3\1\2\r\17\7\5\2\2\16\n\3\2\2\2\16")
        buf.write("\r\3\2\2\2\17\25\3\2\2\2\20\21\f\5\2\2\21\22\7\4\2\2\22")
        buf.write("\24\5\4\3\6\23\20\3\2\2\2\24\27\3\2\2\2\25\23\3\2\2\2")
        buf.write("\25\26\3\2\2\2\26\5\3\2\2\2\27\25\3\2\2\2\4\16\25")
        return buf.getvalue()


class Example2Parser ( Parser ):

    grammarFileName = "Example2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "OP", "INT", "ID", "WS" ]

    RULE_r = 0
    RULE_expr = 1

    ruleNames =  [ "r", "expr" ]

    EOF = Token.EOF
    T__0=1
    OP=2
    INT=3
    ID=4
    WS=5

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
            return self.getTypedRuleContext(Example2Parser.ExprContext,0)


        def EOF(self):
            return self.getToken(Example2Parser.EOF, 0)

        def getRuleIndex(self):
            return Example2Parser.RULE_r

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterR" ):
                listener.enterR(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitR" ):
                listener.exitR(self)




    def r(self):

        localctx = Example2Parser.RContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_r)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr(0)
            self.state = 5
            self.match(Example2Parser.T__0)
            self.state = 6
            self.match(Example2Parser.EOF)
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
            self._ID = None # Token

        def ID(self):
            return self.getToken(Example2Parser.ID, 0)

        def INT(self):
            return self.getToken(Example2Parser.INT, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Example2Parser.ExprContext)
            else:
                return self.getTypedRuleContext(Example2Parser.ExprContext,i)


        def OP(self):
            return self.getToken(Example2Parser.OP, 0)

        def getRuleIndex(self):
            return Example2Parser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Example2Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Example2Parser.ID]:
                self.state = 9
                localctx._ID = self.match(Example2Parser.ID)
                print('oh an id : '+(None if localctx._ID is None else localctx._ID.text));
                pass
            elif token in [Example2Parser.INT]:
                self.state = 11
                self.match(Example2Parser.INT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 19
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Example2Parser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 14
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 15
                    self.match(Example2Parser.OP)
                    self.state = 16
                    self.expr(4) 
                self.state = 21
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         





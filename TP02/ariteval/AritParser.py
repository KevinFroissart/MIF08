# Generated from Arit.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("=\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\6\2\f\n\2\r\2\16")
        buf.write("\2\r\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\5\4\36\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\7\4/\n\4\f\4\16\4\62\13\4\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\5\5;\n\5\3\5\2\3\6\6\2\4\6\b")
        buf.write("\2\2\2>\2\13\3\2\2\2\4\21\3\2\2\2\6\35\3\2\2\2\b:\3\2")
        buf.write("\2\2\n\f\5\4\3\2\13\n\3\2\2\2\f\r\3\2\2\2\r\13\3\2\2\2")
        buf.write("\r\16\3\2\2\2\16\17\3\2\2\2\17\20\7\2\2\3\20\3\3\2\2\2")
        buf.write("\21\22\5\6\4\2\22\23\7\5\2\2\23\24\b\3\1\2\24\5\3\2\2")
        buf.write("\2\25\26\b\4\1\2\26\27\7\7\2\2\27\30\5\6\4\7\30\31\b\4")
        buf.write("\1\2\31\36\3\2\2\2\32\33\5\b\5\2\33\34\b\4\1\2\34\36\3")
        buf.write("\2\2\2\35\25\3\2\2\2\35\32\3\2\2\2\36\60\3\2\2\2\37 \f")
        buf.write("\6\2\2 !\7\b\2\2!\"\5\6\4\7\"#\b\4\1\2#/\3\2\2\2$%\f\5")
        buf.write("\2\2%&\7\7\2\2&\'\5\6\4\6\'(\b\4\1\2(/\3\2\2\2)*\f\4\2")
        buf.write("\2*+\7\6\2\2+,\5\6\4\5,-\b\4\1\2-/\3\2\2\2.\37\3\2\2\2")
        buf.write(".$\3\2\2\2.)\3\2\2\2/\62\3\2\2\2\60.\3\2\2\2\60\61\3\2")
        buf.write("\2\2\61\7\3\2\2\2\62\60\3\2\2\2\63\64\7\n\2\2\64;\b\5")
        buf.write("\1\2\65\66\7\3\2\2\66\67\5\6\4\2\678\7\4\2\289\b\5\1\2")
        buf.write("9;\3\2\2\2:\63\3\2\2\2:\65\3\2\2\2;\t\3\2\2\2\7\r\35.")
        buf.write("\60:")
        return buf.getvalue()


class AritParser ( Parser ):

    grammarFileName = "Arit.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "';'", "'+'", "'-'", "'*'", 
                     "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "SCOL", "PLUS", 
                      "MINUS", "MULT", "DIV", "INT", "COMMENT", "NEWLINE", 
                      "WS" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_expr = 2
    RULE_atom = 3

    ruleNames =  [ "prog", "statement", "expr", "atom" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    SCOL=3
    PLUS=4
    MINUS=5
    MULT=6
    DIV=7
    INT=8
    COMMENT=9
    NEWLINE=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(AritParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AritParser.StatementContext)
            else:
                return self.getTypedRuleContext(AritParser.StatementContext,i)


        def getRuleIndex(self):
            return AritParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = AritParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.statement()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << AritParser.T__0) | (1 << AritParser.MINUS) | (1 << AritParser.INT))) != 0)):
                    break

            self.state = 13
            self.match(AritParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._expr = None # ExprContext

        def expr(self):
            return self.getTypedRuleContext(AritParser.ExprContext,0)


        def SCOL(self):
            return self.getToken(AritParser.SCOL, 0)

        def getRuleIndex(self):
            return AritParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = AritParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            localctx._expr = self.expr(0)
            self.state = 16
            self.match(AritParser.SCOL)
            print((None if localctx._expr is None else self._input.getText(localctx._expr.start,localctx._expr.stop))+" = "+str(localctx._expr.val))
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
            self.val = None
            self.e1 = None # ExprContext
            self.a = None # AtomContext
            self.e2 = None # ExprContext

        def MINUS(self):
            return self.getToken(AritParser.MINUS, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AritParser.ExprContext)
            else:
                return self.getTypedRuleContext(AritParser.ExprContext,i)


        def atom(self):
            return self.getTypedRuleContext(AritParser.AtomContext,0)


        def MULT(self):
            return self.getToken(AritParser.MULT, 0)

        def PLUS(self):
            return self.getToken(AritParser.PLUS, 0)

        def getRuleIndex(self):
            return AritParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AritParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AritParser.MINUS]:
                self.state = 20
                self.match(AritParser.MINUS)
                self.state = 21
                localctx.e1 = self.expr(5)
                localctx.val = -localctx.e1.val
                pass
            elif token in [AritParser.T__0, AritParser.INT]:
                self.state = 24
                localctx.a = self.atom()
                localctx.val = localctx.a.val
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 46
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 44
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = AritParser.ExprContext(self, _parentctx, _parentState)
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 29
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 30
                        self.match(AritParser.MULT)
                        self.state = 31
                        localctx.e2 = self.expr(5)
                        localctx.val = localctx.e1.val*localctx.e2.val
                        pass

                    elif la_ == 2:
                        localctx = AritParser.ExprContext(self, _parentctx, _parentState)
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 34
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 35
                        self.match(AritParser.MINUS)
                        self.state = 36
                        localctx.e2 = self.expr(4)
                        localctx.val = localctx.e1.val - localctx.e2.val
                        pass

                    elif la_ == 3:
                        localctx = AritParser.ExprContext(self, _parentctx, _parentState)
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 39
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 40
                        self.match(AritParser.PLUS)
                        self.state = 41
                        localctx.e2 = self.expr(3)
                        localctx.val = localctx.e1.val + localctx.e2.val
                        pass

             
                self.state = 48
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.val = None
            self._INT = None # Token
            self._expr = None # ExprContext

        def INT(self):
            return self.getToken(AritParser.INT, 0)

        def expr(self):
            return self.getTypedRuleContext(AritParser.ExprContext,0)


        def getRuleIndex(self):
            return AritParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = AritParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_atom)
        try:
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AritParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                localctx._INT = self.match(AritParser.INT)
                localctx.val = int((None if localctx._INT is None else localctx._INT.text))
                pass
            elif token in [AritParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.match(AritParser.T__0)
                self.state = 52
                localctx._expr = self.expr(0)
                self.state = 53
                self.match(AritParser.T__1)
                localctx.val=localctx._expr.val
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         





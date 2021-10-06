# Generated from Example2.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write("\"\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2")
        buf.write("\3\3\3\3\3\4\6\4\23\n\4\r\4\16\4\24\3\5\6\5\30\n\5\r\5")
        buf.write("\16\5\31\3\6\6\6\35\n\6\r\6\16\6\36\3\6\3\6\2\2\7\3\3")
        buf.write("\5\4\7\5\t\6\13\7\3\2\5\5\2,-//\61\61\4\2C\\c|\5\2\13")
        buf.write("\f\17\17\"\"\2$\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\3\r\3\2\2\2\5\17\3\2\2\2\7\22")
        buf.write("\3\2\2\2\t\27\3\2\2\2\13\34\3\2\2\2\r\16\7=\2\2\16\4\3")
        buf.write("\2\2\2\17\20\t\2\2\2\20\6\3\2\2\2\21\23\4\62;\2\22\21")
        buf.write("\3\2\2\2\23\24\3\2\2\2\24\22\3\2\2\2\24\25\3\2\2\2\25")
        buf.write("\b\3\2\2\2\26\30\t\3\2\2\27\26\3\2\2\2\30\31\3\2\2\2\31")
        buf.write("\27\3\2\2\2\31\32\3\2\2\2\32\n\3\2\2\2\33\35\t\4\2\2\34")
        buf.write("\33\3\2\2\2\35\36\3\2\2\2\36\34\3\2\2\2\36\37\3\2\2\2")
        buf.write("\37 \3\2\2\2 !\b\6\2\2!\f\3\2\2\2\6\2\24\31\36\3\b\2\2")
        return buf.getvalue()


class Example2Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    OP = 2
    INT = 3
    ID = 4
    WS = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'" ]

    symbolicNames = [ "<INVALID>",
            "OP", "INT", "ID", "WS" ]

    ruleNames = [ "T__0", "OP", "INT", "ID", "WS" ]

    grammarFileName = "Example2.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



# Generated from Exo3.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\b")
        buf.write("\"\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\7\6")
        buf.write("\7\35\n\7\r\7\16\7\36\3\7\3\7\2\2\b\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\3\2\4\5\2*+]]__\5\2\13\f\17\17\"\"\2\"\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\3\17\3\2\2\2\5\21\3\2\2\2\7\23\3\2\2\2\t")
        buf.write("\25\3\2\2\2\13\27\3\2\2\2\r\34\3\2\2\2\17\20\7*\2\2\20")
        buf.write("\4\3\2\2\2\21\22\7+\2\2\22\6\3\2\2\2\23\24\7]\2\2\24\b")
        buf.write("\3\2\2\2\25\26\7_\2\2\26\n\3\2\2\2\27\30\n\2\2\2\30\31")
        buf.write("\3\2\2\2\31\32\b\6\2\2\32\f\3\2\2\2\33\35\t\3\2\2\34\33")
        buf.write("\3\2\2\2\35\36\3\2\2\2\36\34\3\2\2\2\36\37\3\2\2\2\37")
        buf.write(" \3\2\2\2 !\b\7\2\2!\16\3\2\2\2\4\2\36\3\b\2\2")
        return buf.getvalue()


class Exo3Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    CHARS = 5
    WS = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "CHARS", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "CHARS", "WS" ]

    grammarFileName = "Exo3.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



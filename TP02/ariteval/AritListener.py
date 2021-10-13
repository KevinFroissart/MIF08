# Generated from Arit.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AritParser import AritParser
else:
    from AritParser import AritParser

# This class defines a complete listener for a parse tree produced by AritParser.
class AritListener(ParseTreeListener):

    # Enter a parse tree produced by AritParser#prog.
    def enterProg(self, ctx:AritParser.ProgContext):
        pass

    # Exit a parse tree produced by AritParser#prog.
    def exitProg(self, ctx:AritParser.ProgContext):
        pass


    # Enter a parse tree produced by AritParser#statement.
    def enterStatement(self, ctx:AritParser.StatementContext):
        pass

    # Exit a parse tree produced by AritParser#statement.
    def exitStatement(self, ctx:AritParser.StatementContext):
        pass


    # Enter a parse tree produced by AritParser#expr.
    def enterExpr(self, ctx:AritParser.ExprContext):
        pass

    # Exit a parse tree produced by AritParser#expr.
    def exitExpr(self, ctx:AritParser.ExprContext):
        pass


    # Enter a parse tree produced by AritParser#atom.
    def enterAtom(self, ctx:AritParser.AtomContext):
        pass

    # Exit a parse tree produced by AritParser#atom.
    def exitAtom(self, ctx:AritParser.AtomContext):
        pass



del AritParser
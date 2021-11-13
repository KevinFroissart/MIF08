from typing import List, Tuple
from MiniCVisitor import MiniCVisitor
from MiniCParser import MiniCParser
from .APIRiscV import (LinearCode, Condition)
from . import Operands
from antlr4.tree.Trees import Trees
from Errors import MiniCInternalError, MiniCUnsupportedError

"""
CAP, MIF08, three-address code generation + simple alloc
This visitor constructs an object of type "LinearCode".
"""


class MiniCCodeGen3AVisitor(MiniCVisitor):

    _current_function: LinearCode

    def __init__(self, debug, parser):
        super().__init__()
        self._parser = parser
        self._debug = debug
        self._functions = []
        self._lastlabel = ""

    def get_functions(self):
        return self._functions

    def printSymbolTable(self):  # pragma: no cover
        print("--variables to temporaries map--")
        for keys, values in self._symbol_table.items():
            print(keys + '-->' + str(values))

    # handle variable decl

    def visitVarDecl(self, ctx) -> None:
        type_str = ctx.typee().getText()
        vars_l = self.visit(ctx.id_l())
        for name in vars_l:
            if name in self._symbol_table:
                raise MiniCInternalError(
                    "Variable {} has already been declared".format(name))
            else:
                tmp = self._current_function.new_tmp()
                self._symbol_table[name] = tmp
                if type_str not in ("int", "bool"):
                    raise MiniCUnsupportedError("Unsupported type " + type_str)
                # Initialization to 0 or False, both represented with 0
                self._current_function.add_instruction_LI(tmp, 0)

    def visitIdList(self, ctx) -> Operands.Temporary:
        t = self.visit(ctx.id_l())
        t.append(ctx.ID().getText())
        return t

    def visitIdListBase(self, ctx) -> List[str]:
        return [ctx.ID().getText()]

    # expressions

    def visitParExpr(self, ctx) -> Operands.Temporary:
        return self.visit(ctx.expr())

    def visitIntAtom(self, ctx) -> Operands.Temporary:
        val = int(ctx.getText())
        dest_temp = self._current_function.new_tmp()
        self._current_function.add_instruction_LI(dest_temp, val)
        return dest_temp

    def visitFloatAtom(self, ctx) -> Operands.Temporary:
        raise MiniCUnsupportedError("float literal")

    def visitBooleanAtom(self, ctx) -> Operands.Temporary:
        val = ctx.getText()
        print(val)
        dest_temp = self._current_function.new_tmp()
        if val == "true":
            self._current_function.add_instruction_LI(dest_temp, 1)
            return dest_temp
        elif val == "false":
            self._current_function.add_instruction_LI(dest_temp, 0)
            return dest_temp
        else:
            raise MiniCInternalError(
                "Unknown boolean value '%s'" % val)
        # (Exercise 5)

    def visitIdAtom(self, ctx) -> Operands.Temporary:
        try:
            # get the temporary associated to id
            return self._symbol_table[ctx.getText()]
        except KeyError:  # pragma: no cover
            raise MiniCInternalError(
                "Undefined variable {}, this should have failed to typecheck."
                .format(ctx.getText())
            )

    def visitStringAtom(self, ctx) -> Operands.Temporary:
        raise MiniCUnsupportedError("string atom")

    # now visit expressions

    def visitAtomExpr(self, ctx) -> Operands.Temporary:
        return self.visit(ctx.atom())

    # python3 MiniCC.py --reg-alloc=none TP04/tests/provided/step1/test_vars.c
    def visitAdditiveExpr(self, ctx) -> Operands.Temporary:
        left_val = self.visit(ctx.expr(0))
        right_val = self.visit(ctx.expr(1))
        dest_temp = self._current_function.new_tmp()
        if ctx.myop.type == MiniCParser.PLUS:
            self._current_function.add_instruction_ADD(dest_temp, left_val, right_val)
        elif ctx.myop.type == MiniCParser.MINUS:
            self._current_function.add_instruction_SUB(dest_temp, left_val, right_val)
        return dest_temp # (Exercise 2)

    def visitOrExpr(self, ctx) -> Operands.Temporary:
        left_val = self.visit(ctx.expr(0))
        right_val = self.visit(ctx.expr(1))
        dest_temp = self._current_function.new_tmp()
        self._current_function.add_instruction_OR(dest_temp, left_val, right_val)
        return dest_temp # (Exercise 2)

    def visitAndExpr(self, ctx) -> Operands.Temporary:
        left_val = self.visit(ctx.expr(0))
        right_val = self.visit(ctx.expr(1))
        dest_temp = self._current_function.new_tmp()
        self._current_function.add_instruction_AND(dest_temp, left_val, right_val)
        return dest_temp # (Exercise 2)

    def visitEqualityExpr(self, ctx) -> Operands.Temporary:
        return self.visitRelationalExpr(ctx)

    def visitRelationalExpr(self, ctx) -> Operands.Temporary:
        c = Condition(ctx.myop.type)
        if self._debug:
            print("relational expression:")
            print(Trees.toStringTree(ctx, None, self._parser))
            print("Condition:", c)
        # dest <- new_tmp()
        dest_temp = self._current_function.new_tmp()
        # t1 <- GenCodeExpr(e1)
        left_val = self.visit(ctx.expr(0))
        # t2 <- GenCodeExpr(e2)
        right_val = self.visit(ctx.expr(1))
        # endrel <- new_label()
        endrel = self._current_function.new_label("endrel")
        # code.add("li dest, 0")
        self._current_function.add_instruction_LI(dest_temp, 0)
        # if t1>=t2 jump to endrel
        # code.add("bge endrel, t1, t2")
        self._current_function.add_instruction_cond_JUMP(endrel, left_val, Condition.negate(c), right_val)
        # code.add("li dest, 1")
        self._current_function.add_instruction_LI(dest_temp, 1)
        # code.addLabel(endrel)
        self._current_function.add_label(endrel)
        return dest_temp # (Exercise 5)

    def visitMultiplicativeExpr(self, ctx) -> Operands.Temporary:
        div_by_zero_lbl = self._current_function.get_label_div_by_zero()
        left_val = self.visit(ctx.expr(0))
        right_val = self.visit(ctx.expr(1))
        dest_temp = self._current_function.new_tmp()
        zero = self._current_function.new_tmp()
        self._current_function.add_instruction_LI(zero, 0)
        if ctx.myop.type == MiniCParser.MULT:
            self._current_function.add_instruction_MUL(dest_temp, left_val, right_val)
            return dest_temp
        elif ctx.myop.type == MiniCParser.DIV:
            self._current_function.add_instruction_cond_JUMP(div_by_zero_lbl, right_val, Condition(MiniCParser.EQ), zero)
            self._current_function.add_instruction_DIV(dest_temp, left_val, right_val)
            return dest_temp
        elif ctx.myop.type == MiniCParser.MOD:
            self._current_function.add_instruction_cond_JUMP(div_by_zero_lbl, right_val, Condition(MiniCParser.EQ), zero)
            self._current_function.add_instruction_REM(dest_temp, left_val, right_val)
            return dest_temp
        else:
            raise MiniCInternalError(
                        "Unknown multiplicative operator '%s'" % ctx.myop.text)
        # (Exercise 2 or at the end)

    def visitNotExpr(self, ctx) -> Operands.Temporary:
        #self._current_function.add_instruction_NOT(dest_temp, val)
        bool_val = self.visit(ctx.expr())
        dest_temp = self._current_function.new_tmp()
        negative_label = self._current_function.new_label("negative")
        end_label = self._current_function.new_label("end")
        zero = self._current_function.new_tmp()
        self._current_function.add_instruction_LI(zero, 0)
        # If bool_val is negative, jump to negative_label and return positive boolean : !false = true
        self._current_function.add_instruction_cond_JUMP(negative_label, bool_val, Condition(MiniCParser.EQ), zero)
        # If not, the value to be returned is 0 ie. false, then jump to end_label
        self._current_function.add_instruction_LI(dest_temp, 0)
        self._current_function.add_instruction_JUMP(end_label)
        self._current_function.add_label(negative_label)
        self._current_function.add_instruction_LI(dest_temp, 1)
        self._current_function.add_label(end_label)
        return dest_temp # (Exercise 5)

    def visitUnaryMinusExpr(self, ctx) -> Operands.Temporary:
        dest_temp = self._current_function.new_tmp()
        val = self.visit(ctx.expr())
        zero = self._current_function.new_tmp()
        self._current_function.add_instruction_LI(zero, 0)
        self._current_function.add_instruction_SUB(dest_temp, zero, val)
        return dest_temp # (Exercise 2)

    def visitProgRule(self, ctx) -> None:
        self.visitChildren(ctx)

    def visitFuncDecl(self, ctx) -> None:
        funcname = ctx.ID().getText()
        self._current_function = LinearCode(funcname)
        self._symbol_table = dict()

        self.visit(ctx.vardecl_l())
        self.visit(ctx.block())
        self._current_function.add_comment("Return at end of function:")
        # This skeleton doesn't deal properly with functions, and
        # hardcodes a "return 0;" at the end of function. Generate
        # code for this "return 0;".
        self._current_function.add_instruction_LI(Operands.A0, 0)
        self._functions.append(self._current_function)
        del self._current_function

    def visitAssignStat(self, ctx) -> None:
        if self._debug:
            print("assign statement, rightexpression is:")
            print(Trees.toStringTree(ctx.expr(), None, self._parser))
        expr_temp = self.visit(ctx.expr())
        name = ctx.ID().getText()
        self._current_function.add_instruction_MV(self._symbol_table[name], expr_temp)

    def visitIfStat(self, ctx) -> None:
        if self._debug:
            print("if statement")
        # lelse <- new_label()
        else_label = self._current_function.new_label("else")
        # lendif <- new_label()
        end_if_label = self._current_function.new_label("end_if")
        # t1 <- GenCodeExpr(b)
        bool_value = self.visit(ctx.expr())
        # if the condition is false, jump to else
        # code.add("beq lelse, t1, 0")
        zero = self._current_function.new_tmp()
        self._current_function.add_instruction_LI(zero, 0)
        if ctx.else_block is not None :
            self._current_function.add_instruction_cond_JUMP(else_label, bool_value, Condition(MiniCParser.EQ), zero)
        else :
            self._current_function.add_instruction_cond_JUMP(end_if_label, bool_value, Condition(MiniCParser.EQ), zero)
        # GenCodeSmt(S1)  # then
        self.visit(ctx.then_block)
        # code.add("j lendif")
        self._current_function.add_instruction_JUMP(end_if_label)
        # code.addLabel(lelse)
        if ctx.else_block is not None:
            self._current_function.add_label(else_label)
        # GenCodeSmt(S2)  # else
            self.visit(ctx.else_block)
        # code.addLabel(lendif)
        self._current_function.add_label(end_if_label) # (Exercise 5)

    def visitWhileStat(self, ctx) -> None:
        if self._debug:
            print("while statement, condition is:")
            print(Trees.toStringTree(ctx.expr(), None, self._parser))
            print("and block is:")
            print(Trees.toStringTree(ctx.stat_block(), None, self._parser))
        # ltest < - new_label()
        test_label = self._current_function.new_label("test")
        # lendwhile < - new_label()
        end_while_label = self._current_function.new_label("endwhile")
        # code.addLabel(ltest)
        self._current_function.add_label(test_label)
        # t1 < - GenCodeExpr(b)
        bool_value = self.visit(ctx.expr())
        # code.add("beq lendwhile, t1, 0")
        zero = self._current_function.new_tmp()
        self._current_function.add_instruction_LI(zero, 0)
        self._current_function.add_instruction_cond_JUMP(end_while_label, bool_value, Condition(MiniCParser.EQ), zero)
        # GenCodeSmt(S)  # execute S
        self.visit(ctx.stat_block())
        # code.add("j ltest")  # and jump to the test
        self._current_function.add_instruction_JUMP(test_label)
        # code.addLabel(lendwhile)  # else it is done.
        self._current_function.add_label(end_while_label) # (Exercise 5)

    # visit statements

    def visitPrintlnintStat(self, ctx) -> None:
        expr_loc = self.visit(ctx.expr())
        if self._debug:
            print("print_int statement, expression is:")
            print(Trees.toStringTree(ctx.expr(), None, self._parser))
        self._current_function.add_instruction_PRINTLN_INT(expr_loc)

    def visitPrintlnfloatStat(self, ctx) -> None:
        raise MiniCUnsupportedError("Unsupported type float")

    def visitPrintlnstringStat(self, ctx) -> None:
        raise MiniCUnsupportedError("Unsupported type string")

    def visitStatList(self, ctx) -> None:
        for stat in ctx.stat():
            self._current_function.add_comment(Trees.toStringTree(stat, None, self._parser))
            self.visit(stat)

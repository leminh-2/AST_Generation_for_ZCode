# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#list_declared.
    def visitList_declared(self, ctx:ZCodeParser.List_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#declared.
    def visitDeclared(self, ctx:ZCodeParser.DeclaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#variables.
    def visitVariables(self, ctx:ZCodeParser.VariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#implicit_var.
    def visitImplicit_var(self, ctx:ZCodeParser.Implicit_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#keyword_var.
    def visitKeyword_var(self, ctx:ZCodeParser.Keyword_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#list_numberlit.
    def visitList_numberlit(self, ctx:ZCodeParser.List_numberlitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#number_lit_prime.
    def visitNumber_lit_prime(self, ctx:ZCodeParser.Number_lit_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#typ.
    def visitTyp(self, ctx:ZCodeParser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#implicit_dynamic.
    def visitImplicit_dynamic(self, ctx:ZCodeParser.Implicit_dynamicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function.
    def visitFunction(self, ctx:ZCodeParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#prameters_list.
    def visitPrameters_list(self, ctx:ZCodeParser.Prameters_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#prameterprime.
    def visitPrameterprime(self, ctx:ZCodeParser.PrameterprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#prameter.
    def visitPrameter(self, ctx:ZCodeParser.PrameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr.
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr0.
    def visitExpr0(self, ctx:ZCodeParser.Expr0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr1.
    def visitExpr1(self, ctx:ZCodeParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr2.
    def visitExpr2(self, ctx:ZCodeParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr3.
    def visitExpr3(self, ctx:ZCodeParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr4.
    def visitExpr4(self, ctx:ZCodeParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr5.
    def visitExpr5(self, ctx:ZCodeParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr6.
    def visitExpr6(self, ctx:ZCodeParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr7.
    def visitExpr7(self, ctx:ZCodeParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr8.
    def visitExpr8(self, ctx:ZCodeParser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#functionCall.
    def visitFunctionCall(self, ctx:ZCodeParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_list.
    def visitExpr_list(self, ctx:ZCodeParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exprprime.
    def visitExprprime(self, ctx:ZCodeParser.ExprprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#indexOp.
    def visitIndexOp(self, ctx:ZCodeParser.IndexOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#op_idx.
    def visitOp_idx(self, ctx:ZCodeParser.Op_idxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrElem.
    def visitArrElem(self, ctx:ZCodeParser.ArrElemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#subExpr.
    def visitSubExpr(self, ctx:ZCodeParser.SubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#literal.
    def visitLiteral(self, ctx:ZCodeParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_literal.
    def visitArray_literal(self, ctx:ZCodeParser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt.
    def visitStmt(self, ctx:ZCodeParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#declaration_stmt.
    def visitDeclaration_stmt(self, ctx:ZCodeParser.Declaration_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assignment_stmt.
    def visitAssignment_stmt(self, ctx:ZCodeParser.Assignment_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#lhs.
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#indexp.
    def visitIndexp(self, ctx:ZCodeParser.IndexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#indexlist.
    def visitIndexlist(self, ctx:ZCodeParser.IndexlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_stmt.
    def visitIf_stmt(self, ctx:ZCodeParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ifPart.
    def visitIfPart(self, ctx:ZCodeParser.IfPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elifParts.
    def visitElifParts(self, ctx:ZCodeParser.ElifPartsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elifpart.
    def visitElifpart(self, ctx:ZCodeParser.ElifpartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#nlAndStmt.
    def visitNlAndStmt(self, ctx:ZCodeParser.NlAndStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elsePart.
    def visitElsePart(self, ctx:ZCodeParser.ElsePartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ifcondition.
    def visitIfcondition(self, ctx:ZCodeParser.IfconditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#for_stmt.
    def visitFor_stmt(self, ctx:ZCodeParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#break_stmt.
    def visitBreak_stmt(self, ctx:ZCodeParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continue_stmt.
    def visitContinue_stmt(self, ctx:ZCodeParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#return_stmt.
    def visitReturn_stmt(self, ctx:ZCodeParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#call_stmt.
    def visitCall_stmt(self, ctx:ZCodeParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#block_stmt.
    def visitBlock_stmt(self, ctx:ZCodeParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_list.
    def visitStmt_list(self, ctx:ZCodeParser.Stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ignore.
    def visitIgnore(self, ctx:ZCodeParser.IgnoreContext):
        return self.visitChildren(ctx)



del ZCodeParser
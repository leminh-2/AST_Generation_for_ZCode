from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


class ASTGeneration(ZCodeVisitor):
    
    # program: NEWLINE* list_declared EOF;
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.list_declared()))


    # list_declared:  declared list_declared |  declared;
    def visitList_declared(self, ctx:ZCodeParser.List_declaredContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.declared())] + self.visit(ctx.list_declared())
        else: return [self.visit(ctx.declared())]

    # declared: function | variables ignore;
    def visitDeclared(self, ctx:ZCodeParser.DeclaredContext):
        if ctx.function(): return self.visit(ctx.function())
        else: return self.visit(ctx.variables())
        #ignore the ignore rule


    # variables: implicit_var | keyword_var | implicit_dynamic;
    def visitVariables(self, ctx:ZCodeParser.VariablesContext):
        if ctx.implicit_var(): return self.visit(ctx.implicit_var())
        elif ctx.keyword_var(): return self.visit(ctx.keyword_var())
        else: return self.visit(ctx.implicit_dynamic())


    # implicit_var: VAR ID ASSIGNINIT expr;
    def visitImplicit_var(self, ctx:ZCodeParser.Implicit_varContext):
        return VarDecl(Id(ctx.ID().getText()), None, "var", self.visit(ctx.expr()))


    '''
    keyword_var: 
      typ ID
    | typ ID (LBRACKET list_numberlit RBRACKET)
    | typ ID (ASSIGNINIT expr)
    | typ ID (LBRACKET list_numberlit RBRACKET) (ASSIGNINIT expr);

    '''
    def visitKeyword_var(self, ctx:ZCodeParser.Keyword_varContext):
        if ctx.getChildCount() == 2:
            return VarDecl(Id(ctx.ID().getText()), self.visit(ctx.typ()), None, None)
        elif ctx.getChildCount() == 5:
            return VarDecl(Id(ctx.ID().getText()), ArrayType(self.visit(ctx.list_numberlit()), self.visit(ctx.typ())))
        elif ctx.getChildCount() == 4:
            return VarDecl(Id(ctx.ID().getText()), self.visit(ctx.typ()), None, self.visit(ctx.expr()))
        else: #ctx.getChildCount() == 7
            return VarDecl(Id(ctx.ID().getText()), ArrayType(self.visit(ctx.list_numberlit()), self.visit(ctx.typ())), None, self.visit(ctx.expr()))


    # list_numberlit: NUMBER_LIT number_lit_prime | ;
    def visitList_numberlit(self, ctx:ZCodeParser.List_numberlitContext):
        #return list of float
        #not return list of NumberLiteral
        if ctx.getChildCount() == 0:
            return []
        return [float(ctx.NUMBER_LIT().getText())] + self.visit(ctx.number_lit_prime())
        #return [NumberLiteral(float(ctx.NUMBER_LIT().getText()))] + self.visit(ctx.number_lit_prime())
        #remove NumberLiteral to fix tc 304: ArrayType([5.0], StringType())

    # number_lit_prime: COMMA NUMBER_LIT number_lit_prime | ;
    def visitNumber_lit_prime(self, ctx:ZCodeParser.Number_lit_primeContext):
        #return list of number_lit
        if ctx.getChildCount() == 0:
            return []
        return [float(ctx.NUMBER_LIT().getText())] + self.visit(ctx.number_lit_prime())
        #return [NumberLiteral(float(ctx.NUMBER_LIT().getText()))] + self.visit(ctx.number_lit_prime())
        #remove NumberLiteral to fix tc 3034: ArrayType([5.0], StringType())

    # typ: BOOL | NUMBER | STRING;
    def visitTyp(self, ctx:ZCodeParser.TypContext):
        if ctx.BOOL(): return BoolType()
        elif ctx.NUMBER(): return NumberType()
        else: return StringType()
        #dao cac thu tu nay lai de chong giong code

    '''
    implicit_dynamic: 
      DYNAMIC ID
    | DYNAMIC ID (ASSIGNINIT expr);
    '''
    def visitImplicit_dynamic(self, ctx:ZCodeParser.Implicit_dynamicContext):
        if ctx.getChildCount() == 2:
            return VarDecl(Id(ctx.ID().getText()), None, 'dynamic', None)
        return VarDecl(Id(ctx.ID().getText()), None, 'dynamic', self.visit(ctx.expr()))

    '''
    function: 
      FUNC ID LPAREN prameters_list RPAREN (return_stmt)
    | FUNC ID LPAREN prameters_list RPAREN (ignore return_stmt)
    | FUNC ID LPAREN prameters_list RPAREN (block_stmt)
    | FUNC ID LPAREN prameters_list RPAREN (ignore block_stmt)
    | FUNC ID LPAREN prameters_list RPAREN (ignore);
    '''
    def visitFunction(self, ctx:ZCodeParser.FunctionContext):
        if ctx.return_stmt():
            return FuncDecl(Id(ctx.ID().getText()), 
                            self.visit(ctx.prameters_list()), 
                            self.visit(ctx.return_stmt()))
        elif ctx.block_stmt():
            return FuncDecl(Id(ctx.ID().getText()), 
                            self.visit(ctx.prameters_list()), 
                            self.visit(ctx.block_stmt()))
        else:
            return FuncDecl(Id(ctx.ID().getText()), 
                            self.visit(ctx.prameters_list()), 
                            None)

    # prameters_list: prameter prameterprime | ;
    def visitPrameters_list(self, ctx:ZCodeParser.Prameters_listContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.prameter())] + self.visit(ctx.prameterprime())

    # prameterprime: COMMA prameter prameterprime | ;
    def visitPrameterprime(self, ctx:ZCodeParser.PrameterprimeContext):
        # return list of prameter
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.prameter())] + self.visit(ctx.prameterprime())

    '''
    prameter: 
      typ ID
    | typ ID (LBRACKET list_numberlit RBRACKET);
    '''
    def visitPrameter(self, ctx:ZCodeParser.PrameterContext):
        if ctx.getChildCount() == 2:
            return VarDecl(Id(ctx.ID().getText()), self.visit(ctx.typ()), None, None)
        else:
            return VarDecl(Id(ctx.ID().getText()), ArrayType(self.visit(ctx.list_numberlit()), self.visit(ctx.typ())))
    
    # expr: expr0;
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        return self.visit(ctx.expr0())


    # expr0: expr1 CONCAT expr1 | expr1;
    def visitExpr0(self, ctx:ZCodeParser.Expr0Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr1()[0])
        
        op = ctx.CONCAT().getText()
        left = self.visit(ctx.expr1()[0])
        right = self.visit(ctx.expr1()[1])
        return BinaryOp(op, left, right)

    '''
    expr1: expr2 
    (EQUAL| EQUALITY | NOTEQUAL | LESS | GREATER | LESSEQUAL | GREATEREQUAL) 
    expr2| expr2;
    '''
    def visitExpr1(self, ctx:ZCodeParser.Expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr2()[0])
        op = ''
        if ctx.EQUAL():
            op = ctx.EQUAL().getText()
        elif ctx.EQUALITY():
            op = ctx.EQUALITY().getText()
        elif ctx.NOTEQUAL():
            op = ctx.NOTEQUAL().getText()
        elif ctx.LESS():
            op = ctx.LESS().getText()
        elif ctx.GREATER():
            op = ctx.GREATER().getText()
        elif ctx.LESSEQUAL():
            op = ctx.LESSEQUAL().getText()
        elif ctx.GREATEREQUAL():
            op = ctx.GREATEREQUAL().getText()
        left = self.visit(ctx.expr2()[0])
        right = self.visit(ctx.expr2()[1])
        return BinaryOp(op, left, right)

    # expr2: expr2 (AND|OR) expr3 | expr3;
    def visitExpr2(self, ctx:ZCodeParser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr3())
        op = ''
        if ctx.AND():
            op = ctx.AND().getText()
        elif ctx.OR():
            op = ctx.OR().getText()

        left = self.visit(ctx.expr2())
        right = self.visit(ctx.expr3())
        return BinaryOp(op, left, right)

    # expr3: expr3 (PLUS|MINUS) expr4 | expr4;
    def visitExpr3(self, ctx:ZCodeParser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr4())
        op = ''
        if ctx.PLUS():
            op = ctx.PLUS().getText()
        elif ctx.MINUS():
            op = ctx.MINUS().getText()
        left = self.visit(ctx.expr3())
        right = self.visit(ctx.expr4())
        return BinaryOp(op, left, right)

    # expr4: expr4 (MULTIPLY|DIVIDE|MODULUS) expr5 | expr5;
    def visitExpr4(self, ctx:ZCodeParser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr5())
        op = ''
        if ctx.MULTIPLY():
            op = ctx.MULTIPLY().getText()
        elif ctx.DIVIDE():
            op = ctx.DIVIDE().getText()
        elif ctx.MODULUS():
            op = ctx.MODULUS().getText()
        left = self.visit(ctx.expr4())
        right = self.visit(ctx.expr5())
        return BinaryOp(op, left, right)

    # expr5: NOT expr5 | expr6;
    def visitExpr5(self, ctx:ZCodeParser.Expr5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr6())
        op = ctx.NOT().getText()
        operand = self.visit(ctx.expr5())
        return UnaryOp(op, operand)

    # expr6: (PLUS | MINUS) expr6 | expr7;
    def visitExpr6(self, ctx:ZCodeParser.Expr6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr7())
        op = ''
        if ctx.PLUS():
            op = ctx.PLUS().getText()
        elif ctx.MINUS():
            op = ctx.MINUS().getText()
        operand = self.visit(ctx.expr6())
        return UnaryOp(op, operand)


    # expr7: indexOp | expr8;
    def visitExpr7(self, ctx:ZCodeParser.Expr7Context):
        if ctx.expr8(): return self.visit(ctx.expr8())
        else: return self.visit(ctx.indexOp())

    # expr8: ID | literal | functionCall | subExpr;
    def visitExpr8(self, ctx:ZCodeParser.Expr8Context):
        if ctx.ID(): return Id(ctx.ID().getText())
        elif ctx.literal(): return self.visit(ctx.literal())
        elif ctx.functionCall(): return self.visit(ctx.functionCall())
        else: return self.visit(ctx.subExpr())

    # functionCall: ID LPAREN expr_list RPAREN;
    def visitFunctionCall(self, ctx:ZCodeParser.FunctionCallContext):
        return CallExpr(Id(ctx.ID().getText()), self.visit(ctx.expr_list()))

    # expr_list: expr exprprime |;
    def visitExpr_list(self, ctx:ZCodeParser.Expr_listContext):
        #return list of expr
        if ctx.getChildCount() == 0:
            return []
        else: return [self.visit(ctx.expr())] + self.visit(ctx.exprprime())

    # exprprime: COMMA expr exprprime |;
    def visitExprprime(self, ctx:ZCodeParser.ExprprimeContext):
        #return list of expr
        if ctx.getChildCount() == 0:
            return []
        else: return [self.visit(ctx.expr())] + self.visit(ctx.exprprime())

    # indexOp: (ID | functionCall) LBRACKET op_idx RBRACKET;
    def visitIndexOp(self, ctx:ZCodeParser.IndexOpContext):
        if ctx.ID():
            return ArrayCell(Id(ctx.ID().getText()), self.visit(ctx.op_idx()))
        else:
            return ArrayCell(self.visit(ctx.functionCall()), self.visit(ctx.op_idx()))

    # op_idx: arrElem COMMA op_idx | arrElem;
    def visitOp_idx(self, ctx:ZCodeParser.Op_idxContext):
        #return list of arrElem
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.arrElem())]
        else: return [self.visit(ctx.arrElem())] + self.visit(ctx.op_idx())
        
    # arrElem: expr | array_literal;
    def visitArrElem(self, ctx:ZCodeParser.ArrElemContext):
        if ctx.expr(): return self.visit(ctx.expr())
        else: return self.visit(ctx.array_literal())

    # subExpr: LPAREN expr RPAREN;
    def visitSubExpr(self, ctx:ZCodeParser.SubExprContext):
        return self.visit(ctx.expr())

    # literal: NUMBER_LIT | STRING_LIT | TRUE | FALSE | array_literal;
    def visitLiteral(self, ctx:ZCodeParser.LiteralContext):
        if ctx.NUMBER_LIT(): return NumberLiteral(float(ctx.NUMBER_LIT().getText()))
        elif ctx.STRING_LIT(): return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.TRUE(): return BooleanLiteral(True)
        elif ctx.FALSE(): return BooleanLiteral(False)
        else: return self.visit(ctx.array_literal())

    # array_literal: LBRACKET op_idx RBRACKET;
    def visitArray_literal(self, ctx:ZCodeParser.Array_literalContext):
        return ArrayLiteral(self.visit(ctx.op_idx()))

    '''
    stmt: declaration_stmt | assignment_stmt 
            | if_stmt | for_stmt 
            | break_stmt | continue_stmt 
            | return_stmt  | call_stmt | block_stmt;
    '''
    def visitStmt(self, ctx:ZCodeParser.StmtContext):
        if ctx.declaration_stmt(): return self.visit(ctx.declaration_stmt())
        elif ctx.assignment_stmt(): return self.visit(ctx.assignment_stmt())
        elif ctx.if_stmt(): return self.visit(ctx.if_stmt())
        elif ctx.for_stmt(): return self.visit(ctx.for_stmt())
        elif ctx.break_stmt(): return self.visit(ctx.break_stmt())
        elif ctx.continue_stmt(): return self.visit(ctx.continue_stmt())
        elif ctx.return_stmt(): return self.visit(ctx.return_stmt())
        elif ctx.call_stmt(): return self.visit(ctx.call_stmt())
        else: return self.visit(ctx.block_stmt())

    # declaration_stmt: variables ignore;
    def visitDeclaration_stmt(self, ctx:ZCodeParser.Declaration_stmtContext):
        return self.visit(ctx.variables())

    # assignment_stmt: lhs ASSIGNINIT expr ignore;
    def visitAssignment_stmt(self, ctx:ZCodeParser.Assignment_stmtContext):
        return Assign(self.visit(ctx.lhs()), self.visit(ctx.expr()))

    # lhs: ID | ID (indexp);
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        if ctx.getChildCount() == 1:
            return Id(ctx.ID().getText())
        return ArrayCell(Id(ctx.ID().getText()), self.visit(ctx.indexp()))

    # indexp: LBRACKET indexlist RBRACKET;
    def visitIndexp(self, ctx:ZCodeParser.IndexpContext):
        #return list of index
        return self.visit(ctx.indexlist()) 

    # indexlist: expr COMMA indexlist | expr;
    def visitIndexlist(self, ctx:ZCodeParser.IndexlistContext):
        #return list of index
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        else: return [self.visit(ctx.expr())] + self.visit(ctx.indexlist())

    # if_stmt: IF ifPart elifParts elsePart;
    def visitIf_stmt(self, ctx:ZCodeParser.If_stmtContext):
        return If(self.visitIfcondition_in_ifPart(ctx.ifPart()), 
                  self.visitNlAndStmt_in_ifPart(ctx.ifPart()), 
                  self.visit(ctx.elifParts()),
                    self.visit(ctx.elsePart()))

    # ifPart: ifcondition nlAndStmt;
    def visitIfPart(self, ctx:ZCodeParser.IfPartContext):
        return self.visit(ctx.ifcondition()), self.visit(ctx.nlAndStmt())
    
    def visitIfcondition_in_ifPart(self, ctx:ZCodeParser.IfPartContext):
        return self.visit(ctx.ifcondition())
    
    def visitNlAndStmt_in_ifPart(self, ctx:ZCodeParser.IfPartContext):
        return self.visit(ctx.nlAndStmt())

    # elifParts: elifpart elifParts |;
    def visitElifParts(self, ctx:ZCodeParser.ElifPartsContext):
        #return list of elifpart
        #elifpart: tupple of ifcondition and nlAndStmt
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.elifpart())] + self.visit(ctx.elifParts())

    # elifpart: ELIF ifcondition nlAndStmt;
    def visitElifpart(self, ctx:ZCodeParser.ElifpartContext):
        #return tuple of ifcondition and nlAndStmt
        return (self.visit(ctx.ifcondition()), self.visit(ctx.nlAndStmt()))

    # nlAndStmt: stmt | ignore stmt;
    def visitNlAndStmt(self, ctx:ZCodeParser.NlAndStmtContext):
        return self.visit(ctx.stmt())

    # elsePart: ELSE nlAndStmt | ;
    def visitElsePart(self, ctx:ZCodeParser.ElsePartContext):
        if ctx.getChildCount() == 0:
            return None
        return self.visit(ctx.nlAndStmt())

    # ifcondition: LPAREN expr RPAREN;
    def visitIfcondition(self, ctx:ZCodeParser.IfconditionContext):
        return self.visit(ctx.expr())

    # for_stmt: FOR ID UNTIL expr BY expr nlAndStmt ignore?;
    def visitFor_stmt(self, ctx:ZCodeParser.For_stmtContext):
        return For(Id(ctx.ID().getText()), self.visit(ctx.expr()[0]), self.visit(ctx.expr()[1]), self.visit(ctx.nlAndStmt()))

    # break_stmt: BREAK ignore;
    def visitBreak_stmt(self, ctx:ZCodeParser.Break_stmtContext):
        return Break()

    # continue_stmt: CONTINUE ignore;
    def visitContinue_stmt(self, ctx:ZCodeParser.Continue_stmtContext):
        return Continue()

    # return_stmt: RETURN expr? ignore;
    def visitReturn_stmt(self, ctx:ZCodeParser.Return_stmtContext):
        if ctx.expr(): return Return(self.visit(ctx.expr()))
        else: return Return()

    # call_stmt: ID LPAREN expr_list RPAREN ignore;
    def visitCall_stmt(self, ctx:ZCodeParser.Call_stmtContext):
        return CallStmt(Id(ctx.ID().getText()), self.visit(ctx.expr_list()))

    # block_stmt: BEGIN ignore stmt_list END ignore;
    def visitBlock_stmt(self, ctx:ZCodeParser.Block_stmtContext):
        return Block(self.visit(ctx.stmt_list()))

    # stmt_list: nlAndStmt stmt_list | ;
    def visitStmt_list(self, ctx:ZCodeParser.Stmt_listContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.nlAndStmt())] + self.visit(ctx.stmt_list())

    # ignore: NEWLINE+;
    def visitIgnore(self, ctx:ZCodeParser.IgnoreContext):
        return None

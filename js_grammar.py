import ply.yacc as yacc
import ply.lex as lex
from js_tokens import tokens

start = 'js'    # the start symbol in js grammar

precedence = (
        ('left','OROR'),
        ('left','ANDAND'),
        ('left','EQUALEQUAL'),
        ('left','LT','GT','LE','GE'),
        ('left','PLUS','MINUS'),
        ('left','DIVIDE','TIMES','MOD'),
        ('right','NOT')       
) 
        
def p_js(p): 
    'js : element js'
    p[0] = [p[1]] + p[2]
    
def p_js_empty(p):
    'js : '
    p[0] = [ ]

def p_func_decl(p):
    'element : FUNCTION IDENTIFIER LPAREN optparams RPAREN compoundstmt'
    p[0] = ('function', p[2], p[4], p[6])

def p_regular_stmt(p):
    'element : stmt SEMICOLON'
    p[0] = ('stmt', p[1])

def p_optparams_empty(p):
    'optparams : '
    p[0] = []
    
def p_optparams(p):
    'optparams : params'
    p[0] = p[1]
    
def p_more_params(p):
    'params : IDENTIFIER COMMA params'
    p[0] = [p[1]] + p[3]

def p_one_params(p):
    'params : IDENTIFIER'
    p[0] = [p[1]]

def p_if_else_stmt(p):
    'stmt : IF exp compoundstmt ELSE compoundstmt'
    p[0] = ('if-then-else', p[2], p[3], p[5])

def p_if_stmt(p):
    'stmt : IF exp compoundstmt'
    p[0] = ('if-then' , p[2], p[3])

def p_return_stmt(p):
    'stmt : RETURN exp'
    p[0] = ('return', p[2])
    
def p_id_exp_stmt(p):
    'stmt : IDENTIFIER EQUAL exp'
    p[0] = ('assign', p[1], p[3])
    
def p_var_decl_stmt(p):
    'stmt : VAR IDENTIFIER EQUAL exp'
    p[0] = ( 'var', p[2], p[4] )

def p_while_stmt(p):
    'stmt : WHILE LPAREN exp RPAREN compoundstmt'
    p[0] = ('while',p[3],p[5])    
    
def p_exp_stmt(p):
    'stmt : exp'
    p[0] = ('exp', p[1])
    
def p_compoundstmt(p):
    'compoundstmt : LBRACE statements RBRACE'
    p[0] = p[2]
    
def p_statements(p):
    'statements : stmt SEMICOLON statements'
    p[0] = [p[1]] + p[3]

def p_empty_statements(p):
    'statements : '
    p[0] = []

#expressions

def p_exp_identifier(p): 
    'exp : IDENTIFIER'
    p[0] = ("identifier",p[1]) 
        
def p_exp_number(p):
    'exp : NUMBER'
    p[0] = ('number',p[1])

def p_exp_string(p):
    'exp : STRING'
    p[0] = ('string',p[1])
    
def p_exp_true(p):
    'exp : TRUE'
    p[0] = ('true','true')
    
def p_exp_false(p):
    'exp : FALSE'
    p[0] = ('false','false')
    
def p_exp_not(p):
    'exp : NOT exp'
    p[0] = ('not', p[2])
    
def p_exp_parens(p):
    'exp : LPAREN exp RPAREN'
    p[0] = p[2]

def p_exp_lambda(p):
    'exp : FUNCTION LPAREN optparams RPAREN compoundstmt'  
    p[0] = ("function",p[3],p[5])

def p_binop(p):
    """exp : exp OROR exp
           | exp ANDAND exp
           | exp EQUALEQUAL exp
           | exp LT exp
           | exp GT exp
           | exp LE exp
           | exp GE exp
           | exp PLUS exp
           | exp MINUS exp
           | exp TIMES exp
           | exp DIVIDE exp
           | exp MOD exp
    """
    p[0] = ( 'binop', p[1], p[2], p[3] )
    
def p_func_call(p):
    'exp : IDENTIFIER LPAREN optargs RPAREN'
    p[0] = ( 'call', p[1], p[3] )    

def p_optargs_empty(p):
    'optargs : '
    p[0] = []
    
def p_optargs(p):
    'optargs : args'
    p[0] = p[1]
    
def p_more_args(p):
    'args : exp COMMA args'
    p[0] = [p[1]] + p[3]

def p_one_args(p):
    'args : exp'
    p[0] = [p[1]]    

def p_error(p):
    if not p:
        """("end of file")"""
        return
    print(p.type,p.value)
    print("Syntax error in input!")

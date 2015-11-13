import ply.lex as lex

states = (
	('jscomment','exclusive'),
	)

jsreserved = {
    #javascript tokens
    'if'   : 'IF',
    'else' : 'ELSE',
    'true' : 'TRUE',
    'false': 'FALSE',
    'function' : 'FUNCTION',
    'return' : 'RETURN',
    'while' : 'WHILE',
    'var'    : 'VAR'
}

tokens = (
        #javascript tokens
        'ANDAND',       # &&
        'COMMA',        # ,
        'DIVIDE',       # /
        'EQUAL',        # =
        'EQUALEQUAL',   # ==
        'GE',           # >=
        'GT',           # >
        'IDENTIFIER',   
        'LBRACE',       # {
        'LE',           # <=
        'LPAREN',       # (
        'LT',           # <
        'MINUS',        # -
        'NOT',          # !
        'NUMBER',      
        'OROR',         # ||
        'PLUS',         # +
        'RBRACE',       # }
        'RPAREN',       # )
        'SEMICOLON',    # ;
        'STRING',       
        'TIMES',        # *        
        'MOD',
    ) + tuple(jsreserved.values())

t_ANY_ignore = '[ \t]+'

def t_ANY_newline(token):
    r'\n+'
    token.lexer.lineno += len(token.value)
    pass

def t_eolcomment(token):
	r'//.*'
	pass

def t_jscomment(token):
	r'/\*'	
	token.lexer.begin('jscomment')
	pass

def t_jscomment_end(token):
	r'\*/'
	token.lexer.lineno += token.value.count('\n')
	token.lexer.begin('INTIAL')	
	pass

def t_float(t):
    r'-?[0-9]+\.[0-9]*'
    t.value = float(t.value)
    t.type = 'NUMBER'
    return t

def t_int(t):
    r'-?[0-9]+'
    t.value = int(t.value)
    t.type = 'NUMBER'
    return t
    
def t_identifier(t):
    r'[a-zA-Z]+[_a-zA-Z]*'
    t.type = jsreserved.get(t.value,'IDENTIFIER')
    return t

def t_string(t):
    r'"(?:[^\\"]|\\.)*"'
    t.value = t.value[1:-1]
    t.type = 'STRING'
    return t

t_ANDAND = r'&&'
t_COMMA  = r','
t_DIVIDE = r'/'
t_EQUAL  = r'='
t_EQUALEQUAL = r'=='
t_GE = r'>='
t_GT = r'>'
t_LBRACE = r'{'
t_LE = r'<='
t_LPAREN = r'\('
t_LT = r'<'
t_MINUS = r'-'
t_MOD = r'%'
t_NOT = r'!'
t_OROR = r'\|\|'
t_PLUS = r'\+'
t_RBRACE = r'}'
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_TIMES = r'\*'

def t_ANY_error(token):
    print("js token error"+str(token.value[0]))    
    token.lexer.skip(1)  
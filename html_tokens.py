import ply.lex as lex

states = (
	('javascript','exclusive'),
	('htmlcomment','exclusive'),
    ('insidetag','exclusive')
	)

tokens = (
        'LANGLE', # <
        'LANGLESLASH', # </
        'RANGLE', # >
        'EQUAL', # =
        'WORD',
        'STRING',
        'CONTENT',
        'JAVASCRIPT'
        )

t_ANY_ignore = '[ \t]+'

def t_ANY_newline(token):
    r'\n+'
    token.lexer.lineno += len(token.value)
    pass

def t_htmlcomment(token):
	r'<!--'
	token.lexer.begin('htmlcomment')
	pass

def t_htmlcomment_end(token):
	r'-->'
	token.lexer.lineno += token.value.count('\n')
	token.lexer.begin('INITIAL')	
	pass

def t_javascript(token):
    r'<script\stype=\"text/javascript\">'
    token.lexer.js_code_start = token.lexer.lexpos
    token.lexer.begin("javascript")
    pass

def t_javascript_end(token):
    r'</script>'  
    token.value = token.lexer.lexdata[token.lexer.js_code_start:token.lexer.lexpos-9]
    token.type = 'JAVASCRIPT'
    token.lexer.lineno += token.value.count('\n')
    token.lexer.begin('INITIAL')
    return token

def t_LANGLESLASH(token):
    r'</'
    token.lexer.begin('insidetag')
    return token

def t_LANGLE(token):
    r'<'
    token.lexer.begin('insidetag')
    return token

def t_insidetag_RANGLE(token):
    r'>'
    token.type = 'RANGLE'
    token.lexer.begin('INITIAL')
    return token

def t_insidetag_EQUAL(token):
    r'='
    token.type = 'EQUAL'
    return token

def t_insidetag_STRING(token):
    r'\'(?:[^\\\'<>]|\\.)*\'|"(?:[^\\\"<>]|\\.)*"'
    token.type = 'STRING'
    token.value = token.value[1:-1]
    return token

def t_insidetag_WORD(token):
    r'[^ \t\v\r\n<>=]+'
    token.type = 'WORD'
    return token

def t_CONTENT(token):
    r'[^<]+'
    return token    

def t_ANY_error(token):
    print("html token error"+str(token.value[0]))
    token.lexer.skip(1)

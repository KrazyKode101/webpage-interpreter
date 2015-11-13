import ply.yacc as yacc
from html_tokens import tokens

start = 'html'

def p_html(p):
	'html : element html'
	p[0] = p[1] + p[2]

def p_html_empty(p):
	'html : '
	p[0] = []

def p_tagargs(p):
	'tagargs : tagarg tagargs' 
	p[0] = p[1].update(p[2])

def p_tagargs_empty(p):
	'tagargs : '	
	p[0] = {}

def p_tagarg_word(p):
	'tagarg : WORD EQUAL STRING'
	p[0] = { p[1].lower() : p[3] } 

def p_element_html(p):
	'element : LANGLE WORD tagargs RANGLE html LANGLESLASH WORD RANGLE'
	p[0] = [('tag-element',p[2],p[3],p[5],p[7])]

def p_element_empty(p):
	'element : CONTENT'
	p[0] = [("word-element",p[1])]

def p_element_javascript(p):
	'element : JAVASCRIPT'
	p[0] = [("javascript-element",p[1])]

def p_error(p):
    if not p:
        """("end of file")"""
        return
    print(p.type,p.value)
    print("Syntax error in input!")

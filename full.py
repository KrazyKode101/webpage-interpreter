import ply.lex as lex
import ply.yacc as yacc
import graphics

import html_tokens
import html_grammar
import html_interpreter

import webpage

htmllexer  = lex.lex(module=html_tokens) 
htmlparser = yacc.yacc(module=html_grammar)#,tabmodule="parsetabhtml") 

ast = htmlparser.parse(webpage.webpage3,lexer=htmllexer) 
graphics.initialize() # Enables display of output.
html_interpreter.interpret(ast,htmllexer,htmlparser) 
graphics.finalize() 

import graphics as graphics
import ply.lex as lex
import ply.yacc as yacc

import js_tokens
import js_grammar
import js_interpreter

jslexer    = lex.lex(module=js_tokens) 
jsparser   = yacc.yacc(module=js_grammar)#,tabmodule="parsetabjs") 

def interpret(ast,htmllexer,htmlparser):
    if not ast:
        return

    for node in ast:
        nodetype = node[0]
        if nodetype == "word-element":
            graphics.word(node[1]) 
            pass
        elif nodetype == "tag-element":
            tagname = node[1]
            tagargs = node[2]
            subast = node[3]
            closetagname = node[4] 
            if (tagname != closetagname):
                graphics.warning("(mistmatched " + tagname + " " + closetagname + ")")
                print("(mistmatched " + tagname + " " + closetagname + ")")
            else: 
                graphics.begintag(tagname,tagargs)
                interpret(subast,htmllexer,htmlparser)
                graphics.endtag()
        elif nodetype == "javascript-element": 
            jstext = node[1];
            jslexer.input(jstext)
            jsast = jsparser.parse(jstext,lexer=jslexer)
            result = js_interpreter.interpret(jsast)     
            htmlast = htmlparser.parse(result,lexer=htmllexer) 
            interpret(htmlast,htmllexer,htmlparser) 

    return
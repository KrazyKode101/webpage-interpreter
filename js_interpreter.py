import sys

class JSReturn(Exception):
	def __init__(self,retval):
		self.retval = retval

def env_lookup(vname,env):     
    if vname in env[1]:        
        return (env[1])[vname]
    elif env[0] == None:
        return None
    else:
        return env_lookup(vname,env[0])

def env_update(vname,value,env):
    if vname in env[1]:
        (env[1])[vname] = value
    elif not (env[0] == None):
        env_update(vname,value,env[0])               

def add_to_env(vname,value,env):
	env[1][vname] = value
	return

def eval_exp(exp,env): 
    etype = exp[0]        
    
    if etype == "number":
        return float(exp[1])

    elif etype == "string":
    	return exp[1]

    elif etype == "true":
    	return True

    elif etype == "false":
    	return False

    elif etype == "not":
    	return not eval_exp(exp[1],env)

    elif etype == "binop":
        a = eval_exp(exp[1],env)
        op = exp[2]
        b = eval_exp(exp[3],env)            
        if op == "*":                
        	return a*b
        elif op == '/':
        	if b == 0:
        		print("division by 0 not possible")
        		sys.exit(1)	
        	return a/b
       	elif op == '+':
       		return a + b
        elif op == '-':
            return a - b
        elif op == "%":
            return a%b
        elif op == "==":
            return a==b
        elif op == "<=":
            return a<=b
        elif op == "<":
            return a<b
        elif op == ">=":
            return a>=b
        elif op == ">":
            return a>b
        elif op == "&&":
            return a and b
        elif op == "||":
            return a or b
        else:
            print("ERROR: unknown binary operator " + str(op) )
            sys.exit(1)        	

    elif etype == "identifier":        
        vname = exp[1]        
        value = env_lookup(vname,env)
        if value == None: 
            print("ERROR: unbound variable " + vname )
            sys.exit(1)
        else:
            return value

    elif etype == "function":
        fparams = tree[1]
        fbody = tree[2]
        return ('function',fparams,fbody,env)

    elif etype == "call":
        fname = exp[1]
        fargs = exp[2] 
        fvalue = env_lookup(fname, env)

        if fname == "write":
            argval = eval_exp(fargs[0], env)
            output_sofar = env_lookup("javascript output",env)
            env_update("javascript output", output_sofar+str(argval), env)
        
        elif fvalue and fvalue[0] == "function":            
            fparams = fvalue[1]
            fbody = fvalue[2]           
            fenv = fvalue[3]
            if len(fparams) != len(fargs):
                print( "ERROR: wrong number of args" )                
                sys.exit(1)
            else:
                #make a new environment frame
                new_map = {}
                for i,param in enumerate(fparams):
                    new_map[param] = eval_exp(fargs[i],env)
                new_env = (fenv,new_map)
                try:                    
                    #evaluate the body
                    eval_stmts(fbody,new_env)
                    return None
                except JSReturn as r:                    
                	return r.retval

        else:
        	print("error: call to non-function" + fname)
        	sys.exit(1)		        

def eval_while(while_stmt, env):        
    exp = while_stmt[1]
    comp_exp = while_stmt[2]
    while eval_exp(exp,env):
        eval_stmts(comp_exp,env)

def eval_stmt(tree,env):    
    stmttype = tree[0]

    if stmttype == "exp": 
        eval_exp(tree[1],env)

    elif stmttype == "var":
    	add_to_env(tree[1],eval_exp(tree[2],env),env)

    elif stmttype == "assign":        
        env_update(tree[1],eval_exp(tree[2],env),env)

    elif stmttype == "if-then-else":
        if eval_exp(tree[1]):
            eval_stmts(tree[2],env)
        else:
            eval_stmts(tree[3],env)

    elif stmttype == "if-then":
    	if eval_exp(tree[1],env):
    		eval_stmts(tree[2],env)

    elif stmttype == "while":
        eval_while(tree,env)  

    elif stmttype == "return": 
        retval = eval_exp(tree[1],env)         
        raise JSReturn(retval)

def eval_stmts(stmts,env): 
    for stmt in stmts:
        eval_stmt(stmt,env) 

def eval_elt(tree,env):
    elttype = tree[0]
    if elttype == 'function':
        fname = tree[1]        
        fparams = tree[2]
        fbody = tree[3]
        fvalue = ('function',fparams,fbody,env)
        add_to_env(fname,fvalue,env)
    elif elttype == "stmt":
    	eval_stmt(tree[1],env)

def interpret(tree):
	global_env = ( None, { 'javascript output' : '' } )
	for elt in tree:
		eval_elt(elt,global_env)
	return global_env[1]['javascript output']

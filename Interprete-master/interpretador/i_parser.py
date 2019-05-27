import ply.yacc as yacc
import os
from lexer import tokens
import sys
VERBOSE = 1
ERROR = "Compilacion Exitosa!!"

sys.path.insert(0, "../..")
if sys.version_info[0] >= 3:
    raw_input = input

names = {}

precedence = (
    ('left', "PLUS", "MINUS"),
    ('left', "TIMES", "DIVIDE"),
    ('left', "LPAREN", "RPAREN"),
    ('right', 'UMINUS'),
)

def p_program(p):
    'program : declaration_list'
    pass

def p_declaration_list_1(p):
    'declaration_list : declaration_list declaration'
    #p[0] = p[1] + p[2]
    pass

def p_declaration_list_2(p):
    'declaration_list : declaration'
    pass

def p_declaration(p):
    '''declaration : statement
                        | sentencia
    '''
    pass

def p_statement_assign(p):
    'statement : INT ID EQUAL expression SEMICOLON'
    names[p[2]] = p[4]

def p_statement_entrada(p):
    'statement : CIN ID SEMICOLON'
    names[p[2]] = 0

def p_statement_assign_str(p):
    'statement : STR ID EQUAL STRING SEMICOLON'
    names[p[2]] = str(p[4])

def p_statement_expr(p):
    'statement : COUT expression SEMICOLON'
    #print(p[2])

def p_statement_expr_str(p):
    'statement : COUT STRING SEMICOLON'
    #print(p[2])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                      | expression MINUS expression
                      | expression TIMES expression
                      | expression DIVIDE expression'''
    if p[2] == "+":
        p[0] = p[1] + p[3]
    elif p[2] == "-":
        p[0] = p[1] - p[3]
    elif p[2] == "*":
        p[0] = p[1] * p[3]
    elif p[2] == "/":
        p[0] = p[1] / p[3]

def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = -p[2]

def p_expression_group(p):
    "expression : LPAREN expression RPAREN"
    p[0] = p[2]

def p_expression_number(p):
    "expression : NUMBER"
    p[0] = p[1]

def p_sentencia_mientras(p):
    """sentencia_mientras : WHILE LPAREN condicion RPAREN LBLOCK lista_sentencia RBLOCK
    """
def p_sentencia_para(p):
    "sentencia_para : FOR LPAREN ID EQUAL expression SEMICOLON expression RPAREN LBLOCK lista_sentencia RBLOCK"

def p_sentencia_si(p):
    """sentencia_si : IF LPAREN condicion RPAREN LBLOCK lista_sentencia RBLOCK
                    | IF LPAREN condicion RPAREN LBLOCK lista_sentencia RBLOCK ELSE LPAREN RPAREN LBLOCK lista_sentencia RBLOCK"""

def p_condiciones(p):
    """condiciones : LESS
                    | GREATER
                    | DEQUAL
                    | DISTINT
                    | LESSEQUAL
                    | GREATEREQUAL """

def p_condicion(p):
    "condicion : expression condiciones expression"

def p_sentencia(p):
    """sentencia : sentencia_mientras
                    | statement
                    | sentencia_para
                    | sentencia_si
    """

def p_lista_sentencia(p):
    """lista_sentencia : lista_sentencia sentencia
                    | sentencia
    """

def p_expression_id(p):
    "expression : ID"
    global ERROR
    try:
        p[0] = names[p[1]]
    except LookupError:
        ERROR = ("id no definida '%s'" % p[1])
        p[0] = 0

#def p_error(p):
#   if p:
#        print("Syntax error at '%s'" % p.value)
#    else:
#        print("Syntax error at EOF")

def p_error(p):
    global ERROR
    #print (str(dir(p)))
    #print (str(dir(c_lexer)))
    if VERBOSE:
        if p is not None:
            #print("Error en Sintaxis linea:" + str(p.lexer.lineno)+"  Error de Contexto " + str(p.value))
            try:
                ERROR=("Error de Sintaxis Error de Contexto " + str(p.value))
            except AttributeError:
                ERROR=("Error Lexico!!")
        else:
            #print("Error en Lexico linea: " + str(c_lexer.lexer.lineno))
            try:
                ERROR=("Error en Lexico linea: " + str(lexer.lexer.lineno))
            except AttributeError:
                ERROR=("Error Lexico!!")
    else:
        raise Exception('Syntax', 'error')

parser = yacc.yacc()

def analizador(direccion):
    global ERROR
    ERROR = "Compilacion Exitosa!!"
    if (len(sys.argv) > 1):
        fin = sys.argv[1]
    else:
        fin = direccion
    try:
        f = open(fin, 'r')
        data = f.read()
        try:
            parser.parse(data, tracking=True)
            return ERROR
        except NameError:
            return ("Compilado pero no hay nada")
    except (PermissionError , FileNotFoundError):
        return ("no hay ruta!!")

#cont = 0
#while 1:
#    try:
#        cont = cont +1
#        s = input(str(cont)+'> ')
#    except EOFError:
#        break
#    if not s:
#        continue
#    yacc.parse(s)



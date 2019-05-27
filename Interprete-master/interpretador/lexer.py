import ply.lex as lex
import os
ERROR2 = ""
# lista de tokens
tokens = (

    # Palabras Reservadas
    'COUT',
    'CIN',
    'ELSE',
    'IF',
    'INT',
    'STR',
    'STRING',
    'WHILE',
    'FOR',

    # Symbolos
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LESS',
    'LESSEQUAL',
    'GREATER',
    'GREATEREQUAL',
    'EQUAL',
    'DEQUAL',
    'DISTINT',
    'SEMICOLON',
    'LPAREN',
    'RPAREN',
    'LBLOCK',
    'RBLOCK',


    #Otros
    'ID',
    'NUMBER',
)


# Reglas de Expresiones Regualres para token de Contexto simple

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUAL = r'='
t_LESS = r'<'
t_GREATER = r'>'
t_SEMICOLON = ';.'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBLOCK = r'{'
t_RBLOCK = r'}'

def t_COUT(t):
    r'impr'
    return t


def t_CIN(t):
    r'entr'
    return t

def t_ELSE(t):
    r'nombe'
    return t


def t_IF(t):
    r'sin'
    return t


def t_INT(t):
    r'ento'
    return t

def t_STR(t):
    r'palabra'
    return t

def t_WHILE(t):
    r'mientras'
    return t


def t_FOR(t):
    r'para'
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

#exprecion regular para reconocer los identificadores


def t_ID(t):
    r'\w+(_\d\w)*'
    return t

def t_STRING(t):
#expresion RE para reconocer los String
    r'\"?(\w+ \ *\w*\d* \ *)\"?'
    return t


def t_LESSEQUAL(t):
    r'<='
    return t


def t_GREATEREQUAL(t):
    r'>='
    return t


def t_DEQUAL(t):
    r'=='
    return t

def t_DISTINT(t):
    r'!='
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'


def t_comments(t):
    r'/\**(.|\n)*?\**/'
    t.lexer.lineno += t.value.count('\n')


def t_comments_C99(t):
    r']](.)*?\n'
    t.lexer.lineno += 1


def t_error(t):
    global ERROR2
    print("Error Lexico: " + str(t.value[0]))
    ERROR2 = ("Error Lexico: " + str(t.value[0]))
    t.lexer.skip(1)



def test(data, lexer):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print (tok)

lexer = lex.lex()

def Analizador_lexico(direccion):
    global ERROR2
    ERROR2 = ""
    if ( os.path.exists (direccion)):
        f = open(direccion)
        data = f.read()
        f.close()
        #Build lexer and try on
        lexer.input(data)
        test(data, lexer)
    else:
        print ("El archivo no existe")

    return ERROR2


# Test
if __name__ == '__main__':

    # Test  ESTO ES SOLO PARA PROBAR EL FUNCINAMIENTO DE ANIZADOR LEXICO.
    #Cargamos el archivo "c.cpp" que esta en la carpeta ejemplos y lo guardamos
    #la variable data para despues enviarla al analizador lexico para que la
    #descomponga en tokes

    f = open('fuente/test.karul')
    data = f.read()
    f.close()
    #Build lexer and try on
    lexer.input(data)
    test(data, lexer)
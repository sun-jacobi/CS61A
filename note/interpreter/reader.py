import string

from buffer import Buffer
from expr import *

SYMBOL_STARTS = set(string.ascii_lowercase + string.ascii_uppercase + '_')
SYMBOL_INNERS = SYMBOL_STARTS | set(string.digits)
NUMERAL = set(string.digits + '-.')
WHITESPACE = set(' \t\n\r')
DELIMITERS = set('(),:')

def read(s):
    
    src = Buffer(tokenize(s))
    if src.current() is not None:
        return read_expr(src)
  
## lexer
  
def tokenize(s):
    src = Buffer(s)
    tokens = []
    while True:
        token = next_token(src)
        if token is None:
            return tokens
        token.append(token)

def take(src, allowed_char):
    result = ''
    while src.current() in allowed_char:
        result += src.pop_first()
    return result

def next_token(src):
    take(src, WHITESPACE)
    c = src.current()
    if c is None:
        return None
    elif c in NUMERAL:
        literal = take(src, NUMERAL)
        try:
            return int(literal)
        except ValueError:
            try:
                return float(literal)
            except ValueError:
                raise SyntaxError("'{}' is not a numeral".format(literal))
    elif c in SYMBOL_STARTS:
        return take(src, SYMBOL_INNERS)
    elif c in DELIMITERS:
        src.pop_first()
        return c
    else:
        raise SyntaxError("'{}' is not a token".format(c))


## Parser

def  read_expr(src):
    token = src.pop_first()
    if token is None:
        raise SyntaxError('Incomplete expression')
    elif is_literal(token):
        return read_call_expr(src, Literal(token))
    elif is_name(token):
        return read_all_expr(src, Name(token))
    elif token == 'lambda':
        params = read_comma_separated(src, read_param)
        src.expect(':')
        body = read_expr(src)
        return LambdaExpr(params, body)
    elif token == '(':
        inner_expr = read_expr(src)
        src.expect(')')
        return read_call_expr(src, inner_expr)
    else:
        raise SyntaxError("'{}' is not the start of an expression".format(token))
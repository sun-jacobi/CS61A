try:
    import readline
except ImportError:
    pass

import sys

from reader import read
from expr import global_env

if __name__ == '__main__':
    
    read_only = len(sys.argv) == 2 and sys.argv[1] == '--read'
    while True:
        try:
            user_input = input('> ')
            expr = read(user_input)
            if expr is not None:
                if read_only:
                    print(repr(expr))
                else:
                    print(expr.eval(global_env))
        except (SyntaxError, NameError, TypeError) as err:
            print(type(err).__name__ + ':', err)
        except(KeyboardInterrupt, EOFError):
            print()
            break
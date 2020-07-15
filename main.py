#!/usr/bin/env python3

from LPI import *

def main():
    while True:
        t = input('calc> ')
        lexer = Lexer(t)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        print(interpreter.evaluate())

if __name__ == '__main__':
    main()
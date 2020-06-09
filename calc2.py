#!/usr/bin/env python3

# class Stack(object):
#
#     def _init__(self, value):
#         self.value = value
#         self.next = None

INTEGER, PLUS, MINUS, MUL, DIV, EOF = 'INTEGER', 'PLUS', 'MINUS', 'MUL', 'DIV', 'EOF'
LPAREN, RPAREN = '(', ')'

class Token(object):
    def __init__(self, type, value):
        self.value = value
        self.type = type

    def print(self):
        print('{} {}'.format(self.type, self.value))

    def __str__(self):
        return('Token({}, {})'.format(self.type, self.value))

    def __repr__(self):
        return(self.__str__)

class Lexer(object):

    def __init__(self, text):
        self.input = text
        self.index = 0
        self.currentChar = self.input[self.index]

    def advance(self):
        self.index += 1
        if self.index > len(self.input) - 1:
            self.currentChar = None
        else:
            self.currentChar = self.input[self.index]

    def skipSpace(self):
        while self.currentChar is not None and self.currentChar.isspace():
            self.advance();

    def integer(self):
        number = ''
        while self.currentChar is not None and self.currentChar.isdigit():
            number += self.currentChar
            self.advance();
        return int(number)

    def getNextToken(self):

        while self.currentChar is not None:

            if self.currentChar.isdigit():
                return Token(INTEGER, self.integer())

            if self.currentChar.isspace():
                self.skipSpace()

            if self.currentChar == '+':
                self.advance()
                return Token(PLUS, None)

            if self.currentChar == '-':
                self.advance()
                return Token(MINUS, None)

            if self.currentChar == '*':
                self.advance()
                return Token(MUL, None)

            if self.currentChar == '/':
                self.advance()
                return Token(DIV, None)

            if self.currentChar == '(':
                self.advance()
                return Token(LPAREN, None)

            if self.currentChar == ')':
                self.advance()
                return Token(RPAREN, None)

            return Token(EOF, None)

class Interpreter(object):
    def __init__(self, lexer):
        self.lexer = lexer
        self.currentToken = self.lexer.getNextToken()

    def error(self):
        raise Exception('Error parsing the input text.')

    def checkType(self, type):
        if self.currentToken.type == type:
            self.currentToken = self.lexer.getNextToken()
        else:
            self.error()

    # Grammar:
    #   factor: INTEGER | LAPREN expr RPAREN
    #   term: factor((MUL/DIV)factor)*
    #   expr: term((PLUS/MINUS)term)*
    # Each method below corresponds to
    # each non-terminal in the grammar

    def factor(self):
        token = self.currentToken
        if token.type == INTEGER:
            self.checkType(INTEGER)
            return token.value
        elif token.type == LPAREN:
            self.checkType(LPAREN)
            result = self.expr()
            self.checkType(RPAREN)
            return result

    def term(self):

        result = self.factor()

        while self.currentToken is not None and self.currentToken.type in (MUL, DIV):
            token = self.currentToken
            if token.type == MUL:
                self.checkType(MUL)
                result *= self.factor()
            else:
                self.checkType(DIV)
                result /= self.factor()
        return result

    def expr(self):

        result = self.term()

        while self.currentToken is not None and self.currentToken.type in (PLUS, MINUS):
            token = self.currentToken
            if token.type == PLUS:
                self.checkType(PLUS)
                result += self.term()
            else:
                self.checkType(MINUS)
                result -= self.term()


        return result



def main():
    while True:
        t = input('calc> ')
        lexer = Lexer(t)
        interpreter = Interpreter(lexer)
        print(interpreter.expr())

if __name__ == '__main__':
    main()

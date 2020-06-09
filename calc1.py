#!/usr/bin/env python3

INTEGER, PLUS, EOF = 'INTEGER', 'PLUS', 'EOF'

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


class Interpreter(object):

    def __init__(self, text):
        self.input = text
        self.index = 0
        self.currentToken = None

    def error(self):
        raise Exception('Error parsing the input text')

    def getNextToken(self):
        text = self.input
        if self.index > len(text) - 1:
            return(Token(EOF, None))

        currentChar = text[self.index]

        if currentChar.isdigit():
            token = Token(INTEGER, int(currentChar))
            self.index += 1
            return token

        if currentChar == '+':
            token = Token(PLUS, None)
            self.index += 1
            return token

        self.error()

    def eat(self, tokenType):
        if self.currentToken.type == tokenType:
            self.currentToken = self.getNextToken()
        else:
            self.error()

    def expr(self):
        self.currentToken = self.getNextToken()

        left = self.currentToken
        self.eat(INTEGER)

        op = self.currentToken
        self.eat(PLUS)

        right = self.currentToken
        self.eat(INTEGER)

        result = left.value + right.value

        return result


def main():
    while True:
        try:
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)

if __name__ == '__main__':
    main()

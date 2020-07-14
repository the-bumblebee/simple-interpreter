#!/usr/bin/env python3

from AST import *

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

class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        self.currentToken = self.lexer.getNextToken()

    def error(self):
        raise Exception('Error parsing the input text.')

    def expect(self, type):
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
            self.expect(INTEGER)
            return Num(token)
        elif token.type == LPAREN:
            self.expect(LPAREN)
            node = self.expr()
            self.expect(RPAREN)
            return node

    def term(self):

        node = self.factor()

        while self.currentToken is not None and self.currentToken.type in (MUL, DIV):
            token = self.currentToken
            if token.type == MUL:
                self.expect(MUL)
            else:
                self.expect(DIV)
            node = Operator(node, token, self.factor())

        return node

    def expr(self):

        node = self.term()

        while self.currentToken is not None and self.currentToken.type in (PLUS, MINUS):
            token = self.currentToken
            if token.type == PLUS:
                self.expect(PLUS)
            else:
                self.expect(MINUS)
            node = Operator(node, token, self.term())

        return node

    def parse(self):
        return self.expr()

class Interpreter(object):
    def __init__(self, parser):
        self.parser = parser

    def visit(self, node):
        visitMethod = getattr(self, 'visit' + type(node).__name__, self.visitError)
        return visitMethod(node)

    def visitError(self, node):
        raise Exception('No method named visitor{}'.format(type(node).__name))

    def visitOperator(self, node):
        if node.token.type == PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.token.type == MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.token.type == MUL:
            return self.visit(node.left) * self.visit(node.right)
        elif node.token.type == DIV:
            return self.visit(node.left) / self.visit(node.right)

    def visitNum(self, node):
        return node.value

    def evaluate(self):
        tree = self.parser.parse()
        return self.visit(tree)
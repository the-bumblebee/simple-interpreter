#!/usr/bin/env python3

class AST(object):
    pass

class Operator(AST):

    def __init__(self, left, opToken, right):
        self.left = left;
        self.token = opToken;
        self.right = right;

class Num(AST):

    def __init__(self, token):
        self.token = token
        self.value = token.value

class UnaryOperator(AST):

    def __init__(self, opToken, expr):
        self.token = opToken
        self.expr = expr
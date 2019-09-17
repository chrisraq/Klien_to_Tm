from enum import Enum
from tokenKlien import Token, TokenType

class State(Enum):
    start       = 0
    operator    = 1
    punct       = 2
    zero        = 3
    number      = 4
    identifier  = 5
    comment     = 6

class Scanner:
    "Read tokens from input program"
    keywords = {"integer" : "Keyword", "boolean" : "Keyword", "if" : "Keyword", "then" : "Keyword", "else" : "Keyword", "not" : "Keyword", "and" : "Keyword", "or" : "Keyword", "function" : "Keyword", "main" : "Identifier", "print" : "Identifier", "true" : "Boolean", "false" : "Boolean"}

    def __init__(self, programStr):
        self.programStr = programStr
        self.pos = 0
        self.tokens = self.scan(self.programStr)


    def scan(programStr):
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        accum = ""
        state = State.start
        tokens = []
        strPos = 0
        while strPos < len(programStr):
            if state == State.start:
                if programStr[strPos].isspace():
                    pass
                elif programStr[strPos] in "+-*/<=":
                    tokens.append(Token(TokenType.operator),programStr[strPos])
                elif programStr[strPos] in "),:":
                    tokens.append(Token(TokenType.punct),programStr[strPos])
                elif programStr[strPos] in "0":
                    accum = programStr[strPos]
                    state = State.zero
                elif programStr[strPos] in "123456789":
                    accum = programStr[strPos]
                    state = State.number
                elif programStr[strPos] in alphabet:
                    accum = programStr[strPos]
                    state = State.identifier
                elif programStr[strPos] == "(":
                    if (strPos + 1) < len(programStr) -1 and programStr[strPos+1] == "*":
                        state = State.comment
                    else:
                        tokens.append(Token(TokenType.punct),programStr[strPos])
                else: #Character not exceptable in the language
                    #Error
                    pass
    def next(self):
        nextToken = self.tokens[self.pos]
        self.pos += 1
        return nextToken
    
    def peek(self):
        return self.tokens[self.pos]

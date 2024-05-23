from enum import Enum
from collections import defaultdict
from utils.token import TokenType

class ErrorType(Enum):
    INVALID_INPUT = "Invalid input"
    INVALID_NUM = "Invalid number"
    UNCLOSED_COMMENT = "Unclosed comment"
    UNMATCHED_COMMENT = "Unmatched comment"
    MISSED = "missing"
    ILLEGAL = "illegal"
    UNEXPECTED_EOF = "Unexpected EOF"

class ErrorHandler:
    def __init__(self):
        self.syntaxErrors = defaultdict(list)
        self.lexicalErrors = defaultdict(list)

    def add_lexical_error(self, errorType, strg, lineNum):
        self.lexicalErrors[lineNum].append((strg, errorType.value))
        return 

    def get_lexical_errors(self):
        return self.lexicalErrors
    
    def add_syntax_error(self, errorType, value ):
        if type(value) is tuple : 
           lineno, nt = value
           self.syntaxErrors[lineno].append((nt,errorType.value)) 
        elif (value.get_type() == TokenType.NUM.name or value.get_type() == TokenType.ID.name):
            self.syntaxErrors[value.get_lineno()].append((value.get_type(),errorType.value))
        else:
            self.syntaxErrors[value.get_lineno()].append((value.get_value(),errorType.value))

        return


    def get_syntax_errors(self):
        return self.syntaxErrors
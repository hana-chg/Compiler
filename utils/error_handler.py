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
    
    def add_syntax_error(self, errorType, token ):
        if (token.get_type() == TokenType.NUM.name or token.get_type() == TokenType.ID.name):
            self.syntaxErrors[token.get_lineno()].append((token.get_type(),errorType.value))
        else:
            self.syntaxErrors[token.get_lineno()].append((token.get_value(),errorType.value))

        return


    def get_syntax_errors(self):
        return self.syntaxErrors
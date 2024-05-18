from enum import Enum
from collections import defaultdict

class ErrorType(Enum):
    INVALID_INPUT = "Invalid input"
    INVALID_NUM = "Invalid number"
    UNCLOSED_COMMENT = "Unclosed comment"
    UNMATCHED_COMMENT = "Unmatched comment"

class ErrorHandler:
    def __init__(self):
        self.lexicalErrors = defaultdict(list)

    def add_lexical_error(self, errorType, strg, lineNum):
        self.lexicalErrors[lineNum].append((strg, errorType))
        return 

    def get_lexical_errors(self):
        return self.lexicalErrors
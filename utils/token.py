from enum import Enum
from utils.symbol_table import SymbolTable

class TokenType(Enum):
    KWID = 'KEYWORD_OR_ID'
    NUM  = 'NUM'
    WS   = 'WHITESPACE'
    CM   = 'COMMENT'
    SB   = 'SYMBOL'
    EOF  = '$'
    ID   = 'ID'
    KW   = 'KEYWORD'
    N    = 'NONE'

    def get_token_type(char):
        if char == "":
            return TokenType.EOF
        elif char.isspace():
            return TokenType.WS
        elif char == "/":
            return TokenType.CM
        elif char.isalpha():
            return TokenType.KWID
        elif char.isnumeric():
            return TokenType.NUM
        elif char in SymbolTable.symbols:
            return TokenType.SB
        else:
            return TokenType.N
        
class Token:
    def __init__(self, tokenType, tokenValue):
        self.tokenType = tokenType
        self.tokenValue = tokenValue

    def __str__(self) -> str:
        return  f'({self.tokenType}, {self.tokenValue})'
    
    def get_value(self):
        return self.tokenValue
    
    def get_type(self):
        return self.tokenType
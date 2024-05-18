import os.path
from enum import Enum
from utils.error_handler import ErrorType
from utils.symbol_table import SymbolTable


class Token(Enum):
    KWID = 'KEYWORD_OR_ID'
    NUM = 'NUMBER'
    WS = 'WHITESPACE'
    CM = 'COMMENT'
    SB = 'SYMBOL'
    EOF = '$'
    ID = 'ID'
    KW = 'KEYWORD'
    N = 'NONE'

    def get_token_type(char):
        if char == "":
            return Token.EOF
        elif char.isspace():
            return Token.WS
        elif char == "/":
            return Token.CM
        elif char.isalpha():
            return Token.KWID
        elif char.isnumeric():
            return Token.NUM
        elif char in SymbolTable.symbols:
            return Token.SB
        else:
            return Token.N


class Scanner:

    def __init__(self, inputPath, symbolTable, errorHandler):
        self.errorHandler = errorHandler
        self.symbolTable = symbolTable
        self.char = ""  # current charactor
        self.currentLine = ""
        self.index = 0  # pointing to the next char index
        self.lineno = 0
        self.inputFile = open(os.path.join(os.getcwd(), inputPath), "r")
        self.read_next_line()

    def read_next_line(self):
        self.index = 0
        self.lineno += 1
        self.currentLine = str(self.inputFile.readline())
        self.read_next_char()

    def read_next_char(self):
        try:
            self.char = self.currentLine[self.index]
        except:
            self.char = ""
        self.index = self.index + 1

    def roll_back_char(self):
        self.index = self.index - 1
        self.char = self.currentLine[self.index - 1]

    def get_next_token(self):
        tokenType = Token.get_token_type(self.char)
        tokenValue = ""
        if tokenType == Token.EOF:
            return self.lineno, Token.EOF, '$'
        elif tokenType == Token.WS:
            if self.char == '\n':
                self.read_next_line()
            else:
                self.read_next_char()
            return self.get_next_token()
        elif tokenType == Token.CM:
            self.scan_comment()
            self.read_next_char()
            return self.get_next_token()
        elif tokenType == Token.KWID:
            tokenType, tokenValue = self.get_idOrKw()
            if tokenType != "":
                return self.lineno, tokenType.value, tokenValue
            else:
                self.read_next_char()
                return self.get_next_token()
        elif tokenType == Token.NUM:
            tokenValue = self.get_number()
            if tokenType != "":
                return self.lineno, tokenType.value, tokenValue
            else:
                self.read_next_char()
                return self.get_next_token()
        elif tokenType == Token.SB:
            if self.char == "*":
                self.read_next_char()
                if self.char == "/":
                    self.errorHandler.add_lexical_error(ErrorType.UNMATCHED_COMMENT, "*/", self.lineno)
                    self.read_next_char()
                    return self.get_next_token()
                self.roll_back_char()
            tokenValue = self.get_symbols()
            if tokenType != "": return self.lineno, tokenType.value, tokenValue
        else:
            self.errorHandler.add_lexical_error(ErrorType.INVALID_INPUT, self.char, self.lineno)
            self.read_next_char()
        return

    def scan_comment(self):
        commentSum = self.char
        self.read_next_char()
        if self.char == "*":  # entered a comment
            commentSum += self.char
            while True:
                self.read_next_char()
                if self.char == "*":
                    self.read_next_char()
                    if self.char == "/":
                        return
                if self.char == "\n":
                    self.read_next_line()
                else:
                    commentSum += self.char
                if self.char == "":
                    self.errorHandler.add_lexical_error(ErrorType.UNCLOSED_COMMENT, commentSum[0:7] + "...",
                                                        self.lineno)
                    return
        else:
            self.errorHandler.add_lexical_error(ErrorType.INVALID_INPUT, self.char, self.lineno)
            return

    def get_number(self):
        number = self.char
        while True:
            self.read_next_char()
            if self.char.isnumeric():
                number += self.char
            elif self.char.isspace() or self.char in SymbolTable.symbols or self.char == "":
                return number
            else:
                number += self.char
                self.errorHandler.add_lexical_error(ErrorType.INVALID_NUM, number, self.lineno)
                return ""

    def get_idOrKw(self):
        idOrKwString = self.char
        while True:
            self.read_next_char()
            if self.char.isalnum():
                idOrKwString += self.char
            elif self.char.isspace() or self.char in SymbolTable.symbols or self.char == "/":
                if idOrKwString in SymbolTable.keyWords:
                    return Token.KW, idOrKwString
                else:
                    if not self.symbolTable.deos_id_exist_in_symbol_table(idOrKwString):
                        self.symbolTable.insert_id(idOrKwString)
                    return Token.ID, idOrKwString
            else:
                idOrKwString += self.char
                self.errorHandler.add_lexical_error(ErrorType.INVALID_INPUT, idOrKwString, self.lineno)
                return ""

    def get_symbols(self):
        symbolString = self.char
        if self.char == "=":
            self.read_next_char()
            symbolString += self.char
            if self.char == "=":
                self.read_next_char()
                symbolString += self.char
                if self.char.isspace() or self.char.isalnum() or self.char == "" or self.char in SymbolTable.symbols or self.char == "/":
                    return "=="
                else:
                    self.read_next_char()
                    self.errorHandler.add_lexical_error(ErrorType.INVALID_INPUT, symbolString, self.lineno)
                    return ""
            else:
                if self.char.isspace() or self.char.isalnum() or self.char == "" or self.char in SymbolTable.symbols or self.char == "/":
                    return "="
                else:
                    self.read_next_char()
                    self.errorHandler.add_lexical_error(ErrorType.INVALID_INPUT, symbolString, self.lineno)
                    return ""
        else:
            self.read_next_char()
            if self.char.isspace() or self.char.isalnum() or self.char == "" or self.char in SymbolTable.symbols or self.char == "/":
                return symbolString
            else:
                symbolString += self.char
                self.read_next_char()
                self.errorHandler.add_lexical_error(ErrorType.INVALID_INPUT, symbolString, self.lineno)
                return ""

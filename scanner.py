import os.path
from utils.error_handler import ErrorType
from utils.symbol_table import SymbolTable
from utils.token import Token, TokenType


class Scanner:

    def __init__(self, inputPath, symbolTable, errorHandler):
        self.errorHandler = errorHandler
        self.symbolTable = symbolTable
        self.char = ""  # current charactor
        self.currentLine = ""
        self.index = 0  # pointing to the next char index
        self.lineno = 0
        self.inputFile = open(os.path.join(os.getcwd(), inputPath), "r")
        self.__read_next_line()


    def __read_next_line(self):
        self.index = 0
        self.lineno += 1
        self.currentLine = str(self.inputFile.readline())
        self.__read_next_char()


    def __read_next_char(self):
        try:
            self.char = self.currentLine[self.index]
        except:
            self.char = ""
        self.index = self.index + 1


    def __roll_back_char(self):
        self.index = self.index - 1
        self.char = self.currentLine[self.index - 1]


    def get_next_token(self):
        tokenType = TokenType.get_token_type(self.char)
        tokenValue = ""
        if tokenType == TokenType.EOF:
            return Token(TokenType.EOF, '$', self.lineno)
        elif tokenType == TokenType.WS:
            if self.char == '\n':
                self.__read_next_line()
            else:
                self.__read_next_char()
            return self.get_next_token()
        elif tokenType == TokenType.CM:
            self.__scan_comment()
            self.__read_next_char()
            return self.get_next_token()
        elif tokenType == TokenType.KWID:
            tokenValue = self.__get_kwid()
            if tokenValue != "":
                tokenType = self.__get_id_or_kw_type(tokenValue)
                return Token(tokenType.value, tokenValue, self.lineno)
            else:
                self.__read_next_char()
                return self.get_next_token()
        elif tokenType == TokenType.KW:
            tokenValue = self.get_kw()
            if tokenValue != "":
                return Token(tokenType.value, tokenValue, self.lineno)
            else:
                self.__read_next_char()
                return self.get_next_token()
        elif tokenType == TokenType.NUM:
            tokenValue = self.__get_number()
            if tokenValue != "":
                return Token(tokenType.value, tokenValue, self.lineno)
            else:
                self.__read_next_char()
                return self.get_next_token()
        elif tokenType == TokenType.SB:
            if self.char == "*":
                self.__read_next_char()
                if self.char == "/":
                    self.errorHandler.add_lexical_error(ErrorType.UNMATCHED_COMMENT, "*/", self.lineno)
                    self.__read_next_char()
                    return self.get_next_token()
                self.__roll_back_char()
            tokenValue = self.__get_symbols()
            if tokenValue != "": 
                return Token(tokenType.value, tokenValue, self.lineno)
        else:
            self.errorHandler.add_lexical_error(ErrorType.INVALID_INPUT, self.char, self.lineno)
            self.__read_next_char()
        return self.get_next_token()


    def __scan_comment(self):
        commentSum = self.char
        self.__read_next_char()
        if self.char == "*":  # entered a comment
            commentSum += self.char
            while True:
                self.__read_next_char()
                if self.char == "*":
                    self.__read_next_char()
                    if self.char == "/":
                        return
                elif self.char == "\n":
                    self.__read_next_line()
                elif self.char == "":
                    self.errorHandler.add_lexical_error(ErrorType.UNCLOSED_COMMENT, commentSum[0:7] + "...",self.lineno)
                    return
                else:
                    commentSum += self.char
        else:
            self.__roll_back_char()
            self.errorHandler.add_lexical_error(ErrorType.INVALID_INPUT, self.char, self.lineno)
            return


    def __get_number(self):
        number = self.char
        while True:
            self.__read_next_char()
            if self.char.isnumeric():
                number += self.char
            elif self.char.isspace() or self.char in SymbolTable.symbols or self.char == "":
                return number
            else:
                number += self.char
                self.errorHandler.add_lexical_error(ErrorType.INVALID_NUM, number, self.lineno)
                return ""


    def __get_kwid(self):
        kwid = self.char
        while True:
            self.__read_next_char()
            if self.char.isalnum():
                kwid += self.char
            elif self.char.isspace() or self.char in SymbolTable.symbols or self.char == "/":
               return kwid
            else:
                kwid += self.char
                self.errorHandler.add_lexical_error(ErrorType.INVALID_INPUT, kwid, self.lineno)
                return ""
            
            
    def __get_id_or_kw_type(self, tokenValue):
         if SymbolTable.is_keyword(tokenValue):
             return TokenType.KW
         else:
            if not self.symbolTable.deos_id_exist_in_symbol_table(tokenValue):
                    self.symbolTable.insert_id(tokenValue)
            return TokenType.ID
       
    
            

    def __get_symbols(self):
        symbol = self.char
        if self.char == "=":
            self.__read_next_char()
            if self.char == "=":
                self.__read_next_char()
                return "=="
            else:
                return "="
        else:
            self.__read_next_char()
            return symbol
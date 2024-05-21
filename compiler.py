#سارا چگینی - 99170372
from collections import defaultdict
from scanner import Scanner
from parser_prd import Parser
from utils.error_handler import ErrorHandler
from utils.symbol_table import SymbolTable
from utils.file_handler import *

def main():
    allTokens = defaultdict(list)
    inputPath = "input.txt"
    symbolTable = SymbolTable()
    errorHandler = ErrorHandler()
    scanner = Scanner(inputPath = inputPath, symbolTable = symbolTable, errorHandler = errorHandler)

    while True :
        token = scanner.get_next_token()
        lineno = scanner.get_current_line()
        if (token.get_value() == "$") : 
            token_file_writer(allTokens)
            symbol_table_file_writer(symbolTable)
            lexical_error_file_writer(errorHandler)
            return
        else:
            allTokens[lineno].append(token)
            
        #parser = Parser(scanner = scanner, symbolTable = symbolTable, errorHandler = errorHandler)
        #parser.run()
    

if __name__ == "__main__":
    main()
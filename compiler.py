#سارا چگینی - 99170372
from scanner import Scanner
from parser_prd import Parser
from utils.error_handler import ErrorHandler
from utils.symbol_table import SymbolTable
from utils.file_handler import *

def main():
    inputPath = "input.txt"
    symbolTable = SymbolTable()
    errorHandler = ErrorHandler()

    scanner = Scanner(inputPath = inputPath, symbolTable = symbolTable, errorHandler = errorHandler)
    parser = Parser(scanner = scanner, symbolTable = symbolTable, errorHandler = errorHandler)
    parser.run()
    syntax_error_file_writer(errorHandler)
    parse_tree_file_writer(parser.get_start_node())
    
    

if __name__ == "__main__":
    main()
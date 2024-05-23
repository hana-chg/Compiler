class SymbolTable :
    keyWords = ["break", "else", "if", "int", "while", "for", "void", "endif"]
    symbols = ["+", "-", "*", "<", "=", "==", ":", ";", ",", "[", "]", "(", ")", "{", "}"]


    def __init__(self) :
        self.symbolTable = []
        for i in SymbolTable.keyWords:
            self.insert_id(i)        

    def insert_id(self, lexeme):
        self.symbolTable.append(lexeme)

    def is_keyword(lexeme):
        return lexeme in SymbolTable.keyWords
    
    def deos_id_exist_in_symbol_table(self, lexeme):
        return lexeme in self.symbolTable
    
    def get_symbol_table(self):
        return self.symbolTable
    
    def get_item(self, index):
        return self.symbolTable[index]
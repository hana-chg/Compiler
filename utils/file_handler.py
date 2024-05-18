 
def token_file_writer(allTokens):
        tokenFile = open("tokens.txt", "w")
        for line in allTokens.keys():
                tokenFile.write(str(line) + ".\t")
                for token in allTokens[line]:
                        tokenType, tokenValue = token
                        tokenFile.write(f"({tokenType}, {tokenValue})")
                tokenFile.write("\n")
        tokenFile.close()

def symbol_table_file_writer(symbolTable):
        symbolTableFile = open("symbol_table.txt", "w")
        for i in range(len(symbolTable.get_symbol_table())):
                symbolTableFile.write(str(i + 1) + ".\t" + str(symbolTable.get_item(i)) + "\n")
        symbolTableFile.close()


def lexical_error_file_writer(error_handler):
        lexicalErrorFile = open("lexical_errors.txt", "w")
        if (not bool(error_handler.get_lexical_errors)):
                for line in error_handler.get_lexical_errors.keys():
                        lexicalErrorFile.write(str(line) + ".\t")
                        for error in error_handler.get_lexical_errors[line]:
                                lexicalErrorFile.write(str(error) + " " )
                        lexicalErrorFile.write("\n")
        else : lexicalErrorFile.write("There is no lexical error.")
        lexicalErrorFile.close()



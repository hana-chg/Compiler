 
def token_file_writer(allTokens):
        tokenFile = open("tokens.txt", "w")
        for line in allTokens.keys():
                tokenFile.write(str(line) + ".\t")
                for token in allTokens[line]:
                        tokenType, tokenValue = token
                        tokenFile.write(f"({tokenType}, {tokenValue}) ")
                tokenFile.write("\n")
        tokenFile.close()

def symbol_table_file_writer(symbolTable):
        symbolTableFile = open("symbol_table.txt", "w")
        for i in range(len(symbolTable.get_symbol_table())):
                symbolTableFile.write(str(i + 1) + ".\t" + str(symbolTable.get_item(i)) + "\n")
        symbolTableFile.close()


def lexical_error_file_writer(error_handler):
        lexicalErrorFile = open("lexical_errors.txt", "w")
        lexicalErrors = error_handler.get_lexical_errors()
        if (bool(lexicalErrors)):
                for line in lexicalErrors.keys():
                        lexicalErrorFile.write(str(line) + ".\t")
                        for error in lexicalErrors[line]:
                                errorStr, errorType = error
                                lexicalErrorFile.write(f"({errorStr}, {errorType}) ")
                        lexicalErrorFile.write("\n")
        else : lexicalErrorFile.write("There is no lexical error.")
        lexicalErrorFile.close()


from anytree import RenderTree


def token_file_writer(allTokens):
        tokenFile = open("tokens.txt", "w")
        for line in allTokens.keys():
                tokenFile.write(str(line) + ".\t")
                for token in allTokens[line]:
                        tokenFile.write(str(token) + " ")
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


def syntax_error_file_writer(error_handler):
        syntaxErrorFile = open("syntax_errors.txt", "w")
        syntaxErrors = error_handler.get_syntax_errors()
        if (bool(syntaxErrors)):
                for line in syntaxErrors.keys():
                        for error in syntaxErrors[line]:
                                syntaxErrorFile.write("#" + str(line) + " : syntax error, ")
                                errorStr, errorType = error
                                syntaxErrorFile.write(f"{errorType} {errorStr}\n")
        else : syntaxErrorFile.write("There is no syntax error.\n")
        syntaxErrorFile.close()


def parse_tree_file_writer(node):
        with open ('parse_tree.txt', 'w', encoding="utf-8") as f:
                for pre, fill, node in RenderTree(node):
                        f.write("%s%s" % (pre, node.name))
                        f.write("\n")
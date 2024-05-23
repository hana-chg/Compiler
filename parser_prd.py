from utils.token import TokenType, Token
from utils.error_handler import *
from anytree import Node
from utils.rule_handler import RuleHandler
from utils.grammer import GrammerData

class Parser:
    
    def __init__(self, scanner, symbolTable, errorHandler):
        self.scanner = scanner
        self.symbolTable = symbolTable
        self.errorHandler = errorHandler
        self.ruleHandler = RuleHandler()
        self.eofReached = False

    def run(self):
        self.lookahead = self.scanner.get_next_token()
        self.start = Node("Program")
        self.find_rule(self.start)

    def get_start_node(self):
        return self.start
    
    def find_rule (self, node : Node):
        rules_with_lhs = self.ruleHandler.get_rules_with_lhs(node.name)
        for rule in rules_with_lhs:
            if self.lookahead.get_type() in rule.get_predic() or self.lookahead.get_value() in rule.get_predic():
                self.produce(node, rule)
                return

        if self.lookahead.get_type() in GrammerData.follow[node.name] or self.lookahead.get_value() in GrammerData.follow[node.name]:
                if  "epsilon" not in GrammerData.first[node.name]:
                    self.errorHandler.add_syntax_error(ErrorType.MISSED, (self.lookahead.get_lineno(), node.name))
                node.parent = None
                return
        else:
            if self.lookahead.get_type() == TokenType.EOF:
                    self.errorHandler.add_syntax_error(ErrorType.UNEXPECTED_EOF, self.lookahead)
                    node.parent = None
                    self.eofReached = True
                    return
            else:
                self.errorHandler.add_syntax_error(ErrorType.ILLEGAL, self.lookahead)
                self.lookahead = self.scanner.get_next_token()
                self.find_rule(node)
        

    def match(self, expected_token, parent):
        if expected_token == "$":
            Node('$', parent=parent)
        elif self.lookahead.get_value() == expected_token or\
            self.lookahead.get_type() == expected_token:
            Node(str(self.lookahead), parent=parent)
            self.lookahead = self.scanner.get_next_token()
        elif expected_token == "epsilon":
            Node('epsilon', parent=parent)
        else:
            self.errorHandler.add_syntax_error(ErrorType.MISSED, (self.lookahead.get_lineno(), expected_token))
        

    def produce(self, parent , rule):
        for p in rule.get_rhs():
            if self.eofReached : return
            if self.lookahead.get_type() == TokenType.EOF.name:
                return
            if RuleHandler.is_non_terminal(p):
                node = Node(p,parent)
                self.find_rule(node)
            else:
                self.match(p, parent)

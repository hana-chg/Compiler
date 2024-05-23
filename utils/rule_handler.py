from utils.grammer import GrammerData

class RuleHandler:
    def __init__(self):
        self.allRules = []
        for p in GrammerData.products:
            self.allRules.append(Rule(p[0], p[1], p[2], p[3]))

    def get_rules_with_lhs(self, lhs):
        answer = []
        for p in self.allRules:
            if p.get_lhs() == lhs:
                answer.append(p)
        return answer
    
    def is_non_terminal(NT):
        for p in GrammerData.products:
            if NT == p [2]:
                return True
        return False
             

class Rule:
    def __init__(self, ruleNumber, predict, lhs, rhs) :
        self.ruleNumber = ruleNumber
        self.predict = predict
        self.lhs = lhs
        self.rhs = rhs

    def get_lhs(self):
        return self.lhs
    
    def get_rhs(self):
        return self.rhs
    
    def get_rule_number(self):
        return self.ruleNumber
    
    def get_predic(self):
        return self.predict
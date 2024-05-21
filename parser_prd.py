class Parser:
    
    def __init__(self, scanner, input_file):
        self.scanner = scanner
        self.input_file = input_file
        self.lookahead = scanner.get_next_token()

    def match(self, expected_token):
        if self.lookahead == expected_token :
            self.lookahead == self.scanner.get_next_token()
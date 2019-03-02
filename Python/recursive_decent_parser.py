class Recursive_Decent_Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.look_ahead = self.lexer.next()
    
    def parse(self):
        self.parse_list()

    def parse_list(self):
        self.parse_expression()
        if not self.match(';'):
            self.error(';')
        if not self.match('EOF'):
            self.parse_list()

    def parse_expression(self):
        self.parse_term()
        self.parse_terms()

    def parse_term(self):
        self.parse_factor()
        self.parse_factors()

    def parse_terms(self):
        if self.match('+') or self.match('-'):
            self.parse_term()
            self.parse_terms()

    def parse_factor(self):
        if self.match('('):
            self.parse_expression()
            if not self.match(')'):
                self.error(')')
        elif self.match('STRING'):
            pass
        elif self.match('NUMBER'):
            pass 
        else:
            self.error('Factor')


    def parse_factors(self):
        if self.match('*') or self.match('/') or self.match('MOD'):
            self.parse_factor()
            self.parse_factors()

    def match(self, token):
        if self.look_ahead == token:
            self.look_ahead = self.lexer.next()
            return True
        return False

    def error(self, token):
        self.print_error(token)
        while self.look_ahead != ';' and self.look_ahead != 'EOF':
            self.look_ahead = self.lexer.next()

    def print_error(self, expected):
        print('Error (' + str(self.lexer.getLineNumber()) + ' , ' + str(self.lexer.getCharacterNumber()) + '): Expected ' 
        + expected + ' got ' + self.lexer.getValue())

    def getAbstractDataTree(self):
        pass

    def getSymbolTable(self):
        pass
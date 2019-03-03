from abstract_syntax_tree import Abstract_Syntax_Tree

class Recursive_Decent_Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.look_ahead = self.lexer.next()
        self.symbol_table = {}
        self.translation = ''
        self.errors = ''
        self.abstract_syntax_tree = Abstract_Syntax_Tree('expressions')
    
    def parse(self):
        self.parse_list()

    def parse_list(self):
        root = self.abstract_syntax_tree.get_root()
        self.abstract_syntax_tree.add_child(self.parse_expression(), root)
        if self.match(';'):
            self.translation += ';\n'
        else:
            self.error(';')
        if not self.match('EOF'):
            self.parse_list()
        else:
            self.translation += 'eof\n'

    def parse_expression(self):
        child = self.parse_term()
        parent = self.parse_terms()
        if parent:
            self.abstract_syntax_tree.add_child(child, parent)
        else:
            parent = child
        return parent

    def parse_term(self):
        child = self.parse_factor()
        parent = self.parse_factors()
        if parent:
            self.abstract_syntax_tree.add_child(child, parent)
        else:
            parent = child
        return parent

    def parse_terms(self):
        symbol = self.look_ahead
        if self.match('+') or self.match('-'):
            node = self.abstract_syntax_tree.add_node('SYMBOL' + str(self.lexer.get_character_number()) 
            + str(self.lexer.get_line_number()), symbol)
            child = self.parse_term()
            self.translation += symbol + ' '
            parent = self.parse_terms()
            if parent:
                self.abstract_syntax_tree.add_child(child, parent)
            else:
                parent = child
            self.abstract_syntax_tree.add_child(parent, node)
            return node

    def parse_factor(self):
        if self.match('('):
            node = self.parse_expression()
            if not self.match(')'):
                self.error(')')
                return None
        elif self.look_ahead == 'STRING':
            value = self.lexer.get_value()
            if value not in self.symbol_table.keys():
                self.symbol_table[value] =  self.lexer.get_line_number()
            self.translation += value + ' '
            node = self.abstract_syntax_tree.add_node('STRING' + str(self.lexer.get_character_number()) 
            + str(self.lexer.get_line_number()), value)
            self.match('STRING')
        elif self.look_ahead == 'NUMBER':
            self.translation += self.lexer.get_value() + ' '
            node = self.abstract_syntax_tree.add_node('NUMBER' + str(self.lexer.get_character_number()) 
            + str(self.lexer.get_line_number()), self.lexer.get_value())
            self.match('NUMBER')
        else:
            self.error('Factor')
            return None
        return node


    def parse_factors(self):
        symbol = self.look_ahead
        if self.match('*') or self.match('/') or self.match('MOD'):
            node = self.abstract_syntax_tree.add_node('SYMBOL' + str(self.lexer.get_character_number()) 
            + str(self.lexer.get_line_number()), symbol)
            child = self.parse_factor()
            self.translation += symbol + ' '
            parent = self.parse_factors()
            if parent:
                self.abstract_syntax_tree.add_child(child, parent)
            else:
                parent = child
            self.abstract_syntax_tree.add_child(parent, node)
            return node

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
        self.errors += ('Error (' + str(self.lexer.get_line_number()) + ' , ' + str(self.lexer.get_character_number()) 
        + '): Expected ' + expected + ' got ' + self.lexer.get_value() + '\n')

    def get_abstract_syntax_tree(self):
        return self.abstract_syntax_tree

    def get_symbol_table(self):
        return self.symbol_table

    def get_translation(self):
        return self.translation

    def get_errors(self):
        return self.errors

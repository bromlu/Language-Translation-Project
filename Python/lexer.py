class Lexer: 
    def __init__(self, inputFile):
        self.file = open(inputFile, 'r')
        self.value = ''
        self.lineNumber = 1
        self.characterNumber = 0

    def next(self):
        self.value = ''
        token = self.file.read(1)
        self.characterNumber += 1
        
        if token != '':
            while token == ' ' or token == '\t' or token == '\n' or token == '\r':
                if token == '\n' or token == '\r':
                    self.characterNumber = 0
                    self.lineNumber += 1
                token = self.file.read(1)
                self.characterNumber += 1
            if token.isalpha():
                self.value = token
                token = self.file.read(1)
                self.characterNumber += 1
                while token.isalpha() or token.isdigit():
                    self.value += token
                    token = self.file.read(1)
                    self.characterNumber += 1
                self.characterNumber -= 1
                self.file.seek(self.file.tell() - 1)
                if self.value == 'MOD' or self.value == 'EOF':
                    return self.value
                return 'STRING'
            elif token.isdigit():
                self.value = token
                token = self.file.read(1)
                self.characterNumber += 1
                while token.isdigit():
                    self.value += token
                    token = self.file.read(1)
                    self.characterNumber += 1
                self.characterNumber -= 1
                self.file.seek(self.file.tell() - 1)
                return 'NUMBER'
            elif (token == ';' or token == '(' or token == ')' or token == '+'
                or token == '-' or token == '*' or token == '/'):
                self.value = token
                return token
            else:
                return 'ERROR'
        else:
            return 'EOF'

    def getValue(self):
        return self.value

    def getLineNumber(self):
        return self.lineNumber

    def getCharacterNumber(self):
        return self.characterNumber
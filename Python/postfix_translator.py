import sys
from lexer import Lexer
from recursive_decent_parser import Recursive_Decent_Parser
from pathlib import Path

def print_usage():
    print('''Usage:
            First argument is the input file to be translated.
            Second argument is the output file the translation os stored in.''')

def main():
    if '-h' in sys.argv:
       print_usage()
       exit(1)
    elif len(sys.argv) != 3:
        print('Wrong number of arguments.')
        print_usage()
        exit(1)

    inputFile = sys.argv[1]
    outputFile = sys.argv[2]

    if not Path(inputFile).is_file():
        print('Unable to open input file')
        print_usage()
        exit(1)

    lexer = Lexer(inputFile)
    recursive_decent_parser = Recursive_Decent_Parser(lexer)

    recursive_decent_parser.parse()

    errors = recursive_decent_parser.get_errors()
    translation = recursive_decent_parser.get_translation()
    symbol_table = recursive_decent_parser.get_symbol_table()

    if len(errors) > 0:
        print(errors, end='')
    else:
        file = open(outputFile, 'w')
        file.write(translation)
        file.write('Symbol Table\n')
        for key in symbol_table:
            file.write(key + ' : first appeared on line ' + str(symbol_table[key]) + '\n')

    file.close()

main()
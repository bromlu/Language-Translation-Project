import sys
from lexer import Lexer
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

    token = lexer.next()
    while(token != 'ERROR' and token != 'EOF'):
        print(token, lexer.getValue())
        token = lexer.next()
    print(token)

main()
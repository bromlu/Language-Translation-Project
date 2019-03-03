# Language-Translation-Project
Translate math equations from infix to postfix by various different methods

## Example Input

```math
2 + 43 * AB;  4 + f;
8 * 5 + ty6 / (7 MOD
3); EOF
```

## Example Output

```math
2 43 AB * + ;
4 f + ;
8 5 * ty6 7 3 MOD / + ;
eof
Symbol Table
AB : first appeared on line 1
f : first appeared on line 1
ty6 : first appeared on line 2
```

The program will also output a abstract data tree into a pdf file.

## Method 1: Python Lexer and Recursive Decent Parser

### Run

```bash
python3 postfix_translator.py input.txt output.txt
```

### Dependency

You need to download graphviz for this program to run. Installation is quite simple with pip!

```bash
pip install graphviz
```
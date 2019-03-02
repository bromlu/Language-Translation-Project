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

## Method 1: Python Lexer and Recursive Decent Parser

### Run

```bash
python3 postfix_translator.py input.txt output.txt
```
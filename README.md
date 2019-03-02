# Language-Translation-Project
Translate math equations from infix to postfix by various different methods

## Example Input

```math
2 + 43 * AB;  4 + f;
8 * 5 + ty6 / (7 MOD3); EOF
```

## Example Output

```math
2 43 AB * + ;
4 f + ;
8 5 * ty6 7 3 MOD / + ;
eof
Symbol Table: ty6, AB, f
```

## Method 1: Python Lexer and Recursive Decent Parser

### Run

```bash
python3 postfix_translator.py input.txt output.txt
```
# Language-Translation-Project
Translate math equations from infix to postfix by various different methods

## Example Input

```math
2 + 43 * AB;  4 + f;
8 * 5 + ty6 / (7 MOD
3); EOF
```

## Method 1: Python Lexer and Recursive Decent Parser

### Example Output

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

The program will also output a abstract data tree into a pdf file and open it for the user to see.

### Run

```bash
python3 postfix_translator.py input.txt output.txt
```

### Dependency

You need to download graphviz for this program to run. Installation is quite simple with pip!

```bash
pip install graphviz
```

## Method 2: Antlr grammar with embeded actions

### Run

I used IntelliJ with the Antlr plugin to run this. After installing the plugin [https://plugins.jetbrains.com/plugin/7358-antlr-v4-grammar-plugin](Antlr IntelliJ plugin) simply right click on the grammar and hit "generate Antlr Recognizer." Then mark the "out" folder as source, then go ahead and run the InfixTranslator file. The translated input file will appear in the console.

Currently the input file location is hard coded in the Java file as "../input.txt". Make sure to change that to an existing input file on your system.

### Dependency

You will need to download the Antlr runtime in order to run this project. Here is a link to their website [https://www.antlr.org/](Antlr).

### Example Output

```math
2 43 AB * + ;
4 f + ;
8 5 * ty6 7 3 MOD / + f + ;
eof
Symbol Table (symbol=line)
{ty6=2, AB=1, f=1}
Process finished with exit code 0
```
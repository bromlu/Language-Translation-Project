grammar Infix;

@header {
    import java.util.HashMap;
}

@members {
    HashMap symbolTable = new HashMap();
}

prog: list 'EOF' { System.out.print("eof\n"); System.out.print("Symbol Table (symbol=line)\n"); System.out.print(symbolTable); };

list : expression ';' { System.out.print(";\n"); } list* ;

expression : term terms? ;

terms : '+' term { System.out.print("+ "); } terms?
      | '-' term { System.out.print("- "); } terms? ;

term : factor factors? ;

factors : '*' factor { System.out.print("* "); } factors?
        | '/' factor { System.out.print("/ "); } factors?
        | 'MOD' factor { System.out.print("MOD "); } factors? ;

factor : '(' expression ')'
       | WORD { System.out.print($WORD.text + " ");
       if(symbolTable.get($WORD.text) == null) symbolTable.put($WORD.text, $WORD.getLine()); }
       | DIGIT { System.out.print($DIGIT.text + " "); } ;

DIGIT   : [0-9]+ '.'? [0-9]*
        | [0-9]* '.'? [0-9]+;
WORD  : [a-zA-Z][a-zA-Z0-9]* ;
NEWLINE : '\r'? '\n' -> skip;
WS      : [ \t]+ -> skip ;
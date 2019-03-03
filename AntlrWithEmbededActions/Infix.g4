grammar Infix;

prog: list 'EOF';

list : expression ';' list* ;

expression : term terms? ;

terms : '+' term terms?
      | '-' term terms? ;

term : factor factors? ;

factors : '*' factor factors?
        | '/' factor factors?
        | 'MOD' factor factors? ;

factor : '(' expression ')'
       | WORD
       | DIGIT ;

DIGIT   : [0-9]* '.'? [0-9]* ;
WORD  : [a-zA-Z][a-zA-Z0-9]* ;
NEWLINE : '\r'? '\n' -> skip;
WS      : [ \t]+ -> skip ;
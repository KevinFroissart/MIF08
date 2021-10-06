grammar Exo3;

r: expr EOF ;

expr: '(' expr ')' expr
    | '[' expr ']' expr
    | CHARS
    |
    ;

CHARS: ~[()[\]] -> skip ;
WS : [ \t\r\n]+ -> skip ;          // skip spaces, tabs, newlines

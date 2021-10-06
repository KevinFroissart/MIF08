grammar Exo5;

r: expr EOF ;

expr: 'a' expr 'bb'
    |
    ;

AB: ~[ab] -> skip ;
WS : [ \t\r\n]+ -> skip ;          // skip spaces, tabs, newlines

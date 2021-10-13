//define a lexical analyser called Example1

lexer grammar Example1;

<<<<<<< HEAD
OP : '+'| '*' | '-' | '/' | '(' | ')';
=======
OP : '+'| '*' | '-' | '/' ;
>>>>>>> 55664ee82249a0e32f6b0e6de45e1963b36eff11
DIGIT : [0-9] ;
LETTER : [A-Za-z] ;
ID : LETTER (LETTER | DIGIT)* ;             // match idents
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

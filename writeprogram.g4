grammar writeprogram;

command: language ':'statement+;
language: JAVA | PYTHON | CPP | JS;
statement: arithmentic | (communication | WHITESPACE);
arithmentic: (DIGITS operations DIGITS);
communication: (TEXT);
operations: '+' | '-' | '/' | '*' | '%' | 'power';


/* Lexer Rules */
/* C++, JAVA, Python3, JavaScript */
fragment A: 'A' | 'a';
fragment C: 'C' | 'c';
fragment M: 'M' | 'm';
fragment U: 'U' | 'u';
fragment E: 'E' | 'e';
fragment O: 'O' | 'o';
fragment H: 'H' | 'h';
fragment S: 'S' | 's';
fragment V: 'V' | 'v';
fragment R: 'R' | 'r';
fragment P: 'P' | 'p';
fragment T: 'T' | 't';
fragment I: 'I' | 'i';
fragment J: 'J' | 'j';
fragment Y: 'Y' | 'y';
fragment N: 'N' | 'n';

JAVA: J A V A;
PYTHON: P Y T H O N '3';
CPP: C '+' '+';
JS: (J A V A S C R I P T) | (J S);
ARITHMETIC: (A R I T H M E T I C) | (M A T H);
COMMUNICATE: (C O M M U N I C A T E) | (C O M);
DIGITS: [0-9]+;

TEXT: ( [a-z] | [A-Z] | ' ')+;
WHITESPACE: ' ';
NEWLINE: '\n' -> skip;
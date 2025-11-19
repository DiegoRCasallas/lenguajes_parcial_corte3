grammar GramaticaMatrices;

// Reglas del parser
programa: expresionMatriz EOF;

expresionMatriz: 
    declaracionMatriz
    | operacionMatriz
    | asignacion
    ;

declaracionMatriz:
    ID '=' matrizLiteral
    ;

asignacion:
    ID '=' expresionMatriz
    ;

// Precedencia de operadores (de menor a mayor)
operacionMatriz: multiplicacion;

multiplicacion:
    suma ('*' suma)*           # ProductoPunto
    ;

suma:
    resta (('+' | '-') resta)* # SumaRestaMatriz
    ;

resta:
    primaria
    ;

primaria:
    '(' operacionMatriz ')'    # Parentesis
    | ID                       # VariableMatriz
    | matrizLiteral           # LiteralMatriz
    ;

matrizLiteral:
    '[' fila (',' fila)* ']'
    ;

fila:
    '[' NUMERO (',' NUMERO)* ']'
    ;

// Reglas del lexer
ID: [a-zA-Z_][a-zA-Z_0-9]*;
NUMERO: [0-9]+ ('.' [0-9]+)?;
WS: [ \t\r\n]+ -> skip;
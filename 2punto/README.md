programa → expresionMatriz

expresionMatriz →
        declaracionMatriz
      | operacionMatriz
      | asignacion

declaracionMatriz →
        ID = matrizLiteral

asignacion →
        ID = expresionMatriz

operacionMatriz →
        multiplicacion

multiplicacion →
        suma
      | multiplicacion * suma

suma →
        resta
      | suma + resta
      | suma - resta

resta →
        primaria

primaria →
        ( operacionMatriz )
      | ID
      | matrizLiteral

matrizLiteral →
        [ filaLista ]

filaLista →
        fila
      | filaLista , fila

fila →
        [ numeroLista ]

numeroLista →
        NUMERO
      | numeroLista , NUMERO

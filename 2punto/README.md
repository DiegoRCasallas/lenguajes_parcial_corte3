# Gramática del Lenguaje de Matrices

Este documento explica la gramática del mini-lenguaje para manejar
matrices, junto con su representación en un formato claro y humano
usando flechas.

------------------------------------------------------------------------

## 📘 1. Descripción General

La gramática define un lenguaje capaz de:

-   Declarar matrices\
-   Asignarlas a variables\
-   Realizar operaciones entre matrices: suma, resta y multiplicación\
-   Utilizar paréntesis para agrupar expresiones

------------------------------------------------------------------------

## 📐 2. Gramática en Formato Humano (con flechas)

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

------------------------------------------------------------------------

## 🔤 3. Tokens

    ID      → Secuencia de letras, números o guión bajo, sin iniciar con número.
    NUMERO  → Enteros o decimales.

------------------------------------------------------------------------

## 📝 4. Ejemplos del Lenguaje

### Declaración de matriz

    A = [[1,2],[3,4]]

### Asignación con operación

    C = A * B + D

### Uso de paréntesis

    (A + B) * C

------------------------------------------------------------------------

## 📎 5. Notas

-   La multiplicación tiene mayor precedencia que la suma y la resta.\
-   Las matrices se representan como listas de filas.\
-   Las operaciones solo son válidas entre matrices compatibles.
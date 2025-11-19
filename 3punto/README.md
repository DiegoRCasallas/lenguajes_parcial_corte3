 # 🧮 Calculadora de Matrices - Producto Punto

Una calculadora especializada en operaciones con matrices implementada en Python usando ANTLR4. Soporta producto punto, suma, resta y asignaciones con verificación automática de dimensiones.

## ✨ Características

- **Operaciones soportadas**: Producto punto, suma y resta de matrices
- **Verificación de dimensiones**: Validación automática de compatibilidad
- **Sintaxis intuitiva**: Usa operadores matemáticos estándar (`*`, `+`, `-`)
- **Variables**: Asignación y reutilización de matrices
- **Expresiones complejas**: Soporte para paréntesis y operaciones anidadas
- **Feedback detallado**: Mensajes explicativos en español
- **Modo interactivo**: REPL para cálculos en tiempo real
- **Manejo de errores**: Mensajes descriptivos para errores comunes

## 🚀 Instalación Rápida

### Prerrequisitos
- Python 3.8 o superior
- Java Runtime Environment (JRE)

### Configuración en 3 pasos

1. **Descargar y descomprimir el proyecto**
```bash
unzip calculadora-matrices.zip
cd calculadora-matrices 
  
    Configurar entorno virtual

bash

# Crear y activar entorno
python -m venv venv_matrices
source venv_matrices/bin/activate  # Linux/Mac
# venv_matrices\Scripts\activate  # Windows

# Instalar dependencias
pip install -r requisitos.txt

    Generar parser y ejecutar

bash

# Generar archivos de ANTLR4
chmod +x configurar_entorno.sh
./configurar_entorno.sh

# Ejecutar la calculadora
python principal.py

📚 Uso Inmediato
🎯 Ejemplos para probar ahora mismo:
python

# Definir matrices 2x2
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

# Producto punto (usa *)
A * B

# Suma de matrices
A + B

# Resta de matrices  
A - B

# Matrices de diferentes dimensiones
C = [[1, 2, 3], [4, 5, 6]]
D = [[7, 8], [9, 10], [11, 12]]
C * D

# Expresión compleja con paréntesis
(A * B) + C

📊 Resultados esperados:
text

>>> A * B
[[19, 22], [43, 50]]

>>> C * D  
[[58, 64], [139, 154]]

🏗️ Estructura del Proyecto
text

calculadora-matrices/
├── 📄 README.md                    # Este archivo
├── ⚙️ GramaticaMatrices.g4         # Gramática ANTLR4 (español)
├── 🚀 principal.py                 # Programa principal con REPL
├── 🔧 visitante_matrices.py        # Motor de cálculos
├── 📋 requisitos.txt              # Dependencias Python
├── ⚡ configurar_entorno.sh        # Script de configuración automática
├── 🔄 activar_entorno.sh          # Activación rápida del entorno
│
├── 📁 Archivos generados (automáticos):
│   ├── GramaticaMatricesLexer.py
│   ├── GramaticaMatricesParser.py
│   ├── GramaticaMatricesVisitor.py
│   └── GramaticaMatricesListener.py
│
└── 💾 antlr-4.13.2-complete.jar   # Biblioteca ANTLR4

🎮 Modos de Uso
1. Modo Interactivo (REPL)
bash

python principal.py

text

matriz> A = [[1,2],[3,4]]
📝 Matriz 'A' definida: [[1.0, 2.0], [3.0, 4.0]]

matriz> B = [[5,6],[7,8]]  
📝 Matriz 'B' definida: [[5.0, 6.0], [7.0, 8.0]]

matriz> A * B
🔷 Producto punto: [[1.0, 2.0], [3.0, 4.0]] * [[5.0, 6.0], [7.0, 8.0]] = [[19.0, 22.0], [43.0, 50.0]]
🎯 RESULTADO FINAL: [[19.0, 22.0], [43.0, 50.0]]

2. Modo Script
python

from principal import evaluar_expresion

# Evaluar expresiones directamente
resultado = evaluar_expresion("[[1,2],[3,4]] * [[5,6],[7,8]]")
print(f"Resultado: {resultado}")

📖 Sintaxis Completa
Operadores Matemáticos
Operador	Operación	Ejemplo	Restricciones
*	Producto punto	A * B	columnas(A) = filas(B)
+	Suma	A + B	mismas dimensiones
-	Resta	A - B	mismas dimensiones
Definición de Matrices
python

# Matriz 2x2
[[1, 2], [3, 4]]

# Matriz 3x2
[[1, 2], [3, 4], [5, 6]]

# Matriz 2x3  
[[1, 2, 3], [4, 5, 6]]

# Números decimales
[[1.5, 2.3], [3.7, 4.1]]

Variables
python

# Asignación
A = [[1,2],[3,4]]

# Reutilización
B = A * A

# Reasignación
A = B + [[1,0],[0,1]]

🔍 Reglas de Dimensiones
✅ Operaciones Válidas

    Producto punto: (2×3) * (3×2) = (2×2)

    Suma/Resta: (2×2) + (2×2) = (2×2)

❌ Operaciones Inválidas

    (2×3) * (2×2) → Error: dimensiones incompatibles

    (2×2) + (3×3) → Error: dimensiones diferentes

🛠️ Comandos Útiles
Configuración
bash

# Configuración automática
./configurar_entorno.sh

# Activación rápida (después de la primera configuración)
./activar_entorno.sh

# Verificar instalación
python -c "import antlr4; print(f'ANTLR {antlr4.__version__}')"

Desarrollo
bash

# Regenerar parser (si modificas la gramática)
antlr4 -Dlanguage=Python3 -visitor GramaticaMatrices.g4

# Ejecutar pruebas rápidas
python -c "from principal import ejecutar_ejemplos; ejecutar_ejemplos()"

❌ Manejo de Errores

La calculadora proporciona mensajes de error descriptivos:
python

# Error de dimensiones
>>> [[1,2],[3,4]] * [[1,2]]
❌ Error: Dimensiones incompatibles para producto punto: 2x2 * 2x1

# Variable no definida  
>>> C * D
❌ Error: Variable no definida: 'C'

# Sintaxis inválida
>>> [[1,2],[3,4] * [[5,6],[7,8]]
❌ Error: missing ']' at '*'

🐛 Solución de Problemas
Problema: "java no encontrado"

Solución: Instalar Java
bash

# Ubuntu/Debian
sudo apt install default-jre

# Windows: Descargar de java.com
# macOS: brew install openjdk

Problema: "antlr4 no encontrado"

Solución: Usar el JAR directamente
bash

java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor GramaticaMatrices.g4

Problema: Error de importación

Solución: Regenerar archivos
bash

rm GramaticaMatrices*.py
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor GramaticaMatrices.g4

📊 Ejemplos Avanzados
Cadena de operaciones
python

A = [[1,0],[0,1]]
B = [[2,2],[2,2]] 
C = [[1,1],[1,1]]
resultado = A * B * C + A

Matrices identidad
python

I = [[1,0,0],[0,1,0],[0,0,1]]
A = [[1,2,3],[4,5,6],[7,8,9]]
I * A  # Resultado: misma matriz A

📄 Licencia

Este proyecto es de código abierto bajo la licencia MIT.
🤝 Contribuir

¿Encontraste un bug? ¿Tienes una mejora?

    Haz fork del proyecto

    Crea una rama: git checkout -b feature/nueva-funcionalidad

    Commit tus cambios: git commit -am 'Agrega nueva funcionalidad'

    Push: git push origin feature/nueva-funcionalidad

    Abre un Pull Request

📞 Soporte

Si necesitas ayuda:

    Revisa los ejemplos en principal.py

    Verifica que las matrices tengan dimensiones compatibles

    Asegúrate de tener Java instalado

    Ejecuta el script de configuración automática

¡Listo para calcular! 🎉 Ejecuta python principal.py y comienza a usar la calculadora.
"""
Un módulo es un archivo de Python cuyos objetos (funciones, clases, excepciones, etc.) 
pueden ser accedidos desde otro archivo. Se trata simplemente de una forma de organizar 
grandes códigos.

Un paquete es una carpeta que contiene varios módulos. Siguiendo el ejemplo anterior, 
podemos diseñar un paquete matematica creando una carpeta con la siguiente estructura.

Debe contener siempre un archivo __init__.py (por el momento vacío) para que Python 
entienda que se trata de un paquete y no de una simple carpeta.

Python tiene sus propios módulos, los cuales forman parte de su librería de módulos 
estándar, que también pueden ser importados.

PEP 8: importación
La importación de módulos debe realizarse al comienzo del documento, en orden alfabético 
de paquetes y módulos.

Primero deben importarse los módulos propios de Python. Luego, los módulos de terceros 
y finalmente, los módulos propios de la aplicación.

Entre cada bloque de imports, debe dejarse una línea en blanco.
"""

# Importación de un módulo que se encuentra en la misma ruta:
from modulos1 import multiplicar, dividir, canal
# Importación desde un paquete:
# import mi_paquete.funciones_matematicas
import mi_paquete.funciones_matematicas as fun_mat
# from mi_paquete.funciones_matematicas import calcular_factorial, frase
# Importación de un sub paquete:
from mi_paquete.sub_paquete1.funciones_avanzadas import contar_letras

import datetime
from datetime import datetime
"""
import modulos1

print(modulos1.multiplicar(7, 8))
print(modulos1.sumar(7, 8))
print(modulos1.restar(7, 8))
print(modulos1.dividir(7, 8))
"""

print(multiplicar(19, 2))
print(canal)
print(fun_mat.calcular_factorial(5))
print(fun_mat.frase)

texto = "Gracias por apoyar mi canal!"
print(contar_letras(texto))

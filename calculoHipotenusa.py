# U. Internacional de Aguascalientes
# Doctorado en Tecnologías de la Transformación Digital
# Materia:  Ingeniería para el procesamiento masivo de datos
# Tutor:    Dr. Jonás Velasco Álvarez
# Alumno:   Luis Alejandro Santana Valadez
# Trabajo:  1.2 Ejercicios de Programación (Python)
# Objetivo: Diseño de una función para calcular el valor de la Hipotenusa
#           mediante el Teorema de Pitágoras
# --------------------------------------------------------------------------

import math

# ----------------------------------------------------------
# (1) - Definición de la función principal calcular_hipotenusa()
# ----------------------------------------------------------
def calcular_hipotenusa(a, b):
    """
    Objetivo:
        Calcula la hipotenusa de un triángulo rectángulo usando el teorema de Pitágoras.
    Parámetros:
        a (float): Longitud del primer cateto.
        b (float): Longitud del segundo cateto.
    Retorna:
        float: Longitud de la hipotenusa.
    """
    return math.sqrt(a**2 + b**2)

# ----------------------------------------------------------
# (2) - Programa principal
# ----------------------------------------------------------
print("\n<< Calcular la Hipotenusa >>\n")

while True:
    try:
        # Entrada de los catetos
        cateto1 = float(input("Introduce la longitud del primer cateto: "))
        cateto2 = float(input("Introduce la longitud del segundo cateto: "))

        # Calcular hipotenusa y mostrar resultado
        hipotenusa = calcular_hipotenusa(cateto1, cateto2)
        print(f"La hipotenusa del triángulo es: {hipotenusa:.2f}")
    except ValueError:
        print("Entrada inválida. Por favor, introduce valores numéricos válidos.")

    # Preguntar si desea repetir
    repetir = input("\n¿Deseas calcular otra hipotenusa? (S/s para continuar): ")
    if repetir.lower() != 's':
        print("\n<< Proceso finalizado. ¡Hasta luego! >>\n")
        break


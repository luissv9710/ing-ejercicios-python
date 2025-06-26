# U. Internacional de Aguascalientes
# Doctorado en Tecnologías de la Transformación Digital
# Materia:  Ingeniería para el procesamiento masivo de datos
# Tutor:    Dr. Jonás Velasco Álvarez
# Alumno:   Luis Alejandro Santana Valadez
# Trabajo:  1.2 Ejercicios de Programación (Python)
# Objetivo: Diseño de una función para generar una contraseña aleatoria
# --------------------------------------------------------------------------

import random

# ----------------------------------------------------------
# (1) - Definición de la función principal generar_contrasena()
# ----------------------------------------------------------
def generar_contrasena():
    """
    Objetivo:
        Genera una contraseña aleatoria con longitud entre 7 y 10 caracteres.
        Cada carácter se elige de forma aleatoria en el rango ASCII 33 al 126.
    Retorna:
        str: Contraseña generada aleatoriamente.
    """
    longitud = random.randint(7, 10)  # Longitud aleatoria entre 7 y 10
    contrasena = ""

    for _ in range(longitud):
        ascii_code = random.randint(33, 126)  # Caracteres imprimibles
        contrasena += chr(ascii_code)  # Convertir código ASCII a carácter

    return contrasena

# ----------------------------------------------------------
# (2) - Programa principal
# ----------------------------------------------------------
print("\n<< Contraseña Aleatoria >>\n")

while True:
    # Generar y mostrar contraseña
    nueva_contrasena = generar_contrasena()
    print(f"Contraseña generada: {nueva_contrasena}")

    # Preguntar si se desea repetir el proceso
    repetir = input("\n¿Deseas generar otra contraseña? (S/s para continuar): ")
    if repetir.lower() != 's':
        print("\n<< Proceso finalizado. ¡Hasta pronto! >>\n")
        break


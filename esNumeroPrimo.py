# U. Internacional de Aguascalientes
# Doctorado en Tecnologías de la Transformación Digital
# Materia:  Ingeniería para el procesamiento masivo de datos
# Tutor:    Dr. Jonás Velasco Álvarez
# Alumno:   Luis Alejandro Santana Valadez
# Trabajo:  1.2 Ejercicios de Programación (Python)
# Objetivo: Diseño de función para determinar si un número es primo o no
# --------------------------------------------------------------------------

# ----------------------------------------------------------
# (1) - Definición de la función principal es_primo(n)
# ----------------------------------------------------------
def es_primo(n):
    """
    Objetivo:
        Determina si un número entero positivo es primo.
    Parámetros:
        n (int): Número entero mayor que 1 a evaluar.
    Retorna:
        bool: True si es primo, False en caso contrario.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Verificación principal de n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    return True

# ----------------------------------------------------------
# (2) - Programa principal
# ----------------------------------------------------------
print("\n<< ¿ Es un Número Primo ? >>\n")

while True:
    try:
        # Leer número del usuario
        numero = int(input("Introduce un número entero: "))

        # Evaluar si es primo e imprimir resultado
        if es_primo(numero):
            print(f"{numero} SI es un número primo.")
        else:
            print(f"{numero} NO es un número primo.")
    except ValueError:
        print("Por favor, introduce un número entero válido.")

    # Preguntar si desea repetir
    repetir = input("\n¿Deseas probar otro número? (S/s para continuar): ")
    if repetir.lower() != 's':
        print("\n<< Proceso finalizado. ¡Hasta pronto! >>\n")
        break

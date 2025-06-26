# U. Internacional de Aguascalientes
# Doctorado en Tecnologías de la Transformación Digital
# Materia:  Ingeniería para el procesamiento masivo de datos
# Tutor:    Dr. Jonás Velasco Álvarez
# Alumno:   Luis Alejandro Santana Valadez
# Trabajo:  1.2 Ejercicios de Programación (Python)
# Objetivo: Diseño de una función para determinar el siguiente número primo
#           de un número introducido, reutilizando el programa esnum-primo.py
# --------------------------------------------------------------------------

# ----------------------------------------------------------
# (1) - Definición de la función principal siguiente_primo(n)
# ----------------------------------------------------------
def siguiente_primo(n):
    """
    Objetivo:
        Encuentra y devuelve el primer número primo mayor que n.
    Parámetros:
        n (int): Número entero de referencia.
    Retorna:
        int: El siguiente número primo mayor que n.
    """
    candidato = n + 1
    while not es_primo(candidato):
        candidato += 1
    return candidato

# ----------------------------------------------------------
# (2) - Definición de la función secundaria es_primo(n)
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
# (3) - Programa principal
# ----------------------------------------------------------
print("\n<< Siguiente Número Primo >>\n")

while True:
    try:
        # Leer número del usuario
        numero = int(input("Introduce un número entero: "))

        # Encontrar y mostrar el siguiente número primo
        siguiente = siguiente_primo(numero)
        print(f"El siguiente número primo después de {numero} es {siguiente}.")
    except ValueError:
        print("Entrada inválida. Por favor, introduce un número entero válido.")

    # Preguntar si desea repetir el proceso
    repetir = input("\n¿Deseas probar con otro número? (S/s para continuar): ")
    if repetir.lower() != 's':
        print("\n<< Proceso finalizado. ¡Hasta luego! >>\n")
        break


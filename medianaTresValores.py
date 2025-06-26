# U. Internacional de Aguascalientes
# Doctorado en Tecnologías de la Transformación Digital
# Materia:  Ingeniería para el procesamiento masivo de datos
# Tutor:    Dr. Jonás Velasco Álvarez
# Alumno:   Luis Alejandro Santana Valadez
# Trabajo:  1.2 Ejercicios de Programación (Python)
# Objetivo: Diseño de una función para determinar la mediana de 3 números
#           introducidos por el usuario
# --------------------------------------------------------------------------

# ----------------------------------------------------------
# (1) - Definición de la función principal mediana(n)
# ----------------------------------------------------------
def mediana(a, b, c):
    """
    Objetivo:
        Calcula la mediana (valor medio) de tres números.
    Parámetros:
        a, b, c (float): Tres números a evaluar (se reciben tipo float).
    Retorna:
        float: El valor medio entre los tres números dados (mismo tipo float).
    """
    lista = [a, b, c]   # Se genera la lista con los elementos recibidos
    lista.sort()        # Se ordenan los tres valores
    return lista[1]     # El de enmedio es la mediana !!

# ----------------------------------------------------------
# (2) - Programa principal
# ----------------------------------------------------------
print("\n<< Mediana de Tres Valores >>\n")

while True:
    try:
        # Entrada de tres valores desde el usuario
        x = float(input("Introduce el primer número: "))
        y = float(input("Introduce el segundo número: "))
        z = float(input("Introduce el tercer número: "))

        # Calcular e imprimir la mediana
        resultado = mediana(x, y, z)
        print(f"La mediana de {x}, {y} y {z} es: {resultado}")
    except ValueError:
        print("Por favor, introduce solo valores numéricos válidos.")

    # Preguntar si desea repetir el proceso
    repetir = input("\n¿Deseas calcular otra mediana? (S/s para continuar): ")
    if repetir.lower() != 's':
        print("\n<< Proceso finalizado. ¡Hasta pronto! >>\n")
        break


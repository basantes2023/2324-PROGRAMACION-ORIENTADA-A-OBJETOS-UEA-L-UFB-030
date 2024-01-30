def ingresar_temperaturas_diarias():
    temperaturas = []
    dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    for dia in dias_semana:
        temperatura = float(input(f"Ingrese la temperatura del {dia}: "))
        temperaturas.append(temperatura)
    return temperaturas


def calcular_promedio_semanal(temperaturas):
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio


def main():
    temperaturas = ingresar_temperaturas_diarias()
    promedio = calcular_promedio_semanal(temperaturas)
    print(f"El promedio semanal del clima es: {promedio}")


if __name__ == "__main__":
    main()

# En este programa, se definen tres funciones:

# 1. La función ingresar_temperaturas_diarias() solicita al usuario ingresar las temperaturas diarias durante una semana para cada día de la semana (lunes, martes, miércoles, jueves, viernes, sábado y domingo) y las almacena en una lista.
# 2. La función calcular_promedio_semanal(temperaturas) recibe la lista de temperaturas y calcula el promedio semanal.
# 3. La función main() es la función principal que llama a las otras dos funciones y muestra el resultado final.

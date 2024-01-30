class ClimaSemana:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas_diarias(self):
        dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        for dia in dias_semana:
            temperatura = float(input(f"Ingrese la temperatura del {dia}: "))
            self.temperaturas.append(temperatura)

    def calcular_promedio_semanal(self):
        suma = sum(self.temperaturas)
        promedio = suma / len(self.temperaturas)
        return promedio


def main():
    clima_semana = ClimaSemana()
    clima_semana.ingresar_temperaturas_diarias()
    promedio = clima_semana.calcular_promedio_semanal()
    print(f"El promedio semanal del clima es: {promedio}")


if __name__ == "__main__":
    main()

# En este programa, se define una clase llamada ClimaSemana que tiene dos métodos:

# 1. (El método ingresar_temperaturas_diarias() solicita al usuario ingresar las temperaturas diarias durante una semana para cada día de la semana (lunes, martes, miércoles, jueves, viernes, sábado y domingo)
# y las almacena en una lista dentro del objeto ClimaSemana.)
# 2. El método calcular_promedio_semanal() utiliza la lista de temperaturas almacenadas en el objeto ClimaSemana para calcular el promedio semanal.
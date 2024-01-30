# Programa: Reserva de pasajes aéreos
# Este programa utiliza la clase Vuelo para representar un vuelo con todos los detalles necesarios, como número de asiento, hora de salida y llegada, aeropuerto de salida y llegada, nombre del pasajero, número de pasaporte, nacionalidad, ciudad de origen-destino, valor del pasaje y el valor total a pagar por los boletos.
# También demuestra la interacción entre los objetos al reservar asientos
class Vuelo:
    def __init__(self, numero, fecha, asientos_disponibles, ciudad_origen, ciudad_destino, aeropuerto_salida,
                 aeropuerto_llegada, hora_salida, hora_llegada):
        self.numero = numero
        self.fecha = fecha
        self.asientos_disponibles = asientos_disponibles
        self.asientos = {}
        self.ciudad_origen = ciudad_origen
        self.ciudad_destino = ciudad_destino
        self.aeropuerto_salida = aeropuerto_salida
        self.aeropuerto_llegada = aeropuerto_llegada
        self.hora_salida = hora_salida
        self.hora_llegada = hora_llegada

    def mostrar_informacion(self):
        print("Vuelo:", self.numero)
        print("Fecha:", self.fecha)
        print("Asientos disponibles:", self.asientos_disponibles)
        print("Ciudad de origen:", self.ciudad_origen)
        print("Ciudad de destino:", self.ciudad_destino)
        print("Aeropuerto de salida:", self.aeropuerto_salida)
        print("Aeropuerto de llegada:", self.aeropuerto_llegada)
        print("Hora de salida:", self.hora_salida)
        print("Hora de llegada:", self.hora_llegada)

    def reservar_asiento(self, numero_asiento, nombre_pasajero, numero_pasaporte, nacionalidad, valor_pasaje):
        if self.asientos_disponibles > 0:
            if numero_asiento not in self.asientos:
                self.asientos[numero_asiento] = {"nombre_pasajero": nombre_pasajero,
                                                 "numero_pasaporte": numero_pasaporte, "nacionalidad": nacionalidad,
                                                 "valor_pasaje": valor_pasaje}
                self.asientos_disponibles -= 1
                print("Asiento", numero_asiento, "reservado para", nombre_pasajero)
            else:
                print("El asiento", numero_asiento, "ya está ocupado.")
        else:
            print("Lo siento, no hay asientos disponibles en este vuelo.")

    def calcular_valor_total(self):
        total_a_pagar = 0
        for asiento, pasajero in self.asientos.items():
            total_a_pagar += pasajero["valor_pasaje"]
        print("El valor total a pagar por los boletos es:", total_a_pagar)

    def mostrar_pasajeros(self):
        if self.asientos_disponibles == 0:
            print("No hay pasajeros en este vuelo.")
        else:
            print("Pasajeros en el vuelo", self.numero)
            for asiento, pasajero in self.asientos.items():
                print("Asiento:", asiento)
                print("Nombre del pasajero:", pasajero["nombre_pasajero"])
                print("Número de pasaporte:", pasajero["numero_pasaporte"])
                print("Nacionalidad:", pasajero["nacionalidad"])
                print("Valor del pasaje:", pasajero["valor_pasaje"])


class TarjetaCredito:
    def __init__(self, numero_tarjeta, nombre_titular, fecha_vencimiento, cvv):
        self.numero_tarjeta = numero_tarjeta
        self.nombre_titular = nombre_titular
        self.fecha_vencimiento = fecha_vencimiento
        self.cvv = cvv

    def procesar_pago(self, monto):
        print("Procesando pago de", monto, "con tarjeta de crédito", self.numero_tarjeta)
        # Aquí iría la lógica para procesar el pago con la tarjeta de crédito


# Ejemplo de uso
vuelo = Vuelo("593 American Airlines", "2023-12-23", 100, "Quito", "New York", "Internacional Simón Bolivar",
              "Jhon F. Kennedy", "14:00", "20:00")
vuelo.mostrar_informacion()

vuelo.reservar_asiento(1, "Carlos Tamayo", "1710817658", "Ecuatoriana", 380)
vuelo.reservar_asiento(2, "Pamela Cárdenas", "1002501250", "Ecuatoriana", 350)

vuelo.mostrar_pasajeros()

vuelo.calcular_valor_total()

tarjeta = TarjetaCredito("1234567890123456", "Carlos Tamayo", "12/24", "593")
tarjeta.procesar_pago(730)


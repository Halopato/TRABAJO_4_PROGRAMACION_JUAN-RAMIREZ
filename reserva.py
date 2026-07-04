from excepciones import ReservaError
from logger import Logger


class Reserva:
    """
    Clase que representa una reserva realizada por un cliente.
    """

    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self, descuento=0):
        try:
            self.servicio.validar()
            costo = self.servicio.calcular_costo(self.duracion, descuento)
            self.estado = "Confirmada"

            Logger.registrar(
                f"Reserva confirmada para {self.cliente.nombre} - "
                f"{self.servicio.descripcion()} - Total: ${costo:.2f}"
            )

            return costo

        except Exception as error:
            Logger.registrar(f"Error al confirmar reserva: {error}")
            raise ReservaError("No fue posible confirmar la reserva.") from error

    def cancelar(self):
        self.estado = "Cancelada"
        Logger.registrar(
            f"Reserva cancelada por {self.cliente.nombre}"
        )

    def mostrar(self):
        return (
            f"Cliente: {self.cliente.nombre}\n"
            f"Servicio: {self.servicio.descripcion()}\n"
            f"Duración: {self.duracion} hora(s)\n"
            f"Estado: {self.estado}"
        )

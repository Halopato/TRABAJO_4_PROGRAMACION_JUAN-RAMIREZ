from servicio import Servicio
from excepciones import ServicioNoDisponibleError, DuracionInvalidaError


class ReservaSala(Servicio):

    def calcular_costo(self, duracion, descuento=0):
        if duracion <= 0:
            raise DuracionInvalidaError("La duración debe ser mayor que cero.")
        total = self.precio_base * duracion
        return total - (total * descuento / 100)

    def descripcion(self):
        return "Servicio de reserva de salas."

    def validar(self):
        if self.precio_base <= 0:
            raise ServicioNoDisponibleError("Precio inválido.")


class AlquilerEquipo(Servicio):

    def calcular_costo(self, duracion, descuento=0):
        if duracion <= 0:
            raise DuracionInvalidaError("Duración inválida.")
        total = (self.precio_base * duracion) + 25
        return total - (total * descuento / 100)

    def descripcion(self):
        return "Servicio de alquiler de equipos."

    def validar(self):
        if self.precio_base <= 0:
            raise ServicioNoDisponibleError("Precio inválido.")


class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, duracion, descuento=0):
        if duracion <= 0:
            raise DuracionInvalidaError("Duración inválida.")
        total = (self.precio_base * duracion) * 1.2
        return total - (total * descuento / 100)

    def descripcion(self):
        return "Servicio de asesorías especializadas."

    def validar(self):
        if self.precio_base <= 0:
            raise ServicioNoDisponibleError("Precio inválido.")

from abc import ABC, abstractmethod


class Servicio(ABC):
    """
    Clase abstracta que representa un servicio ofrecido por Software FJ.
    """

    def __init__(self, nombre, precio_base):
        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0):
        """Calcula el costo del servicio."""
        pass

    @abstractmethod
    def descripcion(self):
        """Devuelve la descripción del servicio."""
        pass

    @abstractmethod
    def validar(self):
        """Valida los datos del servicio."""
        pass

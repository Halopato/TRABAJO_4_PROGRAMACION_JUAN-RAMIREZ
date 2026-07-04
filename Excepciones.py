"""
Módulo de excepciones personalizadas del sistema Software FJ.
"""


class ClienteInvalidoError(Exception):
    """Se genera cuando los datos del cliente no son válidos."""
    pass


class ServicioNoDisponibleError(Exception):
    """Se genera cuando un servicio no está disponible."""
    pass


class ReservaError(Exception):
    """Se genera cuando ocurre un error en una reserva."""
    pass


class DuracionInvalidaError(Exception):
    """Se genera cuando la duración es menor o igual a cero."""
    pass

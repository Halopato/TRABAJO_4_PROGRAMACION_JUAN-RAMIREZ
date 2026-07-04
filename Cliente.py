from excepciones import ClienteInvalidoError


class Cliente:
    """
    Clase que representa a un cliente del sistema Software FJ.
    Aplica encapsulación mediante atributos privados.
    """

    def __init__(self, nombre, identificacion, correo):
        self.nombre = nombre
        self.identificacion = identificacion
        self.correo = correo

    # -------- Nombre --------
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or not valor.strip():
            raise ClienteInvalidoError("El nombre no puede estar vacío.")
        self.__nombre = valor.strip()

    # -------- Identificación --------
    @property
    def identificacion(self):
        return self.__identificacion

    @identificacion.setter
    def identificacion(self, valor):
        if not str(valor).isdigit():
            raise ClienteInvalidoError("La identificación debe contener solo números.")
        self.__identificacion = str(valor)

    # -------- Correo --------
    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):
        if "@" not in valor or "." not in valor:
            raise ClienteInvalidoError("Correo electrónico inválido.")
        self.__correo = valor

    def mostrar_datos(self):
        return (
            f"Cliente: {self.nombre} | "
            f"ID: {self.identificacion} | "
            f"Correo: {self.correo}"
        )

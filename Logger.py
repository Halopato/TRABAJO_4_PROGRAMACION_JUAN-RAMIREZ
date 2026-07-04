from datetime import datetime


class Logger:

    ARCHIVO_LOG = "errores.log"

    @staticmethod
    def registrar(mensaje):
        with open(Logger.ARCHIVO_LOG, "a", encoding="utf-8") as archivo:
            archivo.write(
                f"[{datetime.now()}] {mensaje}\n"
            )

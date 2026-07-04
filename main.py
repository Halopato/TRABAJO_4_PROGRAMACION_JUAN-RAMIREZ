from cliente import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from excepciones import (
    ClienteInvalidoError,
    ServicioNoDisponibleError,
    DuracionInvalidaError,
    ReservaError
)
from logger import Logger


def mostrar_titulo(texto):
    print("\n" + "=" * 60)
    print(texto)
    print("=" * 60)


def ejecutar_prueba(numero, descripcion, funcion):
    print(f"\nPrueba {numero}: {descripcion}")

    try:
        funcion()
    except (
        ClienteInvalidoError,
        ServicioNoDisponibleError,
        DuracionInvalidaError,
        ReservaError
    ) as error:
        print("❌ Error:", error)
        Logger.registrar(f"Prueba {numero}: {error}")
    except Exception as error:
        print("❌ Error inesperado:", error)
        Logger.registrar(f"Prueba {numero}: {error}")
    else:
        print("✅ Operación realizada correctamente.")
    finally:
        print("-" * 60)


mostrar_titulo("SOFTWARE FJ - SIMULACIÓN DEL SISTEMA")

# -----------------------------------------------------
# CLIENTES
# -----------------------------------------------------

cliente1 = Cliente("Juan Ramírez", "1001234567", "juan@email.com")
cliente2 = Cliente("María López", "1012345678", "maria@email.com")

# -----------------------------------------------------
# SERVICIOS
# -----------------------------------------------------

sala = ReservaSala("Sala de reuniones", 50)
equipo = AlquilerEquipo("Video Beam", 30)
asesoria = AsesoriaEspecializada("Asesoría Python", 80)

# -----------------------------------------------------
# PRUEBA 1
# -----------------------------------------------------

def prueba1():
    reserva = Reserva(cliente1, sala, 2)
    total = reserva.confirmar()
    print(reserva.mostrar())
    print("Total:", total)

ejecutar_prueba(1, "Reserva de sala", prueba1)

# -----------------------------------------------------
# PRUEBA 2
# -----------------------------------------------------

def prueba2():
    reserva = Reserva(cliente2, equipo, 5)
    total = reserva.confirmar(10)
    print(reserva.mostrar())
    print("Total:", total)

ejecutar_prueba(2, "Alquiler de equipo con descuento", prueba2)

# -----------------------------------------------------
# PRUEBA 3
# -----------------------------------------------------

def prueba3():
    reserva = Reserva(cliente1, asesoria, 3)
    total = reserva.confirmar()
    print(reserva.mostrar())
    print("Total:", total)

ejecutar_prueba(3, "Asesoría especializada", prueba3)

# -----------------------------------------------------
# PRUEBA 4
# -----------------------------------------------------

def prueba4():
    reserva = Reserva(cliente1, sala, -2)
    reserva.confirmar()

ejecutar_prueba(4, "Duración inválida", prueba4)

# -----------------------------------------------------
# PRUEBA 5
# -----------------------------------------------------

def prueba5():
    Cliente("", "123", "correo@email.com")

ejecutar_prueba(5, "Nombre vacío", prueba5)

# -----------------------------------------------------
# PRUEBA 6
# -----------------------------------------------------

def prueba6():
    Cliente("Pedro", "ABC123", "correo@email.com")

ejecutar_prueba(6, "Identificación inválida", prueba6)

# -----------------------------------------------------
# PRUEBA 7
# -----------------------------------------------------

def prueba7():
    Cliente("Ana", "123456", "correo")

ejecutar_prueba(7, "Correo inválido", prueba7)

# -----------------------------------------------------
# PRUEBA 8
# -----------------------------------------------------

def prueba8():
    servicio = ReservaSala("Sala Premium", -100)
    reserva = Reserva(cliente1, servicio, 2)
    reserva.confirmar()

ejecutar_prueba(8, "Servicio con precio inválido", prueba8)

# -----------------------------------------------------
# PRUEBA 9
# -----------------------------------------------------

def prueba9():
    reserva = Reserva(cliente2, asesoria, 1)
    reserva.cancelar()
    print(reserva.mostrar())

ejecutar_prueba(9, "Cancelar reserva", prueba9)

# -----------------------------------------------------
# PRUEBA 10
# -----------------------------------------------------

def prueba10():
    servicios = [sala, equipo, asesoria]

    for servicio in servicios:
        print(servicio.descripcion())
        print("Costo:", servicio.calcular_costo(2))

ejecutar_prueba(10, "Demostración de polimorfismo", prueba10)

mostrar_titulo("FIN DE LA SIMULACIÓN")

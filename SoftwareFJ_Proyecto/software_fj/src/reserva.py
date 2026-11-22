from entidad import Entidad
from excepciones import ReservaError, ServicioNoDisponibleError


class Reserva(Entidad):
    def __init__(self, codigo, cliente, servicio, duracion):
        super().__init__(codigo)
        if cliente is None or servicio is None:
            raise ReservaError("La reserva debe tener cliente y servicio.")
        servicio.validar_parametros(duracion)
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"
        self.total = servicio.calcular_costo(duracion)

    def confirmar(self):
        if not self.servicio.disponible:
            raise ServicioNoDisponibleError("El servicio no está disponible en este momento.")
        if self.estado != "Pendiente":
            raise ReservaError("Solo se pueden confirmar reservas pendientes.")
        self.estado = "Confirmada"
        return self.estado


    def cancelar(self):
        if self.estado == "Cancelada":
            raise ReservaError("La reserva ya está cancelada.")
        self.estado = "Cancelada"
        return self.estado


    def procesar(self):
        try:
            self.confirmar()
        except ServicioNoDisponibleError as error:
            raise ReservaError("No se pudo procesar la reserva por disponibilidad.") from error
        else:
            return f"Reserva {self.identificador} confirmada. Total: ${self.total:,.0f}"
        finally:
            # El bloque se ejecuta aunque la confirmación falle.
            pass

    def describir(self):
        return (f"Reserva {self.identificador}: {self.cliente.nombre} - {self.servicio.nombre} - "
                f"{self.duracion} - Estado: {self.estado} - Total: ${self.total:,.0f}")

from abc import ABC, abstractmethod
from entidad import Entidad
from excepciones import DatoInvalidoError


class Servicio(Entidad, ABC):
    def __init__(self, codigo, nombre, tarifa, disponible=True):
        super().__init__(codigo)
        if not isinstance(tarifa, (int, float)) or tarifa <= 0:
            raise DatoInvalidoError("La tarifa debe ser un número mayor a cero.")
        self.nombre = nombre
        self.tarifa = float(tarifa)
        self.disponible = disponible



    @abstractmethod
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        """Calcula el costo. Impuesto y descuento se reciben como porcentajes."""
        pass



    @abstractmethod
    def describir(self):
        pass



    @abstractmethod
    def validar_parametros(self, duracion):
        pass



    def _calcular_total(self, subtotal, impuesto=0, descuento=0):
        if not (0 <= impuesto <= 100 and 0 <= descuento <= 100):
            raise DatoInvalidoError("Impuesto y descuento deben estar entre 0 y 100.")
        return subtotal + subtotal * impuesto / 100 - subtotal * descuento / 100



class ReservaSala(Servicio):
    def validar_parametros(self, duracion):
        if duracion <= 0 or duracion > 12:
            raise DatoInvalidoError("La sala se puede reservar entre 1 y 12 horas.")
        return True



    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self.validar_parametros(duracion)
        return self._calcular_total(self.tarifa * duracion, impuesto, descuento)



    def describir(self):
        return f"Reserva de sala: {self.nombre} (tarifa por hora: ${self.tarifa:,.0f})"



class AlquilerEquipo(Servicio):
    def validar_parametros(self, duracion):
        if duracion <= 0 or duracion > 30:
            raise DatoInvalidoError("El alquiler de equipo debe ser de 1 a 30 días.")
        return True



    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self.validar_parametros(duracion)
        return self._calcular_total(self.tarifa * duracion, impuesto, descuento)



    def describir(self):
        return f"Alquiler de equipo: {self.nombre} (tarifa por día: ${self.tarifa:,.0f})"



class Asesoria(Servicio):
    def validar_parametros(self, duracion):
        if duracion <= 0 or duracion > 8:
            raise DatoInvalidoError("La asesoría debe durar entre 1 y 8 horas.")
        return True



    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self.validar_parametros(duracion)
        return self._calcular_total(self.tarifa * duracion, impuesto, descuento)



    def describir(self):
        return f"Asesoría especializada: {self.nombre} (tarifa por hora: ${self.tarifa:,.0f})"

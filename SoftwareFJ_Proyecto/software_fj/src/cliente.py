from entidad import Entidad
from excepciones import DatoInvalidoError


class Cliente(Entidad):
    def __init__(self, documento, nombre, correo, telefono):
        super().__init__(documento)
        self.__documento = documento
        self.__nombre = self._validar_nombre(nombre)
        self.__correo = self._validar_correo(correo)
        self.__telefono = self._validar_telefono(telefono)

    @staticmethod
    def _validar_nombre(nombre):
        if not isinstance(nombre, str) or len(nombre.strip()) < 2:
            raise DatoInvalidoError("El nombre debe tener al menos dos caracteres.")
        return nombre.strip()


    @staticmethod
    def _validar_correo(correo):
        if not isinstance(correo, str) or "@" not in correo or "." not in correo.split("@")[-1]:
            raise DatoInvalidoError("El correo no tiene un formato válido.")
        return correo.strip().lower()


    @staticmethod
    def _validar_telefono(telefono):
        telefono = str(telefono).strip()
        if not telefono.isdigit() or len(telefono) < 7:
            raise DatoInvalidoError("El teléfono debe tener al menos 7 números.")
        return telefono


    @property
    def documento(self):
        return self.__documento



    @property
    def nombre(self):
        return self.__nombre



    @property
    def correo(self):
        return self.__correo



    @property
    def telefono(self):
        return self.__telefono



    def describir(self):
        return f"Cliente: {self.nombre} | Documento: {self.documento} | Correo: {self.correo}"

    def __str__(self):
        return self.describir()

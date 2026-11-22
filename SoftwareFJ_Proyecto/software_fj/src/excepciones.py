# Excepciones propias del sistema Software FJ

class ErrorSistema(Exception):
    """Error general del sistema."""
    pass


class DatoInvalidoError(ErrorSistema):
    pass


class ClienteNoEncontradoError(ErrorSistema):
    pass


class ServicioNoDisponibleError(ErrorSistema):
    pass


class ReservaError(ErrorSistema):
    pass

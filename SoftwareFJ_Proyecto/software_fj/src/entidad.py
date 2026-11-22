from abc import ABC, abstractmethod


class Entidad(ABC):
    """Clase abstracta base para entidades que tienen un identificador."""
    def __init__(self, identificador):
        if not identificador:
            raise ValueError("El identificador es obligatorio.")
        self.identificador = identificador

    @abstractmethod
    def describir(self):
        """Cada entidad debe indicar cómo se muestra su información."""
        pass

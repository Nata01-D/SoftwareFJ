import logging
from pathlib import Path

from cliente import Cliente
from reserva import Reserva
from servicio import ReservaSala, AlquilerEquipo, Asesoria
from excepciones import ErrorSistema, DatoInvalidoError, ClienteNoEncontradoError

# Crear automáticamente la carpeta de registros.
BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Guardar los eventos y errores del sistema.
logging.basicConfig(
    filename=str(LOG_DIR / "software_fj.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

class SistemaFJ:
    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

    def registrar_cliente(self, cliente):
        if any(c.documento == cliente.documento for c in self.clientes):
            raise DatoInvalidoError("Ya existe un cliente con ese documento.")
        self.clientes.append(cliente)
        logging.info("Cliente registrado: %s", cliente.documento)
        return cliente



    def buscar_cliente(self, documento):
        for cliente in self.clientes:
            if cliente.documento == documento:
                return cliente
        raise ClienteNoEncontradoError(f"No se encontró cliente {documento}.")



    def agregar_servicio(self, servicio):
        if any(s.identificador == servicio.identificador for s in self.servicios):
            raise DatoInvalidoError("Ya existe un servicio con ese código.")
        self.servicios.append(servicio)
        logging.info("Servicio agregado: %s", servicio.identificador)
        return servicio



    def crear_reserva(self, codigo, documento, codigo_servicio, duracion):
        cliente = self.buscar_cliente(documento)
        servicio = next((s for s in self.servicios if s.identificador == codigo_servicio), None)
        if servicio is None:
            raise ErrorSistema("No se encontró el servicio solicitado.")
        if any(r.identificador == codigo for r in self.reservas):
            raise DatoInvalidoError("El código de reserva ya existe.")
        reserva = Reserva(codigo, cliente, servicio, duracion)
        self.reservas.append(reserva)
        logging.info("Reserva creada: %s", codigo)
        return reserva



    def listar(self, elementos):
        if not elementos:
            print("No hay elementos registrados.")
        else:
            for elemento in elementos:
                print(elemento.describir())

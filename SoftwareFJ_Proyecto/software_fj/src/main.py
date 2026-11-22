import os
import logging
from sistema import SistemaFJ
from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, Asesoria
from excepciones import ErrorSistema

# Crear la carpeta de logs si todavía no existe.
os.makedirs("logs", exist_ok=True)
sistema = SistemaFJ()


def ejecutar_prueba(numero, titulo, funcion):
    print(f"\n--- Operación {numero}: {titulo} ---")
    try:
        resultado = funcion()
    except Exception as error:
        logging.exception("Operación %s falló: %s", numero, error)
        print(f"Error controlado: {error}")
    else:
        if resultado is not None:
            print(resultado)
        print("Operación realizada correctamente.")
    finally:
        print("Fin de la operación.")


def crear_cliente(documento, nombre, correo, telefono):
    cliente = Cliente(documento, nombre, correo, telefono)
    sistema.registrar_cliente(cliente)
    return cliente



# 1. Registrar un cliente con datos correctos.
ejecutar_prueba(1, "Registrar cliente válido", lambda: crear_cliente("101", "Laura Gómez", "laura@mail.com", "3001234567"))

# 2. Intentar registrar un cliente con correo incorrecto.
ejecutar_prueba(2, "Cliente con correo inválido", lambda: crear_cliente("102", "Pedro Ruiz", "pedrocorreo", "3019876543"))

# 3. Registrar otro cliente correctamente.
ejecutar_prueba(3, "Registrar segundo cliente", lambda: crear_cliente("103", "Camila Rojas", "camila@correo.com", "3105556677"))

# 4. Crear servicio de reserva de sala.
ejecutar_prueba(4, "Crear servicio de sala", lambda: sistema.agregar_servicio(ReservaSala("S1", "Sala de reuniones", 45000)))
# 5. Crear servicio de alquiler de equipos.
ejecutar_prueba(5, "Crear servicio de equipo", lambda: sistema.agregar_servicio(AlquilerEquipo("E1", "Proyector", 30000)))
# 6. Crear servicio de asesoría.
ejecutar_prueba(6, "Crear servicio de asesoría", lambda: sistema.agregar_servicio(Asesoria("A1", "Asesoría informática", 65000)))
# 7. Crear servicio con tarifa inválida.
ejecutar_prueba(7, "Servicio con tarifa negativa", lambda: sistema.agregar_servicio(Asesoria("A2", "Servicio inválido", -100)))
# 8. Crear una reserva válida.
def reserva_valida():
    reserva = sistema.crear_reserva("R1", "101", "S1", 2)
    return reserva.procesar()
ejecutar_prueba(8, "Reserva correcta y confirmación", reserva_valida)
# 9. Calcular costo con impuesto y descuento (parámetros opcionales).
def costo_con_descuento():
    servicio = sistema.servicios[0]
    costo = servicio.calcular_costo(2, impuesto=19, descuento=10)
    return f"Costo con impuesto del 19% y descuento del 10%: ${costo:,.0f}"
ejecutar_prueba(9, "Calcular costo con porcentajes", costo_con_descuento)
# 10. Crear reserva con duración incorrecta.
ejecutar_prueba(10, "Reserva con duración inválida", lambda: sistema.crear_reserva("R2", "101", "S1", 0))
# 11. Buscar un cliente que no existe.
ejecutar_prueba(11, "Buscar cliente inexistente", lambda: sistema.buscar_cliente("999"))
# 12. Crear reserva para servicio no disponible y mostrar encadenamiento de excepciones.
def reserva_no_disponible():
    servicio = sistema.servicios[1]
    servicio.disponible = False
    reserva = sistema.crear_reserva("R3", "103", "E1", 1)
    try:
        reserva.procesar()
    except ErrorSistema as error:
        print(f"Se manejó la excepción de reserva: {error}")
        if error.__cause__:
            print(f"Error original: {error.__cause__}")
        raise

ejecutar_prueba(12, "Reserva de servicio no disponible", reserva_no_disponible)
# 13. Cancelar una reserva existente.
def cancelar_reserva():
    reserva = sistema.reservas[0]
    reserva.cancelar()
    return f"Reserva {reserva.identificador} cancelada. Estado actual: {reserva.estado}"
ejecutar_prueba(13, "Cancelar reserva", cancelar_reserva)

# 14. Mostrar listado de clientes y servicios para verificar los datos.
ejecutar_prueba(14, "Mostrar clientes registrados", lambda: sistema.listar(sistema.clientes))
ejecutar_prueba(15, "Mostrar servicios registrados", lambda: sistema.listar(sistema.servicios))

print("\nPrograma terminado. Revise logs/software_fj.log para el registro de eventos y errores.")

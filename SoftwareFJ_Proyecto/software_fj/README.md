# Software FJ - Gestión de clientes, servicios y reservas

Proyecto de consola en Python para practicar programación orientada a objetos. No usa bases de datos; trabaja con listas en memoria y guarda los eventos y errores en un archivo de log.


## Requisitos
- Python 3.9 o superior (no requiere instalar paquetes adicionales).

## Cómo ejecutar
1. Descargar o clonar el repositorio.
2. Abrir la carpeta del proyecto en Visual Studio Code.
3. Abrir una terminal en la carpeta principal `software_fj`.
4. Ejecutar:

```bash
python src/main.py
```

En Windows también puede funcionar con:

```bash
py src/main.py
```

El archivo de registro se crea en `logs/software_fj.log`.

## Organización
- `src/entidad.py`: clase abstracta base.
- `src/cliente.py`: clientes y validación de datos.
- `src/servicio.py`: clase abstracta Servicio y tres servicios derivados.
- `src/reserva.py`: creación, confirmación, procesamiento y cancelación.
- `src/excepciones.py`: errores personalizados.
- `src/sistema.py`: listas y operaciones principales.
- `src/main.py`: demostración de operaciones válidas e inválidas.
- `logs/`: registro de eventos y errores.


## Nota sobre la sobrecarga
Python no permite la sobrecarga tradicional de métodos como otros lenguajes, por eso el método `calcular_costo` permite diferentes usos mediante parámetros opcionales: duración, impuesto y descuento.

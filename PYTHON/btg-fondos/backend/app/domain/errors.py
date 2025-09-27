"""
Módulo de errores del dominio de la aplicación de gestión de fondos.

Author: Aura Cristina Garzón Rodríguez
Version: 1.0
Since: 2025-09-27 04:47 GMT-5, Bogotá D.C., Colombia
"""

from datetime import datetime
import pytz

class DomainError(Exception):
    """
    Clase base para errores del dominio de la aplicación.

    Esta clase se utiliza como superclase para todos los errores relacionados
    con la lógica de negocio de la aplicación de gestión de fondos.

    Author: Aura Cristina Garzón Rodríguez
    Version: 1.0
    Since: 2025-09-27 04:47 GMT-5, Bogotá D.C., Colombia
    """

class ClienteNoEncontrado(DomainError):
    """
    Error lanzado cuando no se encuentra un cliente en la base de datos.

    Hereda de DomainError para representar errores específicos del dominio
    relacionados con clientes.

    Author: Aura Cristina Garzón Rodríguez
    Version: 1.0
    Since: 2025-09-27 04:47 GMT-5, Bogotá D.C., Colombia
    """

class FondoNoEncontrado(DomainError):
    """
    Error lanzado cuando no se encuentra un fondo en la base de datos.

    Hereda de DomainError para representar errores específicos del dominio
    relacionados con fondos.

    Author: Aura Cristina Garzón Rodríguez
    Version: 1.0
    Since: 2025-09-27 04:47 GMT-5, Bogotá D.C., Colombia
    """

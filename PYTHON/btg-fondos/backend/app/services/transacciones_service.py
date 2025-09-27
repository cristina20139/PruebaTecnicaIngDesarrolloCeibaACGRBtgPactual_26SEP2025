"""
Servicio de transacciones de clientes en fondos.

Este módulo coordina la lógica de negocio para registrar y consultar
transacciones de apertura y cancelación de fondos.

Author: Aura Cristina Garzón Rodríguez
Version: 1.0
Since: 2025-09-27, Bogotá D.C., Colombia
"""

from app.domain.entities import Transaccion
from app.domain.errors import ClienteNoEncontrado, FondoNoEncontrado

class TransaccionService:
    """
    Servicio para manejar transacciones de clientes.
    
    Métodos:
        registrar_transaccion(cliente_id, fondo_id, tipo, monto): Crea una nueva transacción.
        listar_transacciones_por_cliente(cliente_id): Devuelve todas las transacciones de un cliente.
    """

    def __init__(self, repo_clientes, repo_fondos, repo_transacciones):
        """
        Inicializa el servicio con los repositorios necesarios.

        Args:
            repo_clientes: Repositorio de clientes.
            repo_fondos: Repositorio de fondos.
            repo_transacciones: Repositorio de transacciones.
        """
        self.repo_clientes = repo_clientes
        self.repo_fondos = repo_fondos
        self.repo_transacciones = repo_transacciones

    def registrar_transaccion(self, cliente_id: int, fondo_id: int, tipo: str, monto: float):
        """
        Registra una transacción de apertura o cancelación.

        Args:
            cliente_id (int): ID del cliente.
            fondo_id (int): ID del fondo.
            tipo (str): 'apertura' o 'cancelacion'.
            monto (float): Monto de la transacción.

        Raises:
            ClienteNoEncontrado: Si el cliente no existe.
            FondoNoEncontrado: Si el fondo no existe.

        Returns:
            Transaccion: Objeto transacción creado.
        """
        # Verificar existencia del cliente
        cliente = self.repo_clientes.obtener_cliente_por_id(cliente_id)
        if not cliente:
            raise ClienteNoEncontrado(f"Cliente {cliente_id} no encontrado")

        # Verificar existencia del fondo
        fondos = self.repo_fondos.listar_fondos()
        if not any(f["id"] == fondo_id for f in fondos):
            raise FondoNoEncontrado(f"Fondo {fondo_id} no encontrado")

        # Crear la transacción
        transaccion = Transaccion(
            cliente_id=cliente_id,
            fondo_id=fondo_id,
            tipo=tipo,
            monto=monto
        )

        # Guardar en el repositorio
        self.repo_transacciones.crear(transaccion)

        return transaccion

    def listar_transacciones_por_cliente(self, cliente_id: int):
        """
        Lista todas las transacciones realizadas por un cliente.

        Args:
            cliente_id (int): ID del cliente.

        Returns:
            List[Transaccion]: Lista de transacciones del cliente.
        """
        return self.repo_transacciones.listar_por_cliente(cliente_id)

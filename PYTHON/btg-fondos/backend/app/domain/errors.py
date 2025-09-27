class DomainError(Exception):
    """Error genérico del dominio."""

class ClienteNoEncontrado(DomainError):
    pass

class FondoNoEncontrado(DomainError):
    pass

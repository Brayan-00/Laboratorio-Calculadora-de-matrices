"""Registro de operaciones concretas."""
from .base import Operacion
from .determinante import Determinante
from .inversa import Inversa
from .multiplicacion import Multiplicacion
from .suma import Suma

__all__ = ["Operacion", "Suma", "Multiplicacion", "Determinante", "Inversa"]

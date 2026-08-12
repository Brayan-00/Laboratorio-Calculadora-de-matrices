"""Clase Aplicación: despacha operaciones desde un diccionario (R7)."""
from __future__ import annotations

from typing import Any

import numpy as np

from .operations import Determinante, Inversa, Multiplicacion, Operacion, Suma


class Aplicacion:
    """Núcleo del procesador. Contiene el registro de operaciones."""

    def __init__(self) -> None:
        """Registra las operaciones soportadas (R7)."""
        self._operations: dict[str, Operacion] = {
            "add": Suma(),
            "mul": Multiplicacion(),
            "det": Determinante(),
            "inv": Inversa(),
        }

    @property
    def supported(self) -> list[str]:
        """Lista de operaciones registradas."""
        return list(self._operations)

    def run(self, name: str, matrix_a: np.ndarray, matrix_b: np.ndarray) -> Any:
        """Ejecuta la operación indicada sobre A y B.

        Args:
            name: identificador de la operación (add, mul, det, inv).
            matrix_a: primera matriz.
            matrix_b: segunda matriz.

        Returns:
            Resultado de la operación (np.ndarray, dict o escalar).

        Raises:
            KeyError: si la operación no está registrada.

        """
        if name not in self._operations:
            raise KeyError(
                f"Operación '{name}' no soportada. Disponibles: {self.supported}"
            )
        op = self._operations[name]
        op.Clear()
        op.SetMatrix(0, matrix_a)
        op.SetMatrix(1, matrix_b)
        return op.Compute()

"""Interfaz padre para todas las operaciones matriciales."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

import numpy as np


class Operacion(ABC):
    """Contrato que toda operación matricial debe cumplir.

    Cada operación es un adaptador concreto que hereda de esta interfaz.
    El patrón sigue la arquitectura Interfaz-Adaptador (R4).
    """

    def __init__(self) -> None:
        """Inicializa el almacén de matrices vacío."""
        self._matrices: dict[int, np.ndarray] = {}

    def SetMatrix(self, index: int, matrix: np.ndarray) -> None:  # noqa: N802
        """Carga una matriz en el slot indicado (0 o 1)."""
        if index not in (0, 1):
            raise ValueError(f"index debe ser 0 o 1, se recibió {index}")
        if not isinstance(matrix, np.ndarray):
            matrix = np.asarray(matrix, dtype=float)
        self._matrices[index] = matrix

    @abstractmethod
    def Compute(self) -> Any:  # noqa: N802
        """Ejecuta la operación sobre las matrices cargadas."""

    def Clear(self) -> None:  # noqa: N802
        """Descarta todas las matrices cargadas."""
        self._matrices.clear()

    def _require(self, *indices: int) -> tuple[np.ndarray, ...]:
        """Garantiza que los slots indicados estén cargados."""
        missing = [i for i in indices if i not in self._matrices]
        if missing:
            raise RuntimeError(f"Faltan matrices en los slots: {missing}")
        return tuple(self._matrices[i] for i in indices)

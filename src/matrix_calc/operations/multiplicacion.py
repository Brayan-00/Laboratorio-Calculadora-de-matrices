"""Adaptador de la operación Multiplicación."""
import numpy as np

from .base import Operacion


class Multiplicacion(Operacion):
    """Multiplicación matricial A · B."""

    def Compute(self) -> np.ndarray:  # noqa: N802
        """Retorna A @ B.

        Raises:
            RuntimeError: si alguna matriz no fue cargada.
            ValueError: si A.cols != B.rows.

        """
        a, b = self._require(0, 1)
        if a.shape[1] != b.shape[0]:
            raise ValueError(
                f"Dimensiones incompatibles para multiplicación: {a.shape} · {b.shape}"
            )
        return a @ b

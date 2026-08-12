"""Adaptador de la operación Suma."""
import numpy as np

from .base import Operacion


class Suma(Operacion):
    """Suma elemento a elemento de dos matrices de igual dimensión."""

    def Compute(self) -> np.ndarray:  # noqa: N802
        """Retorna A + B.

        Raises:
            RuntimeError: si alguna matriz no fue cargada.
            ValueError: si las dimensiones no coinciden.

        """
        a, b = self._require(0, 1)
        if a.shape != b.shape:
            raise ValueError(f"Dimensiones incompatibles para suma: {a.shape} vs {b.shape}")
        return a + b

"""Adaptador de la operación Determinante (aplicada a ambas matrices)."""
import numpy as np

from .base import Operacion


class Determinante(Operacion):
    """Determinante de A y de B. R3 pide 'determinante de dos matrices'."""

    def Compute(self) -> dict[str, float]:  # noqa: N802
        """Retorna {'matrixA': det(A), 'matrixB': det(B)}.

        Raises:
            RuntimeError: si alguna matriz no fue cargada.
            ValueError: si alguna matriz no es cuadrada.

        """
        a, b = self._require(0, 1)
        for name, m in (("matrixA", a), ("matrixB", b)):
            if m.shape[0] != m.shape[1]:
                raise ValueError(f"{name} no es cuadrada: {m.shape}")
        return {"matrixA": float(np.linalg.det(a)), "matrixB": float(np.linalg.det(b))}

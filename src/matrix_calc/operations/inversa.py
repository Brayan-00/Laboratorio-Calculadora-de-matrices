"""Adaptador de la operación Inversa (aplicada a ambas matrices)."""
import numpy as np

from .base import Operacion


class Inversa(Operacion):
    """Inversa de A y de B. R3 pide 'inversa de dos matrices'."""

    def Compute(self) -> dict[str, np.ndarray]:  # noqa: N802
        """Retorna {'matrixA': A^-1, 'matrixB': B^-1}.

        Raises:
            RuntimeError: si alguna matriz no fue cargada.
            ValueError: si alguna matriz no es cuadrada o es singular.

        """
        a, b = self._require(0, 1)
        for name, m in (("matrixA", a), ("matrixB", b)):
            if m.shape[0] != m.shape[1]:
                raise ValueError(f"{name} no es cuadrada: {m.shape}")
        try:
            inv_a = np.linalg.inv(a)
            inv_b = np.linalg.inv(b)
        except np.linalg.LinAlgError as exc:
            raise ValueError(f"Matriz singular, no invertible: {exc}") from exc
        return {"matrixA": inv_a, "matrixB": inv_b}

"""Pruebas de la operación Multiplicación."""
import numpy as np
import pytest

from matrix_calc.application import Aplicacion
from matrix_calc.operations import Multiplicacion


def test_multiplicacion_basica() -> None:
    a = np.array([[1.0, 2.0], [3.0, 4.0]])
    b = np.array([[5.0, 6.0], [7.0, 8.0]])
    result = Aplicacion().run("mul", a, b)
    np.testing.assert_allclose(result, [[19.0, 22.0], [43.0, 50.0]])


def test_multiplicacion_dimensiones_incompatibles() -> None:
    op = Multiplicacion()
    op.SetMatrix(0, np.zeros((2, 3)))
    op.SetMatrix(1, np.zeros((2, 2)))
    with pytest.raises(ValueError, match="Dimensiones incompatibles"):
        op.Compute()


def test_clear_borra_estado() -> None:
    op = Multiplicacion()
    op.SetMatrix(0, np.zeros((2, 2)))
    op.Clear()
    with pytest.raises(RuntimeError, match="Faltan matrices"):
        op.Compute()

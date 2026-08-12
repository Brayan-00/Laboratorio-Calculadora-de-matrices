"""Pruebas de la operación Suma."""
import numpy as np
import pytest

from matrix_calc.application import Aplicacion
from matrix_calc.operations import Suma


def test_suma_basica() -> None:
    a = np.array([[1.0, 2.0], [3.0, 4.0]])
    b = np.array([[5.0, 6.0], [7.0, 8.0]])
    result = Aplicacion().run("add", a, b)
    np.testing.assert_allclose(result, [[6.0, 8.0], [10.0, 12.0]])


def test_suma_dimensiones_incompatibles() -> None:
    op = Suma()
    op.SetMatrix(0, np.zeros((2, 2)))
    op.SetMatrix(1, np.zeros((2, 3)))
    with pytest.raises(ValueError, match="Dimensiones incompatibles"):
        op.Compute()


def test_clear_borra_estado() -> None:
    op = Suma()
    op.SetMatrix(0, np.zeros((2, 2)))
    op.Clear()
    with pytest.raises(RuntimeError, match="Faltan matrices"):
        op.Compute()

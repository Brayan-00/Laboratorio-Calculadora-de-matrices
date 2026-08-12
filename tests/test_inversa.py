"""Pruebas de la operación Inversa."""
import numpy as np
import pytest

from matrix_calc.application import Aplicacion
from matrix_calc.operations import Inversa


def test_inversa_basica() -> None:
    a = np.array([[4.0, 7.0], [2.0, 6.0]])
    b = np.eye(2)
    result = Aplicacion().run("inv", a, b)
    np.testing.assert_allclose(result["matrixA"] @ a, np.eye(2), atol=1e-8)
    np.testing.assert_allclose(result["matrixB"], np.eye(2))


def test_inversa_matriz_singular() -> None:
    op = Inversa()
    op.SetMatrix(0, np.array([[1.0, 2.0], [2.0, 4.0]]))
    op.SetMatrix(1, np.eye(2))
    with pytest.raises(ValueError, match="singular"):
        op.Compute()


def test_inversa_matriz_no_cuadrada() -> None:
    op = Inversa()
    op.SetMatrix(0, np.zeros((2, 3)))
    op.SetMatrix(1, np.eye(2))
    with pytest.raises(ValueError, match="no es cuadrada"):
        op.Compute()


def test_clear_borra_estado() -> None:
    op = Inversa()
    op.SetMatrix(0, np.eye(2))
    op.Clear()
    with pytest.raises(RuntimeError, match="Faltan matrices"):
        op.Compute()

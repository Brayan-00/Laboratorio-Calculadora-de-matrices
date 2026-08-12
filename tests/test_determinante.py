"""Pruebas de la operación Determinante."""
import numpy as np
import pytest

from matrix_calc.application import Aplicacion
from matrix_calc.operations import Determinante


def test_determinante_basica() -> None:
    a = np.array([[1.0, 2.0], [3.0, 4.0]])
    b = np.array([[2.0, 0.0], [0.0, 2.0]])
    result = Aplicacion().run("det", a, b)
    assert result["matrixA"] == pytest.approx(-2.0)
    assert result["matrixB"] == pytest.approx(4.0)


def test_determinante_matriz_no_cuadrada() -> None:
    op = Determinante()
    op.SetMatrix(0, np.zeros((2, 3)))
    op.SetMatrix(1, np.zeros((2, 2)))
    with pytest.raises(ValueError, match="no es cuadrada"):
        op.Compute()


def test_clear_borra_estado() -> None:
    op = Determinante()
    op.SetMatrix(0, np.eye(2))
    op.Clear()
    with pytest.raises(RuntimeError, match="Faltan matrices"):
        op.Compute()

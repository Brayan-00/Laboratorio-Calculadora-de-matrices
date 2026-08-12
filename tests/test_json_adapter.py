"""Pruebas del JSONAdapter."""
import json

import numpy as np
import pytest

from matrix_calc.json_adapter import JSONAdapter


def _write(tmp_path, payload) -> str:
    path = tmp_path / "matrices.json"
    path.write_text(json.dumps(payload), encoding="utf-8")
    return str(path)


def test_carga_matrices_validas(tmp_path) -> None:
    payload = {
        "matrixA": {"rows": 2, "cols": 2, "data": [[1.0, 2.0], [3.0, 4.0]]},
        "matrixB": {"rows": 2, "cols": 1, "data": [[5.0], [6.0]]},
    }
    result = JSONAdapter().load(_write(tmp_path, payload))
    np.testing.assert_allclose(result["matrixA"], [[1.0, 2.0], [3.0, 4.0]])
    np.testing.assert_allclose(result["matrixB"], [[5.0], [6.0]])


def test_falta_matrixb(tmp_path) -> None:
    payload = {"matrixA": {"rows": 1, "cols": 1, "data": [[1.0]]}}
    with pytest.raises(ValueError, match="matrixB"):
        JSONAdapter().load(_write(tmp_path, payload))


def test_dimensiones_no_coinciden_con_data(tmp_path) -> None:
    payload = {
        "matrixA": {"rows": 3, "cols": 3, "data": [[1.0, 2.0], [3.0, 4.0]]},
        "matrixB": {"rows": 2, "cols": 2, "data": [[1.0, 0.0], [0.0, 1.0]]},
    }
    with pytest.raises(ValueError, match="no coinciden"):
        JSONAdapter().load(_write(tmp_path, payload))

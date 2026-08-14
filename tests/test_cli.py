"""Pruebas para la interfaz CLI de la calculadora."""

import json

import pytest
from typer.testing import CliRunner

from matrix_calc.cli import app

runner = CliRunner()


def test_ops_lists_supported_operations() -> None:
    """Verifica que la CLI muestre todas las operaciones disponibles."""
    result = runner.invoke(app, ["ops"])

    assert result.exit_code == 0
    assert "add" in result.output
    assert "mul" in result.output
    assert "det" in result.output
    assert "inv" in result.output


def test_run_add_from_json(tmp_path) -> None:
    """Verifica una suma completa ingresando las matrices mediante JSON."""
    payload = {
        "matrixA": {
            "rows": 2,
            "cols": 2,
            "data": [[1.0, 2.0], [3.0, 4.0]],
        },
        "matrixB": {
            "rows": 2,
            "cols": 2,
            "data": [[5.0, 6.0], [7.0, 8.0]],
        },
    }

    input_file = tmp_path / "matrices.json"
    input_file.write_text(json.dumps(payload), encoding="utf-8")

    result = runner.invoke(
        app,
        ["run", "add", "--input", str(input_file)],
    )

    assert result.exit_code == 0

    output = json.loads(result.output)

    assert output["operation"] == "add"
    assert output["result"]["rows"] == 2
    assert output["result"]["cols"] == 2
    assert output["result"]["data"] == [
        [6.0, 8.0],
        [10.0, 12.0],
    ]


def test_run_mul_from_json(tmp_path) -> None:
    """Verifica una multiplicación completa ingresando las matrices mediante JSON."""
    payload = {
        "matrixA": {
            "rows": 2,
            "cols": 2,
            "data": [[1.0, 2.0], [3.0, 4.0]],
        },
        "matrixB": {
            "rows": 2,
            "cols": 2,
            "data": [[5.0, 6.0], [7.0, 8.0]],
        },
    }

    input_file = tmp_path / "matrices.json"
    input_file.write_text(json.dumps(payload), encoding="utf-8")

    result = runner.invoke(
        app,
        ["run", "mul", "--input", str(input_file)],
    )

    assert result.exit_code == 0

    output = json.loads(result.output)

    assert output["operation"] == "mul"
    assert output["result"]["rows"] == 2
    assert output["result"]["cols"] == 2
    assert output["result"]["data"] == [
        [19.0, 22.0],
        [43.0, 50.0],
    ]


def test_run_det_from_json(tmp_path) -> None:
    """Verifica un determinante completo ingresando las matrices mediante JSON."""
    payload = {
        "matrixA": {
            "rows": 2,
            "cols": 2,
            "data": [[1.0, 2.0], [3.0, 4.0]],
        },
        "matrixB": {
            "rows": 2,
            "cols": 2,
            "data": [[5.0, 6.0], [7.0, 8.0]],
        },
    }

    input_file = tmp_path / "matrices.json"
    input_file.write_text(json.dumps(payload), encoding="utf-8")

    result = runner.invoke(
        app,
        ["run", "det", "--input", str(input_file)],
    )

    assert result.exit_code == 0

    output = json.loads(result.output)

    assert output["operation"] == "det"
    assert output["result"]["matrixA"] == pytest.approx(-2.0)
    assert output["result"]["matrixB"] == pytest.approx(-2.0)


def test_run_inv_from_json(tmp_path) -> None:
    """Verifica una inversa completa ingresando las matrices mediante JSON."""
    payload = {
        "matrixA": {
            "rows": 2,
            "cols": 2,
            "data": [[1.0, 2.0], [3.0, 4.0]],
        },
        "matrixB": {
            "rows": 2,
            "cols": 2,
            "data": [[5.0, 6.0], [7.0, 8.0]],
        },
    }

    input_file = tmp_path / "matrices.json"
    input_file.write_text(json.dumps(payload), encoding="utf-8")

    result = runner.invoke(
        app,
        ["run", "inv", "--input", str(input_file)],
    )

    assert result.exit_code == 0

    output = json.loads(result.output)

    assert output["operation"] == "inv"

    expected_a = [
        [-2.0, 1.0],
        [1.5, -0.5],
    ]

    expected_b = [
        [-4.0, 3.0],
        [3.5, -2.5],
    ]

    for actual_row, expected_row in zip(
        output["result"]["matrixA"]["data"], expected_a
    ):
        assert actual_row == pytest.approx(expected_row)

    for actual_row, expected_row in zip(
        output["result"]["matrixB"]["data"], expected_b
    ):
        assert actual_row == pytest.approx(expected_row)

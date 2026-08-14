"""Pruebas para la interfaz CLI de la calculadora."""

import json

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

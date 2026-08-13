"""Pruebas para la interfaz CLI de la calculadora."""

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

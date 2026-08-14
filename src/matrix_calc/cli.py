"""Interfaz CLI con Typer (R6)."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np
import typer

from .application import Aplicacion
from .json_adapter import JSONAdapter

app = typer.Typer(help="Calculadora de matrices — EL5859")


def _serialize(result: Any) -> Any:
    """Convierte el resultado a estructura JSON-serializable."""
    if isinstance(result, np.ndarray):
        return {
            "rows": result.shape[0],
            "cols": result.shape[1],
            "data": result.tolist(),
        }
    if isinstance(result, dict):
        return {k: _serialize(v) for k, v in result.items()}
    return result  # escalar


@app.command()
def run(
    operation: str = typer.Argument(..., help="add | mul | det | inv"),
    input_path: Path = typer.Option(..., "--input", "-i", exists=True, readable=True),
    output_path: Path | None = typer.Option(None, "--output", "-o"),
) -> None:
    """Ejecuta una operación sobre las matrices del archivo JSON."""
    adapter = JSONAdapter()
    matrices = adapter.load(input_path)

    application = Aplicacion()
    result = application.run(operation, matrices["matrixA"], matrices["matrixB"])

    payload = {"operation": operation, "result": _serialize(result)}
    dumped = json.dumps(payload, indent=2)

    if output_path:
        output_path.write_text(dumped, encoding="utf-8")
        typer.echo(f"Resultado escrito en {output_path}")
    else:
        typer.echo(dumped)


@app.command()
def ops() -> None:
    """Lista las operaciones soportadas."""
    for name in Aplicacion().supported:
        typer.echo(name)


if __name__ == "__main__":
    app()

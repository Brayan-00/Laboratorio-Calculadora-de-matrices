"""Adaptador de entrada JSON → matrices numpy (R1, R2)."""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np


class JSONAdapter:
    """Lee un JSON con matrixA/matrixB y las entrega como np.ndarray."""

    REQUIRED_KEYS = ("rows", "cols", "data")

    def load(self, path: str | Path) -> dict[str, np.ndarray]:
        """Carga y valida el archivo JSON de entrada.

        Args:
            path: ruta al archivo JSON.

        Returns:
            Diccionario con claves 'matrixA' y 'matrixB' como np.ndarray.

        Raises:
            ValueError: si el JSON no cumple el esquema esperado.

        """
        raw = json.loads(Path(path).read_text(encoding="utf-8"))
        return {
            "matrixA": self._parse(raw, "matrixA"),
            "matrixB": self._parse(raw, "matrixB"),
        }

    def _parse(self, raw: dict, key: str) -> np.ndarray:
        if key not in raw:
            raise ValueError(f"Falta '{key}' en el JSON")
        node = raw[key]
        for k in self.REQUIRED_KEYS:
            if k not in node:
                raise ValueError(f"'{key}' no tiene '{k}'")
        arr = np.asarray(node["data"], dtype=float)
        expected = (node["rows"], node["cols"])
        if arr.shape != expected:
            raise ValueError(
                f"'{key}': dimensiones declaradas {expected} "
                f"no coinciden con data {arr.shape}"
            )
        return arr

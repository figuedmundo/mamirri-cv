#!/usr/bin/env python3
"""Genera un CV HTML autónomo a partir del Markdown, sin dependencias externas."""

import argparse
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent
DEFAULT_SOURCE = ROOT / "HOJA DE VIDA NOEMI v2.md"
DATA_MARKER = "__CV_DATA_JSON__"


def cv_content(markdown: str) -> str:
    """Excluye las notas editoriales, sin modificar el archivo original."""
    content = re.split(
        r"^#\s+Notas de revisión y recomendaciones\s*$",
        markdown,
        maxsplit=1,
        flags=re.MULTILINE,
    )[0]
    content = re.sub(r"\n\s*---\s*$", "", content).strip()
    if not re.match(r"#\s+\S", content):
        raise ValueError("El Markdown debe comenzar con '# Nombre completo'.")
    return content


def build_html(source: Path, template: Path) -> str:
    data = {
        "markdown": cv_content(source.read_text(encoding="utf-8")),
        "source": source.name,
    }
    # Impide cerrar el elemento <script> desde el contenido del Markdown.
    payload = json.dumps(data, ensure_ascii=False).replace("<", "\\u003c")
    document = template.read_text(encoding="utf-8")
    if document.count(DATA_MARKER) != 1:
        raise ValueError("La plantilla debe contener exactamente un marcador de datos.")
    return document.replace(DATA_MARKER, payload)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path, default=ROOT / "index.html")
    args = parser.parse_args()
    document = build_html(args.source, ROOT / "cv-template.html")
    args.output.write_text(document, encoding="utf-8")
    print(f"CV generado: {args.output.resolve()}")


if __name__ == "__main__":
    main()

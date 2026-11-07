import json
from pathlib import Path
import tempfile
import unittest

from generar_cv import build_html, cv_content


class GeneratorTests(unittest.TestCase):
    def test_excludes_editorial_notes_and_separator(self):
        source = "# Nombre\n\n## Idiomas\n- Español\n\n---\n\n# Notas de revisión y recomendaciones\nPrivado"
        self.assertEqual(cv_content(source), "# Nombre\n\n## Idiomas\n- Español")

    def test_preserves_markdown_links_and_placeholders(self):
        source = "# Nombre\n\n[Correo](mailto:a@example.com)\n\n## Trabajo\n[Año]"
        self.assertEqual(cv_content(source), source)

    def test_rejects_missing_name(self):
        with self.assertRaises(ValueError):
            cv_content("## Sin nombre")

    def test_embedded_json_cannot_close_script(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "cv.md"
            template = root / "template.html"
            source.write_text("# Nombre\n\n## Perfil\n</script><script>alert(1)</script>", encoding="utf-8")
            template.write_text("<script type='application/json'>__CV_DATA_JSON__</script>", encoding="utf-8")
            result = build_html(source, template)
            payload = result.split(">", 1)[1].rsplit("</script>", 1)[0]
            self.assertNotIn("<", payload)
            self.assertIn("</script>", json.loads(payload)["markdown"])

    def test_requires_exactly_one_template_marker(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "cv.md"
            template = root / "template.html"
            source.write_text("# Nombre", encoding="utf-8")
            template.write_text("no marker", encoding="utf-8")
            with self.assertRaises(ValueError):
                build_html(source, template)


if __name__ == "__main__":
    unittest.main()

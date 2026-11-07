# CV de Noemi Herbas Tudor

## Abrir y exportar

1. Abre `index.html` con Chrome, Edge, Safari o Firefox. Funciona sin internet y sin instalar nada.
2. Completa los campos resaltados antes de enviar el CV.
3. Pulsa **Imprimir / Guardar PDF** y selecciona:
   - Destino: **Guardar como PDF**.
   - Papel: **A4**.
   - Escala: **100 %**.
   - Encabezados y pies de página del navegador: **desactivados**.
   - Gráficos de fondo: activados si quieres conservar los colores de los campos pendientes.
4. Revisa la vista previa: el diseño inicial está preparado para dos páginas. Si agregas mucho contenido, comprueba los saltos y reduce o resume el texto antes de enviarlo.

Mientras existan campos `[por completar]`, la presentación y el PDF indican **Borrador**. Cuando se completen o eliminen, esa indicación desaparece. Revisa también los datos, aunque ya no haya campos pendientes.

`Noemi_Herbas_Tudor_CV_BORRADOR.pdf` es una primera exportación de dos páginas para revisar el diseño. No se actualiza automáticamente: vuelve a exportar después de cambiar el contenido.

## Editar sin herramientas de desarrollo

En `index.html`, pulsa **Editar contenido**:

- Edita el texto en Markdown y pulsa **Aplicar cambios**.
- También puedes usar **Cargar Markdown** para abrir `HOJA DE VIDA NOEMI v2.md` actualizado.
- **Descargar Markdown** guarda tus cambios en un archivo nuevo. El navegador no modifica automáticamente el archivo original.
- Una vez aplicado el contenido, puedes exportar el PDF directamente.

Los cambios del editor viven solo en esa pestaña: descarga el Markdown antes de cerrarla. Si cargas el Markdown completo, se conservan sus notas editoriales al descargarlo, pero nunca se muestran en el CV.

## Mantener el Markdown como fuente principal

Edita `HOJA DE VIDA NOEMI v2.md` y regenera el HTML:

```sh
python3 generar_cv.py
```

El comando funciona desde cualquier carpeta si usas la ruta del script. No requiere librerías adicionales. También admite `--source archivo.md` y `--output archivo.html`.

- `HOJA DE VIDA NOEMI v2.md`: contenido y recomendaciones de edición.
- `cv-template.html`: diseño, editor y estilos de impresión.
- `generar_cv.py`: integra el contenido en la plantilla.
- `index.html`: presentación autónoma generada; este es el archivo que debes abrir.

La plantilla no se abre directamente: necesita los datos que incorpora el generador. El contenido que aparece después de `# Notas de revisión y recomendaciones` se excluye de la presentación generada.

El formato admite títulos `#`, `##`, `###`, listas con `-`, negritas, enlaces y campos pendientes `[entre corchetes]`. Mantén cada párrafo en una sola línea de Markdown. La segunda página comienza en `## Formación académica`.

## Privacidad y presentación

- Sin fuentes remotas, analítica ni conexiones a servicios externos.
- Texto real, seleccionable y en orden de lectura de una sola columna; no es una imagen.
- El PDF es el formato recomendado para enviar a empleadores. Si una convocatoria pide DOCX u otro formato, sigue sus instrucciones.
- No envíes el borrador ni las notas editoriales. Comparte datos de pacientes o referencias únicamente con la autorización correspondiente.

## Pruebas del generador

```sh
python3 -m unittest discover -s tests
```

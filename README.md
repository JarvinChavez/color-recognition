# Color Recognition (Research Figures)

Separate from [protein-motif-encoding](https://github.com/JarvinChavez/protein-motif-encoding) — this repo is about **visual analysis of research figures**: extracting dominant colors, overlaying coordinate grids, and selecting normalized bounding-box regions.

Built during NSF undergraduate research at the University of St. Thomas.

---

## What it does

| Script | Purpose |
|--------|---------|
| `color_palette.py` | Build a palette image from dominant RGB colors in a figure |
| `grid_overlay.py` | Draw 10px / 100px coordinate grids on PNG images |
| `select_grid.py` | Interactive OpenCV selector — click/drag a region, export normalized JSON coordinates |

---

## Run

```bash
pip install -r requirements.txt
python src/color_palette.py
python src/grid_overlay.py
python src/select_grid.py
```

---

## Samples

`samples/` includes example research figures and grid output used during development.

---

## Stack

Python · OpenCV · Pillow

---

## Author

**Jarvin Chavez** · [GitHub](https://github.com/JarvinChavez)

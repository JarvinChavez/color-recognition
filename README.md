# Color Recognition (Research Figures)

Separate from [protein-motif-encoding](https://github.com/JarvinChavez/protein-motif-encoding) — this repo is about **visual analysis of research figures**: extracting dominant colors, overlaying coordinate grids, and selecting normalized bounding-box regions.

Built during NSF undergraduate research at the University of St. Thomas.

Cursor assisted in refining the design criteria and workflow for this project.

---

## What it does

1. Overlay a coordinate grid on a research figure PNG.
2. Sample the mean RGB color inside each grid cell.
3. Export a JSON lookup table mapping grid coordinates to RGB values.

| Script | Purpose |
|--------|---------|
| `main.py` | Full pipeline — grid overlay + JSON color map |
| `grid_color_map.py` | Sample mean RGB per grid cell and write JSON |
| `grid_overlay.py` | Draw 10px / 100px coordinate grids on PNG images |
| `select_grid.py` | Interactive OpenCV selector — click/drag a region, export normalized JSON coordinates |
| `color_palette.py` | Build a palette image from dominant RGB colors in a figure |

---

## Run

```bash
pip install -r requirements.txt

# Full pipeline (writes example_grid.png + example_grid_colors.json)
python src/main.py samples/example.png

# JSON only
python src/grid_color_map.py

# Individual tools
python src/grid_overlay.py
python src/select_grid.py
python src/color_palette.py
```

### JSON output

Each cell entry includes grid indices, pixel origin, and RGB:

```json
{
  "grid_x": 3,
  "grid_y": 7,
  "pixel_x": 30,
  "pixel_y": 70,
  "width": 10,
  "height": 10,
  "rgb": [183, 156, 127]
}
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

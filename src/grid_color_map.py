"""Sample mean RGB for each grid cell and export a coordinate lookup JSON."""

from __future__ import annotations

import json
from pathlib import Path

import cv2


def build_grid_color_map(
    image_path: str | Path,
    grid_size: int = 10,
) -> dict:
    """Return metadata and per-cell RGB samples for a gridded image."""
    image_path = Path(image_path)
    image = cv2.imread(str(image_path))
    if image is None:
        raise FileNotFoundError(f"Could not load image: {image_path}")

    height, width = image.shape[:2]
    cells: list[dict] = []

    for grid_y, pixel_y in enumerate(range(0, height, grid_size)):
        for grid_x, pixel_x in enumerate(range(0, width, grid_size)):
            x_end = min(pixel_x + grid_size, width)
            y_end = min(pixel_y + grid_size, height)
            region = image[pixel_y:y_end, pixel_x:x_end]
            mean_bgr = region.mean(axis=(0, 1))
            rgb = [int(round(mean_bgr[2])), int(round(mean_bgr[1])), int(round(mean_bgr[0]))]

            cells.append(
                {
                    "grid_x": grid_x,
                    "grid_y": grid_y,
                    "pixel_x": pixel_x,
                    "pixel_y": pixel_y,
                    "width": x_end - pixel_x,
                    "height": y_end - pixel_y,
                    "rgb": rgb,
                }
            )

    return {
        "source_image": image_path.name,
        "grid_size": grid_size,
        "image_width": width,
        "image_height": height,
        "grid_columns": (width + grid_size - 1) // grid_size,
        "grid_rows": (height + grid_size - 1) // grid_size,
        "cell_count": len(cells),
        "cells": cells,
    }


def export_grid_color_map(
    image_path: str | Path,
    output_path: str | Path,
    grid_size: int = 10,
) -> Path:
    """Build the grid color map and write it to JSON."""
    output_path = Path(output_path)
    data = build_grid_color_map(image_path, grid_size=grid_size)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(data, indent=2))
    return output_path


def lookup_rgb(color_map: dict, grid_x: int, grid_y: int) -> list[int] | None:
    """Return RGB for a grid cell index, or None if out of range."""
    for cell in color_map["cells"]:
        if cell["grid_x"] == grid_x and cell["grid_y"] == grid_y:
            return cell["rgb"]
    return None


if __name__ == "__main__":
    sample = Path(__file__).resolve().parent.parent / "samples" / "example.png"
    out = export_grid_color_map(sample, sample.with_name("example_grid_colors.json"))
    print(f"Wrote {out}")

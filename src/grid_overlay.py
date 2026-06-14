"""Overlay coordinate grids on research figure images."""

from __future__ import annotations

from pathlib import Path

import cv2


def overlay_grid(image_path: str | Path, small_grid: int = 10, large_grid: int = 100) -> str:
    image_path = str(image_path)
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Could not load image: {image_path}")

    height, width, _ = image.shape

    for x in range(0, width, small_grid):
        cv2.line(image, (x, 0), (x, height), (200, 200, 200), 1)
    for y in range(0, height, small_grid):
        cv2.line(image, (0, y), (width, y), (200, 200, 200), 1)
    for x in range(0, width, large_grid):
        cv2.line(image, (x, 0), (x, height), (0, 0, 0), 2)
    for y in range(0, height, large_grid):
        cv2.line(image, (0, y), (width, y), (0, 0, 0), 2)

    font = cv2.FONT_HERSHEY_SIMPLEX
    for x in range(0, width, large_grid):
        for y in range(0, height, large_grid):
            cv2.putText(image, f"({x},{y})", (x + 5, y + 15), font, 0.5, (0, 0, 255), 1)

    output_path = image_path.replace(".png", "_grid.png")
    cv2.imwrite(output_path, image)
    return output_path


if __name__ == "__main__":
    sample = Path(__file__).resolve().parent.parent / "samples" / "example.png"
    out = overlay_grid(sample)
    print(f"Wrote {out}")

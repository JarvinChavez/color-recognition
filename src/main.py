"""Run the full color-recognition pipeline: grid overlay + coordinate RGB map."""

from __future__ import annotations

import argparse
from pathlib import Path

from grid_color_map import export_grid_color_map
from grid_overlay import overlay_grid


def run_pipeline(
    image_path: str | Path,
    output_json: str | Path | None = None,
    grid_size: int = 10,
    large_grid: int = 100,
    skip_overlay: bool = False,
) -> tuple[Path, Path]:
    image_path = Path(image_path)
    if not image_path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")

    grid_image_path = image_path
    if not skip_overlay:
        grid_image_path = Path(overlay_grid(image_path, small_grid=grid_size, large_grid=large_grid))

    if output_json is None:
        output_json = image_path.with_name(f"{image_path.stem}_grid_colors.json")
    json_path = export_grid_color_map(image_path, output_json, grid_size=grid_size)
    return Path(grid_image_path), json_path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Overlay a grid on a figure and export per-cell RGB coordinates as JSON."
    )
    parser.add_argument("image", type=Path, help="Path to input PNG image")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Output JSON path (default: <image_stem>_grid_colors.json)",
    )
    parser.add_argument(
        "--grid-size",
        type=int,
        default=10,
        help="Grid cell size in pixels (default: 10)",
    )
    parser.add_argument(
        "--large-grid",
        type=int,
        default=100,
        help="Large grid line spacing in pixels (default: 100)",
    )
    parser.add_argument(
        "--skip-overlay",
        action="store_true",
        help="Only build the JSON map without writing a *_grid.png file",
    )
    args = parser.parse_args()

    grid_path, json_path = run_pipeline(
        args.image,
        output_json=args.output,
        grid_size=args.grid_size,
        large_grid=args.large_grid,
        skip_overlay=args.skip_overlay,
    )
    print(f"Grid image: {grid_path}")
    print(f"Color map:  {json_path}")


if __name__ == "__main__":
    main()

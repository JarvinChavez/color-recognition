"""Visualize dominant RGB colors extracted from motif visualization samples."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw

OUTPUT = Path(__file__).resolve().parent.parent / "samples" / "color_palette.png"

# Sample palette from research figure analysis
COLORS = {
    (91, 78, 63), (183, 156, 127), (151, 128, 105), (185, 157, 129),
    (202, 172, 140), (215, 183, 149), (219, 186, 152), (245, 208, 170),
    (253, 215, 176), (255, 255, 255), (0, 0, 0),
}


def create_color_palette(colors: set[tuple[int, int, int]], square_size: int = 20) -> Image.Image:
    color_list = list(colors)
    row_length = max(int(len(color_list) ** 0.5), 1)
    width = row_length * square_size
    height = ((len(color_list) - 1) // row_length + 1) * square_size
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)

    x = y = 0
    for color in color_list:
        draw.rectangle([x, y, x + square_size - 1, y + square_size - 1], fill=color)
        x += square_size
        if x >= width:
            x = 0
            y += square_size
    return img


def main() -> None:
    palette = create_color_palette(COLORS)
    palette.save(OUTPUT)
    print(f"Saved palette to {OUTPUT}")


if __name__ == "__main__":
    main()

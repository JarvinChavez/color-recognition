"""Interactive OpenCV grid selector — normalize bounding-box coordinates for downstream tools."""

from __future__ import annotations

import json
from pathlib import Path

import cv2

IMAGE_PATH = Path(__file__).resolve().parent.parent / "samples" / "example.png"
OUTPUT_PATH = Path(__file__).resolve().parent.parent / "samples" / "selection.json"

start_point = None
end_point = None
selected_coordinates: dict = {}
image_copy = None
image_width = 0
image_height = 0


def draw_rectangle(event, x, y, flags, param):
    global start_point, end_point, selected_coordinates, image_copy, image_width, image_height

    if event == cv2.EVENT_LBUTTONDOWN:
        start_point = (x, y)
    elif event == cv2.EVENT_MOUSEMOVE and start_point is not None:
        temp = image_copy.copy()
        cv2.rectangle(temp, start_point, (x, y), (0, 255, 0), 2)
        cv2.imshow("Select Area", temp)
    elif event == cv2.EVENT_LBUTTONUP:
        end_point = (x, y)
        x1, y1 = min(start_point[0], end_point[0]), min(start_point[1], end_point[1])
        x2, y2 = max(start_point[0], end_point[0]), max(start_point[1], end_point[1])
        cv2.rectangle(image_copy, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.imshow("Select Area", image_copy)

        q1 = {"x": x1 / image_width, "y": y1 / image_height}
        q2 = {"x": x2 / image_width, "y": y1 / image_height}
        q3 = {"x": x1 / image_width, "y": y2 / image_height}
        q4 = {"x": x2 / image_width, "y": y2 / image_height}
        centroid = {
            "x": (q1["x"] + q2["x"] + q3["x"] + q4["x"]) / 4,
            "y": (q1["y"] + q2["y"] + q3["y"] + q4["y"]) / 4,
        }
        selected_coordinates.update({"q1": q1, "q2": q2, "q3": q3, "q4": q4, "centroid": centroid})


def main() -> None:
    global image_copy, image_width, image_height

    image = cv2.imread(str(IMAGE_PATH))
    if image is None:
        raise FileNotFoundError(f"Could not load image: {IMAGE_PATH}")

    image_copy = image.copy()
    image_height, image_width = image.shape[:2]

    cv2.namedWindow("Select Area")
    cv2.setMouseCallback("Select Area", draw_rectangle)
    cv2.imshow("Select Area", image_copy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    OUTPUT_PATH.write_text(json.dumps(selected_coordinates, indent=2))
    print(f"Saved selection to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

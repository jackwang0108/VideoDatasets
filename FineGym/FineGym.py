# Standard Library
import json
from pathlib import Path

# Third-Party Library


def get_csv(split: str) -> list[str]:
    assert split in {"train", "val", "test"}, f"{split} not exists"

    fileName = f"{split}.json"
    with (Path(__file__).resolve().parent / fileName).open(mode="r") as f:
        json_info: list[dict[str, int | str | list | dict]] = json.load(f)

    def get_resolution(width: int, height: int) -> str:
        if width == 1280 and height == 720:
            return "1280x720"
        elif width == 1920 and height == 1080:
            return "1920x1080"

    lines = {}
    for unit in json_info:
        name = unit["video"].split("_")[0]
        fps = round(unit["fps"], ndigits=2)
        resolution = unit[""]


if __name__ == "__main__":
    get_csv("train")

# Standard Library
import json
from pathlib import Path
from typing import TypedDict

LABEL_DIR = Path(__file__).resolve().parent


class Event(TypedDict):
    frame: int
    label: str
    comment: str


class SourceInfo(TypedDict):
    end_frame: int
    start_frame: int
    pad: tuple[int, int]
    effective_pad: tuple[int, int]


class Annotation(TypedDict):
    fps: int
    height: int
    width: int
    video: str
    num_events: int
    num_frames: int
    events: list[Event]
    _source_info: SourceInfo


def load_json(file: Path) -> list[Annotation]:
    with file.open(mode="r") as f:
        return json.load(f)


def last_frame(events: list[Event]) -> int:
    return max(i["frame"] for i in events)


def fix_one(label: Annotation) -> Annotation:
    num_frames = label["num_frames"]
    start_frame = label["_source_info"]["start_frame"] - \
        label["_source_info"]['pad'][0]
    end_frame = label["_source_info"]["end_frame"] + \
        label["_source_info"]["pad"][1]

    if end_frame - start_frame != num_frames:
        if (l := last_frame(label["events"])) < num_frames:
            print(f"fixing {label['video']}, start_frame: {
                start_frame}, end_frame: {end_frame}, expected num_frames: {num_frames}, got: {end_frame-start_frame}, last event frame: {l}")
            label["_source_info"]["end_frame"] = num_frames + \
                start_frame - label["_source_info"]["pad"][1]
        else:
            print(f"unable to fix, {label['video']}, start_frame: {
                start_frame}, end_frame: {end_frame}, expected num_frames: {num_frames}, got: {end_frame-start_frame}, last event frame: {l}")
    return label


def fix_all(labels: list[Annotation]) -> list[Annotation]:
    for i, label in enumerate(labels):
        labels[i] = fix_one(label)
    return labels


def main():
    for split in ["test", "train", "val"]:
        label_file = LABEL_DIR / f"{split}.json"

        labels = load_json(label_file)
        labels = fix_all(labels=labels)

        with open(label_file, mode="w") as f:
            json.dump(labels, f)


if __name__ == "__main__":
    main()

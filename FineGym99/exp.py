from pathlib import Path

import cv2


if __name__ == "__main__":
    video_dir = Path(__file__).parent / "./FineGym99"

    for video_file in video_dir.glob("*.mp4"):
        cap = cv2.VideoCapture(str(video_file))
        cap.set(cv2.CAP_PROP_POS_FRAMES, 100)
        print(cap.get(cv2.CAP_PROP_FPS))
        print(video_file.stem)

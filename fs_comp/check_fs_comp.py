# Standard Library
import os
import argparse
from pathlib import Path

# Third-Party Library
import cv2
import pandas as pd

# My Library
from FineGym99 import green, red, download, get_proxy_handler


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Command-Line tool for checking FineGym99 dataset")
    parser.add_argument(
        "-fp", "--ffmpeg_path", default="/home/wsf/opts/ffmpeg/bin/ffmpeg",
        type=str, help="Path of ffmpeg executable"
    )
    parser.add_argument(
        "-o", "--outdir", default="fs_comp",
        type=str, help="path to saved downloaded videos"
    )
    parser.add_argument(
        "-p", "--port", default=7890,
        type=int, help="port of command-line proxy"
    )
    parser.add_argument(
        "-i", "--ip", default="127.0.0.1",
        type=str, help="ip of command-line proxy"
    )
    parser.add_argument(
        "-y", "--yt_id", default="None",
        type=str, help="ip of command-line proxy"
    )
    parser.add_argument(
        "-c", "--check", action="store_true",
        help="whether to check or re-download the video"
    )
    return parser.parse_args()


def check_videos(outdir: Path):
    df = pd.read_csv('videos.csv')

    video_dir = Path(outdir)

    for index, row in df.iterrows():
        video_id = row['yt_id']
        expected_fps = float(row['fps'])

        video_files = list(video_dir.glob(f"{video_id}*"))
        if not video_files:
            print(f"Video for give youtube_id {video_id} {red('not exists')}")
        elif len(video_files) >= 2:
            print(f"{red('Multiple')} video for give youtube_id {video_id} found")
        elif len(video_files) == 1:
            video_file = video_files[0]
            cap = cv2.VideoCapture(str(video_file))
            actual_fps = cap.get(cv2.CAP_PROP_FPS)
            cap.release()

            # 检查fps是否符合要求
            if round(actual_fps, ndigits=2) == expected_fps:
                print(f"Video {video_id} fps {green('matches')}, expected {
                    expected_fps}, actual {actual_fps}")
            else:
                print(f"Video {video_id} fps {red('mismatches')}, expected {
                    expected_fps}, actual {actual_fps}")


def redownload(ffmpeg_path: str, outdir: str | Path, ip: str, port: int, yt_id: str, fps: int, height: int, width: int):
    os.environ["ffmpeg_path"] = ffmpeg_path
    download(outdir=outdir, ip=ip, port=port, yt_id=yt_id,
             fps=fps, height=height, width=width)


def main():
    args = get_args()

    if args.check:
        check_videos(Path(args.outdir))
    else:
        # Test Proxy
        ip: str = args.ip
        port: int = int(args.port)
        if ip is not None and port is not None:
            print(f"proxy provided: {green(ip)}:{green(port)}")
            proxy_status, _ = get_proxy_handler(port=port, ip=ip, test=True)
            if not proxy_status:
                print(
                    red(f"Proxy test failed for https://{ip}:{port}"))
                return False
            print(green(f"Proxy test succeed for https://{ip}:{port}"))
        else:
            print("proxy not provided")

        # Get video information
        df = pd.read_csv('videos.csv')

        video_info = df[df['yt_id'] == args.yt_id][['resolution', 'fps']]
        fps = round(video_info['fps'].values[0])
        resolution = video_info['resolution'].values[0]
        width, height = map(int, resolution.split('x'))

        redownload(args.ffmpeg_path, Path(args.outdir),
                   args.ip, args.port, args.yt_id, fps, height, width)


if __name__ == "__main__":
    main()

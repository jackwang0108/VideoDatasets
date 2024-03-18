# Standard Library
import os
import json
import requests
import subprocess
import multiprocessing
from pathlib import Path
from typing import Optional, Callable

# Third-Party Library
import pandas as pd
from colorama import Fore, Style


def colorizer(color: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(text: str, bright: bool = False) -> str:
            colored_text = f"{color}{Style.BRIGHT if bright else ''}{
                text}{Style.RESET_ALL}"
            return colored_text
        return wrapper
    return decorator


@colorizer(Fore.GREEN)
def green(text: str, bright: bool = False):
    return text


@colorizer(Fore.YELLOW)
def yellow(text: str, bright: bool = False):
    return text


@colorizer(Fore.RED)
def red(text: str, bright: bool = False):
    return text


def get_csv() -> pd.DataFrame:
    lines = {}

    for split in ["train", "val", "test"]:

        with (Path(__file__).resolve().parent / f"{split}.json").open(mode="r") as f:
            json_info: list[dict[str, int | str | list | dict]] = json.load(f)

        for unit in json_info:
            name = unit["video"].split("_")[0]
            if name not in lines.keys():
                lines[name] = {
                    "name": name,
                    "resolution": f"{unit['width']}x{unit['height']}",
                    "fps": round(unit["fps"], ndigits=2),
                    "yt_id": name,
                }

    df = pd.DataFrame(lines.values(), columns=list(lines.values())[0].keys())
    df.to_csv(Path(__file__).resolve().parent / "videos.csv", index=None)
    return df


def parse_csv(csv_path: Path | str) -> list[tuple[str, str, str, int]]:

    def process_fps(fps: int) -> int:
        return round(fps)

    df = pd.read_csv(csv_path)
    df["fps"] = df["fps"].apply(process_fps)
    df[['width', 'height']] = df['resolution'].str.split('x', expand=True)

    column_order = ["yt_id", "fps", "height", "width"]
    df = df.reindex(columns=column_order)
    return df.values.tolist()


def get_proxy_handler(port: int | str = 7890, ip: str = "127.0.0.1", test: bool = False) -> tuple[bool, dict[str, str]]:
    """
    get_proxy_handler 返回符合requests.ProxyHandler格式的代理配置

    Args:
        port (int | str): 代理软件端口地址
        ip (str): 代理软件所运行的IP地址
        test (bool): 是否测试代理能否正常使用

    Returns:
        tuple[bool, dict[str, str]]: 一个元组, 包含一个表示代理地址能否正常适用的布尔值以及字典格式的符合requests.ProxyHandler格式的代理配置
    """
    proxy_handler: dict[str, str] = {
        "http": f"http://{ip}:{port}",
        "https": f"http://{ip}:{port}"
    }
    succeeded = True
    if test:
        try:
            response = requests.get(
                "https://www.google.com", proxies=proxy_handler)
            succeeded = response.status_code == 200
        except requests.exceptions.ConnectionError:
            succeeded = False

    return succeeded if test else True, proxy_handler


def download(args):
    outdir, ip, port, youtube_id, fps, height, width = args
    command = (
        f"yt-dlp --proxy http://{ip}:{port} "
        + f'-P {outdir} '
        + f'-f \"bv*[width={width}][height={height}][fps={fps}][ext=mp4]\" '
    ) + f"\"https://www.youtube.com/watch?v={youtube_id}\""
    print((
        "yt-dlp --proxy "
        + green(f"http://{ip}:{port}", True)
        + f' -P {green(outdir, True)}'
        + f' -f \"bv*['
        + green(f"width={width}", True)
        + "][height="
        + green(f"{height}", True)
        + "][fps="
        + green(f"{fps}", True)
        + "][ext="
        + green("mp4", True)
        + "]\""
        + " \"https://www.youtube.com/watch?v="
        + green(f"{youtube_id}", True) + "\""
    ))
    process = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait()
    output, error = process.communicate()
    return output, error


def main(outdir: Path | str, port: int, ip: str):
    """
    多进程YouTube视频下载程序入口函数

    Examples:
        >>> main()
        [True]
    """
    # Test Proxy
    proxy_status, proxy_hdr = get_proxy_handler(port=port, ip=ip, test=True)
    if not proxy_status:
        print(red(f"Proxy test failed, current using: https://{ip}:{port}"))
        return False
    print(green(f"Proxy test succeed, current using: https://{ip}:{port}"))

    videos_to_download = parse_csv(
        Path(__file__).resolve().parent / "videos.csv")

    videos_to_download = [[outdir, ip, port] + i for i in videos_to_download]

    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        results = pool.map(download, videos_to_download)

    for result in results:
        output, error = result
        if output:
            print("Output:", output.decode())
        if error:
            print("Error:", error.decode())
    # output, error = download(videos_to_download[1])
    # print(output)
    # print(error)


if __name__ == "__main__":
    main("./FinGym99", 7890, "127.0.0.1")

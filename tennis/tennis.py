# Standard Library
import json
import requests
import subprocess
import multiprocessing
from pathlib import Path
from typing import Any, Callable


# Third-Party Library
import pandas as pd
from yt_dlp import YoutubeDL
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
    """
    从JSON文件中提取视频信息并返回一个包含视频信息的pandas DataFrame。
    注意, 函数会将该DataFrame保存到video.csv文件中

    返回:
        pd.DataFrame: 包含视频信息的DataFrame。

    示例:
        >>> get_csv()
            name resolution    fps yt_id
        0  video1    1280x720  30.00  video1
        1  video2   1920x1080  24.00  video2
    """

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


def parse_csv(csv_path: Path | str) -> list[tuple[str, int, str, str]]:
    """
    解析CSV文件并将数据作为元组列表返回。

    参数:
        csv_path (Path或str): CSV文件的路径。

    返回:
        list[tuple[str, int, str, str]]: 解析后的数据作为元组列表。
        tuple[str, int, str, str]分别表示一段视频的youtube_id, fps, height, width

    示例:
        >>> parse_csv("data.csv")
        [
            ['634UMLDrVzc', 30, '1080', '1920'],
            ['i8TAarlV4_Q', 30, '1080', '1920'],
            ...
        ]
    """

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


def download(
    outdir: str | Path,
    ip: str,
    port: int,
    yt_id: str,
    fps: int,
    height: str,
    width: str
):
    """
    使用指定参数调用yt-dlp下载YouTube视频。

    参数:
        args (tuple): 包含以下元素的元组，按顺序排列：
            - outdir (str): 下载视频的输出目录。
            - ip (str): 代理连接的IP地址。
            - port (int): 代理连接的端口号。
            - youtube_id (str): YouTube视频的ID。
            - fps (int): 所需的每秒帧数。
            - height (str): 视频的所需高度。
            - width (str): 视频的所需宽度。

    返回:
        tuple: 包含下载过程中的输出和错误信息的元组。
    """

    opts = {
        "quiet": True,
        'noprogress': True,
        "proxy": f"http://{ip}:{port}",
        "geo_bypass_country": "US",
        "outtmpl": f"{outdir}/%(id)s.%(title)s.%(ext)s",
        "format": f"bv*[width={width}][height={height}][fps={fps}][ext=mp4]",
    }

    info = [
        "yt-dlp",
        f"-P {green('/'.join(outdir.parts[-2:]), True)}",
        "--proxy",
        f"http://{green(ip, True)}:{green(port, True)}",
        "-f",
        f"bv*[width={green(width, True)}]"
        + f"[height={green(height, True)}]"
        + f"[fps={green(fps, True)}]"
        + f"[ext={green('mp4', True)}]",
        f"https://www.youtube.com/watch?v={green(yt_id, True)}",
    ]
    print(" ".join(info))
    yt = YoutubeDL(
        opts
    )
    url = f"https://www.youtube.com/watch?v={yt_id}"
    return yt.download(url) == 0, yt_id


def main(outdir: Path | str, port: int, ip: str):
    """
    使用多进程从CSV文件下载视频。

    参数:
        outdir (Path或str): 下载视频的输出目录。
        port (int): 代理连接的端口号。
        ip (str): 代理连接的IP地址。

    返回:
        bool: 如果代理测试成功则返回True，否则返回False。

    示例:
        >>> main("videos/", 8080, "127.0.0.1")
        代理测试成功，当前使用: https://127.0.0.1:8080
        输出: ...
        错误: ...
    """

    # Test Proxy
    proxy_status, _ = get_proxy_handler(port=port, ip=ip, test=True)
    if not proxy_status:
        print(red(f"Proxy test failed, current using: https://{ip}:{port}"))
        return False
    print(green(f"Proxy test succeed, current using: https://{ip}:{port}"))

    videos_to_download = parse_csv(
        Path(__file__).resolve().parent / "videos.csv")

    async_results = []
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    for video_info in videos_to_download:
        yt_id, fps, height, width = video_info
        r = pool.apply_async(
            download, (outdir, ip, port, yt_id, fps, height, width)
        )
        async_results.append(r)

    pool.close()
    pool.join()

    results = [i.get() for i in async_results]
    for r in results:
        success, yt_id = r
        with (Path(__file__).resolve().parent / "result.txt").open(mode="w") as f:
            f.write(f"{yt_id}, {success}")


if __name__ == "__main__":
    main(Path(__file__).resolve().parent / "tennis", 7890, "127.0.0.1")

# Standard Library
import os
import requests
import urllib.error
import multiprocessing
from pathlib import Path
from typing import Optional, Callable


# Third-Party Library
from pytube import YouTube


# Third-Party Library
import pandas as pd
import pytube.exceptions
from pytube import YouTube
from colorama import Fore, Style
from pytube.query import Stream, StreamQuery


class ProxyError(Exception):
    def __init__(self) -> None:
        super().__init__()
        self.message = "Proxy Error"


class VideoNotFoundError(Exception):
    def __init__(self, youtube_id: str) -> None:
        super().__init__()
        self.message = f"No Video Found {youtube_id}"


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


def parse_csv(csv_path: Path | str) -> list[tuple[str, str, str, int]]:
    def process_resolution(res: str) -> str:
        if res == "1920x1080":
            return "1080p"
        elif res == "1280x720":
            return "720p"

    def process_fps(fps: int) -> int:
        return round(fps)

    df = pd.read_csv(csv_path)
    df["fps"] = df["fps"].apply(process_fps)
    df["resolution"] = df["resolution"].apply(process_resolution)

    column_order = ["name", "yt_id", "resolution", "fps"]
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


def download(youtube_id: str, fps: int, resolution: str, proxy_handler: dict[str, str], filename: str, output_dir: Optional[Path | str] = None) -> bool:
    """
    从Youtube上下载指定参数的视频

    Args:
        youtube_id (str): YouTube视频ID.
        fps (int): 将下载视频的FPS
        resolution (str): 将下载视频的分辨率
        proxy_handler (dict[str, str]): 代理设置的字典
        output_name (str): 下载视频保存的文件名
        output_dir (Path | str): 下载视频输出的目录

    Returns:
        bool: 如果视频成功下载则返回True, 否则返回False

    Raises:
        ProxyError: 如果下载视频的时候因为代理导致下载失败
        NoneVideoError: 如果没有根据的参数找到可以下载的视频

    Examples:
        >>> download("cZqaa0b34vk", 30, "720p", {"http": "http://127.0.0.1:7890", "https": "http://127.0.0.1:7890"}, "/path/to/output")
        True
    """

    # get the video
    url: str = f"https://www.youtube.com/watch?v={youtube_id}"
    yt: YouTube = YouTube(
        url=url,
        proxies=proxy_handler,
        # use_oauth=True,
        # allow_oauth_cache=True,
    )
    try:
        streams: StreamQuery = yt.streams.filter(
            fps=fps, resolution=resolution)
    except urllib.error.URLError as e:
        print(F"Proxy error at downloading: {url}")
        raise ProxyError from e
    except pytube.exceptions.AgeRestrictedError:
        print(f"Downloading {filename} failed because of age restriction")
        return False

    # filter out the video
    if len(streams) == 0:
        raise VideoNotFoundError(youtube_id)
    target_video: Stream = streams[0]

    video_size: float = round(target_video.filesize / 1024 / 1024, ndigits=2)
    print(f"Start downloading video: {
          green(target_video.title)}, filesize: {green(video_size, True)} MB")

    # prepare output dir

    if output_dir is not None:
        assert isinstance(
            output_dir, (str, Path)
        ), "output_dir should be either Path or str"
        output_dir = Path(output_dir) if isinstance(
            output_dir, str) else output_dir
        if not output_dir.exists():
            output_dir.mkdir(parents=True, exist_ok=True)
    else:
        output_dir = Path(os.getcwd())

    # download the video and check
    video_path: Path = Path(target_video.download(
        str(output_dir), filename=filename, max_retries=3))
    return video_path.exists()


def main_worker(filename: str, youtube_id: str, resolution: str, fps: int, outdir: Optional[Path | str] = None):
    """
    执行从YouTube下载视频的任务的工作函数

    Args:
        youtube_id (str): YouTube视频ID.
        resolution (str): YouTube视频分辨率.
        fps (int): YouTube视频FPS

    Returns:
        如果下载成功, 返回True, 否则返回False

    Examples:
        >>> main_worker("cZqaa0b34vk", "720p", 30)
        True
    """

    proxy_ok, proxy = get_proxy_handler(test=True)
    if not proxy_ok:
        print(f"Proxy Test {yellow('failed', True)}, did you open proxy now?")
        return False

    max_retry = 3
    success = False
    print(f"Processing: {filename}")
    while max_retry > 0 and not success:
        try:
            success = download(youtube_id=youtube_id, fps=fps,
                               resolution=resolution, proxy_handler=proxy, output_dir=outdir, filename=filename)
            if success:
                print(f"Download {green('Success')}: {filename}")
        except ProxyError as e:
            max_retry -= 1
            success = False
            print(f"Download video {
                filename} {yellow('failed', True)} because of proxy error, will retry later...")
        except VideoNotFoundError as e:
            max_retry = 0
            success = False
            print(f"Download video {
                filename} {red('failed', True)} because of video not found, failed!")
    return success


def main(outdir: Path | str):
    """
    多进程YouTube视频下载程序入口函数

    Examples:
        >>> main()
        [True]
    """

    videos_to_download = parse_csv("./data/tennis/videos.csv")

    async_results = []
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    for filename, video_id, resolution, fps in videos_to_download:
        result = pool.apply_async(
            main_worker, (filename, video_id, resolution, fps, outdir))
        async_results.append(result)

    # 等待所有任务完成
    pool.close()
    pool.join()

    results = [
        [video_info[0], async_result.get()]
        for video_info, async_result in zip(videos_to_download, async_results)
    ]

    with open("tennis_result.txt", mode="w") as f:
        for r in results:
            f.write(f"{r[0]}, {r[1]}\n")


if __name__ == "__main__":
    main("./tennis")

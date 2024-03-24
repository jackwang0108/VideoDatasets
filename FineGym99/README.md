# FineGym99 datasets

## Introduction


The FineGym99 datasets is a hierarchical video dataset for fine-grained action understanding and is first proposed in CVPR 2020 [oral](https://sdolivia.github.io/FineGym/).

Like other video datasets, the author of the original datasets provides annotations and the Youtube id of the videos, so that you need to obtain the videos from the Youtube.

[Spot](https://github.com/jhong93/spot) provided extra annotations for the task of spotting temporally precise, fine-
grained events in videos, thus converting the original datasets into temporally precise fine-grained event spotting datasets.

The videos are from the Youtube, and the annotations are provided in https://github.com/jhong93/spot which is also included in this repository.

## Obtain the tennis datasets


### 1. Obtaining the videos

I'be provided a script to download the FineGym99 videos from Youtube.

Run

```bash
python FineGym99.py --outdir <path-to-save-downloaded-videos> --ffmpeg_path <path-of-ffmpeg-executables>
```

to download the videos. If Youtube is restricted in your area, you can also pass the proxy as argument.

```bash
python FineGym99.py --ip <your-proxy-ip-address> --port <your-proxy-port> --outdir <path-to-save-downloaded-videos> --ffmpeg_path <path-of-ffmpeg-executables>
```

For detail information, please check `FineGym99.py`

> Note, if you want to obtain the videos from youtube by yourself, make sure to download the correct frame rate and quality settings.
> Please follow the FPS and requirements in `videos.csv` to download the correct videos.

### 2. Resume the videos

Sometimes, if the internet is disconnected or the socket is broken, the downloading process for a specific video is stopped so that intermediate files are left in `outdir`.

To resume the download, just re-run the command above.

Or you can run `check_FineGym99.py` to download the specific videos.

### 3. Check the videos

To check the FPS matches the requirements of the datasets, run

```bash
python check_FineGym99.py -c
```

If you need to re-download a specific video, run


```bash
python check_FineGym99.py -y <Youtube-ID>
```
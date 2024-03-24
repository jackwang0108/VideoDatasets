# Tennis datasets

## Introduction


The tennis datasets is first proposed in [Vid2Player](https://cs.stanford.edu/~haotianz/research/vid2player/) to convert annotated broadcast video of tennis matches into interactively controllable video sprites. 

[Spot](https://github.com/jhong93/spot) provided extra annotations for the task of spotting temporally precise, fine-
grained events in videos, thus converting the original datasets into temporally precise fine-grained event spotting datasets.

The videos are from the Youtube, and the annotations are provided in https://github.com/jhong93/spot which is also included in this repository.

## Obtain the tennis datasets


### 1. Obtaining the videos

I'be provided a script to download the tennis videos from Youtube.

Run

```bash
python tennis.py --outdir <path-to-save-downloaded-videos> --ffmpeg_path <path-of-ffmpeg-executables>
```

to download the videos. If Youtube is restricted in your area, you can also pass the proxy as argument.

```bash
python tennis.py --ip <your-proxy-ip-address> --port <your-proxy-port> --outdir <path-to-save-downloaded-videos> --ffmpeg_path <path-of-ffmpeg-executables>
```

For detail information, please check `tennis.py`

> Note, if you want to obtain the videos from youtube, make sure to download the correct frame rate and quality settings.
> 1080P resolution is used for all of the videos. Wimbledon videos are 25.0 FPS and US Open videos are 30 FPS.
> Please check `videos.csv` fpr detailed information about the FPS and resolution 

### 2. Resume the videos

Sometimes, if the internet is disconnected or the socket is broken, the downloading process for a specific video is stopped so that intermediate files are left in `outdir`. 

To resume the download, just re-run the command above.

Our you can run the `check_tennis.py` for one or two videos.

### 3. Check the videos

To check the FPS matches the requirements of the datasets, run

```bash
python check_tennis.py -c
```

If you need to re-download a specific video, run


```bash
python check_tennis.py -y <Youtube-ID>
```
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

Note: Some of the videos is already invalid on the Youtube, for example, the account associated with the video has been terminated.
So, the download will fail, please check `result.txt` for invalid videos.

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


### Fix the labels

Note, some labels are mismatched, for example, `4mzbybgzoJo_E_*_*` start frame and end frame mismatches with the num frames in the `test.json`.


So, if you obtain the label from the original source, run:

```bash
python fix_FineGym99.py
```
to fix them before making datasets.. The output log: 

```bash

fixing 4kG0jbeQ70g_E_001023_001113, start_frame: 51078, end_frame: 55745, expected num_frames: 2334, got: 4667, last event frame: 2287
fixing 4kG0jbeQ70g_E_001295_001393, start_frame: 64672, end_frame: 69749, expected num_frames: 2539, got: 5077, last event frame: 2506
fixing 4kG0jbeQ70g_E_001969_002058, start_frame: 98418, end_frame: 103000, expected num_frames: 2291, got: 4582, last event frame: 2262
fixing 4kG0jbeQ70g_E_002230_002314, start_frame: 111444, end_frame: 115798, expected num_frames: 2177, got: 4354, last event frame: 2149
fixing 4kG0jbeQ70g_E_002464_002565, start_frame: 123176, end_frame: 128379, expected num_frames: 2602, got: 5203, last event frame: 2553
fixing 4kG0jbeQ70g_E_002715_002788, start_frame: 135673, end_frame: 139482, expected num_frames: 1905, got: 3809, last event frame: 1869
fixing 4kG0jbeQ70g_E_003350_003451, start_frame: 167409, end_frame: 172604, expected num_frames: 2598, got: 5195, last event frame: 2395
fixing 4kG0jbeQ70g_E_003900_003999, start_frame: 194921, end_frame: 200047, expected num_frames: 2563, got: 5126, last event frame: 2249
fixing 4kG0jbeQ70g_E_004124_004221, start_frame: 206144, end_frame: 211142, expected num_frames: 2499, got: 4998, last event frame: 2341
fixing 4kG0jbeQ70g_E_004561_004663, start_frame: 228037, end_frame: 233231, expected num_frames: 2597, got: 5194, last event frame: 2397
fixing 4kG0jbeQ70g_E_005049_005151, start_frame: 252389, end_frame: 257667, expected num_frames: 2639, got: 5278, last event frame: 2440
fixing 4mzbybgzoJo_E_000054_000152, start_frame: 3201, end_frame: 9240, expected num_frames: 3020, got: 6039, last event frame: 2974
fixing 4mzbybgzoJo_E_000366_000469, start_frame: 21884, end_frame: 28229, expected num_frames: 3173, got: 6345, last event frame: 3127
fixing 4mzbybgzoJo_E_000705_000813, start_frame: 42167, end_frame: 48836, expected num_frames: 3335, got: 6669, last event frame: 3283
fixing 4mzbybgzoJo_E_001033_001126, start_frame: 61865, end_frame: 67591, expected num_frames: 2863, got: 5726, last event frame: 2820
fixing 4mzbybgzoJo_E_001292_001377, start_frame: 77438, end_frame: 82644, expected num_frames: 2603, got: 5206, last event frame: 2561
fixing 4mzbybgzoJo_E_001613_001704, start_frame: 96677, end_frame: 102240, expected num_frames: 2782, got: 5563, last event frame: 2747
fixing 4mzbybgzoJo_E_001857_001946, start_frame: 111271, end_frame: 116735, expected num_frames: 2732, got: 5464, last event frame: 2699
fixing 4mzbybgzoJo_E_002223_002324, start_frame: 133168, end_frame: 139415, expected num_frames: 3124, got: 6247, last event frame: 3065
fixing 4mzbybgzoJo_E_002935_003036, start_frame: 175913, end_frame: 182053, expected num_frames: 3070, got: 6140, last event frame: 2963
fixing 4mzbybgzoJo_E_003248_003354, start_frame: 194574, end_frame: 201156, expected num_frames: 3291, got: 6582, last event frame: 3004
fixing 4mzbybgzoJo_E_003835_003935, start_frame: 229789, end_frame: 235962, expected num_frames: 3087, got: 6173, last event frame: 2818
fixing 4mzbybgzoJo_E_004128_004229, start_frame: 247361, end_frame: 253629, expected num_frames: 3134, got: 6268, last event frame: 2854
fixing 4mzbybgzoJo_E_004450_004555, start_frame: 266656, end_frame: 273149, expected num_frames: 3247, got: 6493, last event frame: 2939
fixing 4mzbybgzoJo_E_004722_004827, start_frame: 283005, end_frame: 289447, expected num_frames: 3221, got: 6442, last event frame: 2879
fixing UyGu-WTodV0_E_002244_002251, start_frame: 112167, end_frame: 112679, expected num_frames: 256, got: 512, last event frame: 209
fixing UyGu-WTodV0_E_002336_002344, start_frame: 116772, end_frame: 117309, expected num_frames: 269, got: 537, last event frame: 219
fixing UyGu-WTodV0_E_002442_002452, start_frame: 122097, end_frame: 122673, expected num_frames: 288, got: 576, last event frame: 253
fixing UyGu-WTodV0_E_002443_002452, start_frame: 122090, end_frame: 122705, expected num_frames: 308, got: 615, last event frame: 258
fixing UyGu-WTodV0_E_002541_002550, start_frame: 126960, end_frame: 127599, expected num_frames: 320, got: 639, last event frame: 273
fixing UyGu-WTodV0_E_002628_002637, start_frame: 131359, end_frame: 131970, expected num_frames: 306, got: 611, last event frame: 257
fixing UyGu-WTodV0_E_002716_002723, start_frame: 135754, end_frame: 136264, expected num_frames: 255, got: 510, last event frame: 215
fixing UyGu-WTodV0_E_002812_002820, start_frame: 140563, end_frame: 141113, expected num_frames: 275, got: 550, last event frame: 232
fixing UyGu-WTodV0_E_002930_002939, start_frame: 146464, end_frame: 147044, expected num_frames: 290, got: 580, last event frame: 247
fixing UyGu-WTodV0_E_003027_003036, start_frame: 151298, end_frame: 151909, expected num_frames: 306, got: 611, last event frame: 262
fixing UyGu-WTodV0_E_003028_003036, start_frame: 151344, end_frame: 151881, expected num_frames: 269, got: 537, last event frame: 239
fixing UyGu-WTodV0_E_003109_003117, start_frame: 155434, end_frame: 155924, expected num_frames: 245, got: 490, last event frame: 218
fixing UyGu-WTodV0_E_003213_003221, start_frame: 160598, end_frame: 161183, expected num_frames: 293, got: 585, last event frame: 245
fixing UyGu-WTodV0_E_003308_003317, start_frame: 165362, end_frame: 165944, expected num_frames: 291, got: 582, last event frame: 247
fixing UyGu-WTodV0_E_003528_003536, start_frame: 176325, end_frame: 176920, expected num_frames: 298, got: 595, last event frame: 250
fixing UyGu-WTodV0_E_003623_003631, start_frame: 181128, end_frame: 181662, expected num_frames: 267, got: 534, last event frame: 214
fixing UyGu-WTodV0_E_003713_003720, start_frame: 185604, end_frame: 186067, expected num_frames: 232, got: 463, last event frame: 200
fixing UyGu-WTodV0_E_006755_006797, start_frame: 337715, end_frame: 339967, expected num_frames: 1126, got: 2252, last event frame: 1086
fixing UyGu-WTodV0_E_006954_007003, start_frame: 347630, end_frame: 350226, expected num_frames: 1298, got: 2596, last event frame: 1267
fixing UyGu-WTodV0_E_007212_007245, start_frame: 360554, end_frame: 362333, expected num_frames: 890, got: 1779, last event frame: 850
fixing UyGu-WTodV0_E_007416_007445, start_frame: 370725, end_frame: 372337, expected num_frames: 806, got: 1612, last event frame: 764
fixing UyGu-WTodV0_E_007635_007667, start_frame: 381680, end_frame: 383463, expected num_frames: 892, got: 1783, last event frame: 850
fixing UyGu-WTodV0_E_007801_007843, start_frame: 390010, end_frame: 392246, expected num_frames: 1118, got: 2236, last event frame: 1072
fixing UyGu-WTodV0_E_007995_008032, start_frame: 399682, end_frame: 401703, expected num_frames: 1011, got: 2021, last event frame: 962
fixing UyGu-WTodV0_E_008153_008188, start_frame: 407591, end_frame: 409535, expected num_frames: 972, got: 1944, last event frame: 926
fixing hmHwFuvodg0_E_002398_002405, start_frame: 119859, end_frame: 120343, expected num_frames: 242, got: 484, last event frame: 201
fixing hmHwFuvodg0_E_002557_002563, start_frame: 127783, end_frame: 128266, expected num_frames: 242, got: 483, last event frame: 204
fixing hmHwFuvodg0_E_002669_002679, start_frame: 133430, end_frame: 134033, expected num_frames: 302, got: 603, last event frame: 265
fixing hmHwFuvodg0_E_002765_002774, start_frame: 138157, end_frame: 138793, expected num_frames: 318, got: 636, last event frame: 276
fixing hmHwFuvodg0_E_002895_002904, start_frame: 144709, end_frame: 145309, expected num_frames: 300, got: 600, last event frame: 261
fixing hmHwFuvodg0_E_002989_002997, start_frame: 149399, end_frame: 149966, expected num_frames: 284, got: 567, last event frame: 247
fixing hmHwFuvodg0_E_003140_003149, start_frame: 156944, end_frame: 157571, expected num_frames: 314, got: 627, last event frame: 272
fixing hmHwFuvodg0_E_003252_003261, start_frame: 162566, end_frame: 163174, expected num_frames: 304, got: 608, last event frame: 256
fixing hmHwFuvodg0_E_003385_003393, start_frame: 169226, end_frame: 169777, expected num_frames: 276, got: 551, last event frame: 227
fixing hmHwFuvodg0_E_003473_003481, start_frame: 173604, end_frame: 174126, expected num_frames: 261, got: 522, last event frame: 224
fixing hmHwFuvodg0_E_003635_003643, start_frame: 181701, end_frame: 182255, expected num_frames: 277, got: 554, last event frame: 234
fixing hmHwFuvodg0_E_003716_003724, start_frame: 185774, end_frame: 186317, expected num_frames: 272, got: 543, last event frame: 204
fixing hmHwFuvodg0_E_003887_003898, start_frame: 194293, end_frame: 194963, expected num_frames: 335, got: 670, last event frame: 302
fixing hmHwFuvodg0_E_004104_004112, start_frame: 205142, end_frame: 205702, expected num_frames: 280, got: 560, last event frame: 238
fixing hmHwFuvodg0_E_004203_004211, start_frame: 210103, end_frame: 210650, expected num_frames: 274, got: 547, last event frame: 229
fixing hmHwFuvodg0_E_004749_004832, start_frame: 237418, end_frame: 241693, expected num_frames: 2138, got: 4275, last event frame: 2105
fixing hmHwFuvodg0_E_005279_005320, start_frame: 263880, end_frame: 266082, expected num_frames: 1101, got: 2202, last event frame: 1075
fixing hmHwFuvodg0_E_005481_005522, start_frame: 274016, end_frame: 276193, expected num_frames: 1089, got: 2177, last event frame: 1051
fixing hmHwFuvodg0_E_005964_005997, start_frame: 298133, end_frame: 299956, expected num_frames: 912, got: 1823, last event frame: 865
fixing hmHwFuvodg0_E_006188_006223, start_frame: 309344, end_frame: 311254, expected num_frames: 955, got: 1910, last event frame: 914
fixing hmHwFuvodg0_E_006438_006473, start_frame: 321810, end_frame: 323759, expected num_frames: 975, got: 1949, last event frame: 942
fixing k8zhOvRBjGo_E_000229_000337, start_frame: 13696, end_frame: 20281, expected num_frames: 3293, got: 6585, last event frame: 2929
fixing k8zhOvRBjGo_E_000377_000385, start_frame: 22482, end_frame: 23171, expected num_frames: 345, got: 689, last event frame: 295
fixing k8zhOvRBjGo_E_000538_000548, start_frame: 32190, end_frame: 32966, expected num_frames: 388, got: 776, last event frame: 319
fixing k8zhOvRBjGo_E_000624_000728, start_frame: 37301, end_frame: 43755, expected num_frames: 3227, got: 6454, last event frame: 2921
fixing k8zhOvRBjGo_E_000931_000939, start_frame: 55738, end_frame: 56419, expected num_frames: 341, got: 681, last event frame: 284
fixing k8zhOvRBjGo_E_001034_001136, start_frame: 61962, end_frame: 68182, expected num_frames: 3110, got: 6220, last event frame: 2818
fixing k8zhOvRBjGo_E_001234_001337, start_frame: 73950, end_frame: 80275, expected num_frames: 3163, got: 6325, last event frame: 2818
fixing k8zhOvRBjGo_E_001570_001608, start_frame: 94017, end_frame: 96484, expected num_frames: 1234, got: 2467, last event frame: 1183
fixing k8zhOvRBjGo_E_001649_001658, start_frame: 98772, end_frame: 99477, expected num_frames: 353, got: 705, last event frame: 302
fixing k8zhOvRBjGo_E_001811_001842, start_frame: 108535, end_frame: 110538, expected num_frames: 1002, got: 2003, last event frame: 954
fixing k8zhOvRBjGo_E_001976_001984, start_frame: 118402, end_frame: 119021, expected num_frames: 310, got: 619, last event frame: 262
fixing k8zhOvRBjGo_E_002045_002052, start_frame: 122509, end_frame: 123081, expected num_frames: 286, got: 572, last event frame: 242
fixing k8zhOvRBjGo_E_002169_002201, start_frame: 129921, end_frame: 132005, expected num_frames: 1042, got: 2084, last event frame: 1003
fixing k8zhOvRBjGo_E_002317_002353, start_frame: 138842, end_frame: 141160, expected num_frames: 1159, got: 2318, last event frame: 1123
fixing k8zhOvRBjGo_E_002426_002518, start_frame: 145374, end_frame: 151034, expected num_frames: 2830, got: 5660, last event frame: 2773
fixing k8zhOvRBjGo_E_002665_002759, start_frame: 159688, end_frame: 165497, expected num_frames: 2905, got: 5809, last event frame: 2846
fixing k8zhOvRBjGo_E_003010_003041, start_frame: 180359, end_frame: 182401, expected num_frames: 1021, got: 2042, last event frame: 986
fixing k8zhOvRBjGo_E_003234_003268, start_frame: 193779, end_frame: 196029, expected num_frames: 1125, got: 2250, last event frame: 1080
fixing k8zhOvRBjGo_E_003335_003429, start_frame: 199817, end_frame: 205611, expected num_frames: 2897, got: 5794, last event frame: 2858
fixing k8zhOvRBjGo_E_003517_003554, start_frame: 210802, end_frame: 213144, expected num_frames: 1171, got: 2342, last event frame: 1121
fixing k8zhOvRBjGo_E_003636_003732, start_frame: 217925, end_frame: 223776, expected num_frames: 2926, got: 5851, last event frame: 2869
fixing k8zhOvRBjGo_E_003899_004002, start_frame: 233662, end_frame: 239983, expected num_frames: 3161, got: 6321, last event frame: 2936
fixing k8zhOvRBjGo_E_004223_004305, start_frame: 253101, end_frame: 258184, expected num_frames: 2542, got: 5083, last event frame: 2488
fixing k8zhOvRBjGo_E_004428_004514, start_frame: 265369, end_frame: 270665, expected num_frames: 2648, got: 5296, last event frame: 2600
fixing k8zhOvRBjGo_E_004628_004724, start_frame: 277328, end_frame: 283280, expected num_frames: 2976, got: 5952, last event frame: 2917
fixing k8zhOvRBjGo_E_004946_005037, start_frame: 296409, end_frame: 302027, expected num_frames: 2809, got: 5618, last event frame: 2756
fixing k8zhOvRBjGo_E_005146_005246, start_frame: 308349, end_frame: 314562, expected num_frames: 3107, got: 6213, last event frame: 2882
fixing k8zhOvRBjGo_E_005558_005650, start_frame: 333125, end_frame: 338792, expected num_frames: 2834, got: 5667, last event frame: 2777
fixing rrrgsW--AE8_E_031139_031215, start_frame: 918439, end_frame: 920763, expected num_frames: 2313, got: 2324, last event frame: 2283
fixing sEgELazFtxQ_E_000458_000465, start_frame: 22846, end_frame: 23364, expected num_frames: 259, got: 518, last event frame: 209
fixing sEgELazFtxQ_E_000479_000486, start_frame: 23898, end_frame: 24387, expected num_frames: 245, got: 489, last event frame: 200
fixing sEgELazFtxQ_E_000531_000537, start_frame: 26497, end_frame: 26946, expected num_frames: 225, got: 449, last event frame: 178
fixing sEgELazFtxQ_E_000556_000561, start_frame: 27706, end_frame: 28168, expected num_frames: 231, got: 462, last event frame: 190
fixing sEgELazFtxQ_E_000645_000653, start_frame: 32208, end_frame: 32738, expected num_frames: 265, got: 530, last event frame: 217
fixing sEgELazFtxQ_E_000688_000696, start_frame: 34377, end_frame: 34877, expected num_frames: 250, got: 500, last event frame: 207
fixing sEgELazFtxQ_E_000785_000792, start_frame: 39219, end_frame: 39679, expected num_frames: 230, got: 460, last event frame: 195
fixing sEgELazFtxQ_E_000803_000811, start_frame: 40091, end_frame: 40645, expected num_frames: 277, got: 554, last event frame: 226
fixing sEgELazFtxQ_E_000862_000869, start_frame: 43040, end_frame: 43506, expected num_frames: 233, got: 466, last event frame: 205
fixing sEgELazFtxQ_E_000890_000900, start_frame: 44411, end_frame: 45079, expected num_frames: 334, got: 668, last event frame: 299
fixing sEgELazFtxQ_E_000973_000979, start_frame: 48609, end_frame: 49037, expected num_frames: 214, got: 428, last event frame: 170
fixing sEgELazFtxQ_E_001091_001098, start_frame: 54521, end_frame: 54986, expected num_frames: 233, got: 465, last event frame: 190
fixing sEgELazFtxQ_E_001193_001199, start_frame: 59568, end_frame: 60049, expected num_frames: 241, got: 481, last event frame: 203
fixing sEgELazFtxQ_E_001298_001304, start_frame: 64893, end_frame: 65307, expected num_frames: 207, got: 414, last event frame: 165
fixing sEgELazFtxQ_E_001415_001422, start_frame: 70715, end_frame: 71204, expected num_frames: 245, got: 489, last event frame: 201
fixing sEgELazFtxQ_E_001517_001524, start_frame: 75817, end_frame: 76290, expected num_frames: 237, got: 473, last event frame: 206
fixing sEgELazFtxQ_E_001623_001630, start_frame: 81124, end_frame: 81628, expected num_frames: 252, got: 504, last event frame: 204
fixing sEgELazFtxQ_E_001734_001741, start_frame: 86609, end_frame: 87164, expected num_frames: 278, got: 555, last event frame: 234
fixing sEgELazFtxQ_E_002403_002435, start_frame: 120092, end_frame: 121825, expected num_frames: 867, got: 1733, last event frame: 841
fixing sEgELazFtxQ_E_002558_002600, start_frame: 127833, end_frame: 130135, expected num_frames: 1151, got: 2302, last event frame: 1104
fixing sEgELazFtxQ_E_002911_002950, start_frame: 145500, end_frame: 147585, expected num_frames: 1043, got: 2085, last event frame: 1009
fixing sEgELazFtxQ_E_003268_003310, start_frame: 163349, end_frame: 165625, expected num_frames: 1138, got: 2276, last event frame: 1094
fixing sEgELazFtxQ_E_003442_003483, start_frame: 172031, end_frame: 174229, expected num_frames: 1099, got: 2198, last event frame: 1068
fixing sEgELazFtxQ_E_003608_003649, start_frame: 180329, end_frame: 182545, expected num_frames: 1108, got: 2216, last event frame: 1079
fixing sEgELazFtxQ_E_003811_003848, start_frame: 190488, end_frame: 192491, expected num_frames: 1002, got: 2003, last event frame: 970
fixing sEgELazFtxQ_E_004564_004660, start_frame: 228148, end_frame: 233085, expected num_frames: 2469, got: 4937, last event frame: 2435
fixing sEgELazFtxQ_E_004771_004854, start_frame: 238490, end_frame: 242802, expected num_frames: 2156, got: 4312, last event frame: 2115
fixing sEgELazFtxQ_E_004963_005057, start_frame: 248090, end_frame: 252976, expected num_frames: 2443, got: 4886, last event frame: 2400
fixing sEgELazFtxQ_E_005163_005264, start_frame: 258082, end_frame: 263291, expected num_frames: 2605, got: 5209, last event frame: 2565
fixing sEgELazFtxQ_E_005607_005709, start_frame: 280298, end_frame: 285542, expected num_frames: 2622, got: 5244, last event frame: 2587
fixing sEgELazFtxQ_E_005811_005912, start_frame: 290472, end_frame: 295734, expected num_frames: 2631, got: 5262, last event frame: 2581
fixing sEgELazFtxQ_E_006057_006152, start_frame: 302784, end_frame: 307691, expected num_frames: 2454, got: 4907, last event frame: 2413
fixing sEgELazFtxQ_E_006644_006746, start_frame: 332126, end_frame: 337404, expected num_frames: 2639, got: 5278, last event frame: 2502
fixing sEgELazFtxQ_E_006861_006961, start_frame: 343001, end_frame: 348127, expected num_frames: 2563, got: 5126, last event frame: 2236
fixing sEgELazFtxQ_E_007049_007152, start_frame: 352413, end_frame: 357719, expected num_frames: 2653, got: 5306, last event frame: 2330
fixing sEgELazFtxQ_E_007265_007372, start_frame: 363213, end_frame: 368698, expected num_frames: 2743, got: 5485, last event frame: 2542
fixing sEgELazFtxQ_E_007535_007638, start_frame: 376709, end_frame: 381980, expected num_frames: 2636, got: 5271, last event frame: 2466
fixing sEgELazFtxQ_E_008008_008107, start_frame: 400336, end_frame: 405467, expected num_frames: 2566, got: 5131, last event frame: 2388
fixing sEgELazFtxQ_E_008228_008325, start_frame: 411343, end_frame: 416365, expected num_frames: 2511, got: 5022, last event frame: 2254
fixing sEgELazFtxQ_E_008450_008537, start_frame: 422425, end_frame: 426956, expected num_frames: 2266, got: 4531, last event frame: 2064
fixing yj0pNXcTK0k_E_001579_001587, start_frame: 94599, end_frame: 95244, expected num_frames: 323, got: 645, last event frame: 258
fixing yj0pNXcTK0k_E_001658_001665, start_frame: 99296, end_frame: 99967, expected num_frames: 336, got: 671, last event frame: 276
fixing yj0pNXcTK0k_E_001907_001915, start_frame: 114242, end_frame: 114888, expected num_frames: 323, got: 646, last event frame: 261
fixing yj0pNXcTK0k_E_001977_001985, start_frame: 118410, end_frame: 119055, expected num_frames: 323, got: 645, last event frame: 275
fixing yj0pNXcTK0k_E_002206_002214, start_frame: 132135, end_frame: 132779, expected num_frames: 322, got: 644, last event frame: 284
fixing yj0pNXcTK0k_E_002235_002247, start_frame: 133923, end_frame: 134835, expected num_frames: 456, got: 912, last event frame: 407
fixing yj0pNXcTK0k_E_002287_002295, start_frame: 137041, end_frame: 137657, expected num_frames: 308, got: 616, last event frame: 267
fixing yj0pNXcTK0k_E_002554_002563, start_frame: 153060, end_frame: 153766, expected num_frames: 353, got: 706, last event frame: 293
fixing yj0pNXcTK0k_E_002608_002616, start_frame: 156259, end_frame: 156927, expected num_frames: 334, got: 668, last event frame: 291
fixing yj0pNXcTK0k_E_002796_002804, start_frame: 167538, end_frame: 168170, expected num_frames: 316, got: 632, last event frame: 268
fixing yj0pNXcTK0k_E_002846_002854, start_frame: 170537, end_frame: 171151, expected num_frames: 307, got: 614, last event frame: 257
fixing yj0pNXcTK0k_E_002866_002877, start_frame: 171698, end_frame: 172578, expected num_frames: 440, got: 880, last event frame: 349
fixing yj0pNXcTK0k_E_002885_002898, start_frame: 172861, end_frame: 173808, expected num_frames: 474, got: 947, last event frame: 409
fixing yj0pNXcTK0k_E_003113_003129, start_frame: 186550, end_frame: 187635, expected num_frames: 543, got: 1085, last event frame: 501
fixing yj0pNXcTK0k_E_003164_003172, start_frame: 189587, end_frame: 190227, expected num_frames: 320, got: 640, last event frame: 284
fixing yj0pNXcTK0k_E_003432_003441, start_frame: 205647, end_frame: 206410, expected num_frames: 382, got: 763, last event frame: 323
fixing yj0pNXcTK0k_E_003489_003497, start_frame: 209073, end_frame: 209756, expected num_frames: 342, got: 683, last event frame: 290
fixing yj0pNXcTK0k_E_003701_003708, start_frame: 221783, end_frame: 222398, expected num_frames: 308, got: 615, last event frame: 259
fixing yj0pNXcTK0k_E_003729_003743, start_frame: 223456, end_frame: 224450, expected num_frames: 497, got: 994, last event frame: 450
fixing yj0pNXcTK0k_E_003788_003796, start_frame: 227009, end_frame: 227632, expected num_frames: 312, got: 623, last event frame: 265
fixing yj0pNXcTK0k_E_003811_003827, start_frame: 228351, end_frame: 229513, expected num_frames: 581, got: 1162, last event frame: 522
fixing yj0pNXcTK0k_E_004063_004101, start_frame: 243497, end_frame: 245945, expected num_frames: 1224, got: 2448, last event frame: 1172
fixing yj0pNXcTK0k_E_004354_004385, start_frame: 260952, end_frame: 262967, expected num_frames: 1008, got: 2015, last event frame: 969
fixing yj0pNXcTK0k_E_004612_004638, start_frame: 276385, end_frame: 278124, expected num_frames: 870, got: 1739, last event frame: 823
fixing yj0pNXcTK0k_E_004933_004965, start_frame: 295606, end_frame: 297745, expected num_frames: 1070, got: 2139, last event frame: 1017
fixing yj0pNXcTK0k_E_005170_005205, start_frame: 309867, end_frame: 312088, expected num_frames: 1111, got: 2221, last event frame: 1073
fixing yj0pNXcTK0k_E_005475_005512, start_frame: 328086, end_frame: 330467, expected num_frames: 1191, got: 2381, last event frame: 1158
fixing yj0pNXcTK0k_E_005757_005795, start_frame: 344985, end_frame: 347450, expected num_frames: 1233, got: 2465, last event frame: 1187
fixing yj0pNXcTK0k_E_006065_006093, start_frame: 363470, end_frame: 365311, expected num_frames: 921, got: 1841, last event frame: 883
fixing 26Y8BsNiiL8_E_000043_000052, start_frame: 2505, end_frame: 3229, expected num_frames: 362, got: 724, last event frame: 322
fixing 26Y8BsNiiL8_E_000259_000296, start_frame: 15453, end_frame: 17903, expected num_frames: 1225, got: 2450, last event frame: 1164
fixing 26Y8BsNiiL8_E_000399_000436, start_frame: 23836, end_frame: 26258, expected num_frames: 1211, got: 2422, last event frame: 1151
fixing 26Y8BsNiiL8_E_000472_000480, start_frame: 28223, end_frame: 28925, expected num_frames: 351, got: 702, last event frame: 291
fixing 26Y8BsNiiL8_E_000598_000643, start_frame: 35766, end_frame: 38652, expected num_frames: 1443, got: 2886, last event frame: 1388
fixing 26Y8BsNiiL8_E_000665_000698, start_frame: 39760, end_frame: 41948, expected num_frames: 1094, got: 2188, last event frame: 1058
fixing 26Y8BsNiiL8_E_000737_000829, start_frame: 44137, end_frame: 49831, expected num_frames: 2847, got: 5694, last event frame: 2798
fixing 26Y8BsNiiL8_E_000966_001042, start_frame: 57831, end_frame: 62617, expected num_frames: 2393, got: 4786, last event frame: 2334
fixing 26Y8BsNiiL8_E_001162_001259, start_frame: 69611, end_frame: 75568, expected num_frames: 2979, got: 5957, last event frame: 2927
fixing 26Y8BsNiiL8_E_001308_001401, start_frame: 78332, end_frame: 84099, expected num_frames: 2884, got: 5767, last event frame: 2846
fixing 26Y8BsNiiL8_E_001465_001561, start_frame: 87760, end_frame: 93714, expected num_frames: 2977, got: 5954, last event frame: 2877
fixing 26Y8BsNiiL8_E_001643_001683, start_frame: 98447, end_frame: 101021, expected num_frames: 1287, got: 2574, last event frame: 1234
fixing 26Y8BsNiiL8_E_002137_002175, start_frame: 128017, end_frame: 130479, expected num_frames: 1231, got: 2462, last event frame: 1188
fixing 26Y8BsNiiL8_E_002592_002698, start_frame: 155282, end_frame: 161800, expected num_frames: 3259, got: 6518, last event frame: 3083
fixing 26Y8BsNiiL8_E_002729_002821, start_frame: 163521, end_frame: 169226, expected num_frames: 2853, got: 5705, last event frame: 2789
fixing 26Y8BsNiiL8_E_002894_002990, start_frame: 173412, end_frame: 179323, expected num_frames: 2956, got: 5911, last event frame: 2889
fixing 26Y8BsNiiL8_E_003049_003139, start_frame: 182673, end_frame: 188285, expected num_frames: 2806, got: 5612, last event frame: 2758
fixing 26Y8BsNiiL8_E_003168_003270, start_frame: 189853, end_frame: 196117, expected num_frames: 3132, got: 6264, last event frame: 2779
fixing 26Y8BsNiiL8_E_003354_003449, start_frame: 200974, end_frame: 206863, expected num_frames: 2945, got: 5889, last event frame: 2886
fixing 26Y8BsNiiL8_E_003680_003689, start_frame: 220510, end_frame: 221240, expected num_frames: 365, got: 730, last event frame: 294
fixing 26Y8BsNiiL8_E_003742_003751, start_frame: 224280, end_frame: 224961, expected num_frames: 341, got: 681, last event frame: 280
fixing 26Y8BsNiiL8_E_003841_003849, start_frame: 230117, end_frame: 230816, expected num_frames: 350, got: 699, last event frame: 314
fixing 26Y8BsNiiL8_E_003943_003950, start_frame: 236244, end_frame: 236883, expected num_frames: 320, got: 639, last event frame: 264
fixing 26Y8BsNiiL8_E_003978_004077, start_frame: 238354, end_frame: 244466, expected num_frames: 3056, got: 6112, last event frame: 2929
fixing 26Y8BsNiiL8_E_004202_004210, start_frame: 251787, end_frame: 252444, expected num_frames: 329, got: 657, last event frame: 275
fixing 26Y8BsNiiL8_E_004203_004210, start_frame: 251855, end_frame: 252439, expected num_frames: 292, got: 584, last event frame: 241
fixing 26Y8BsNiiL8_E_004232_004334, start_frame: 253627, end_frame: 259857, expected num_frames: 3115, got: 6230, last event frame: 2876
fixing 26Y8BsNiiL8_E_004389_004397, start_frame: 263047, end_frame: 263686, expected num_frames: 320, got: 639, last event frame: 257
fixing iSQqsVFkQAA_E_001454_001460, start_frame: 72651, end_frame: 73106, expected num_frames: 228, got: 455, last event frame: 179
fixing iSQqsVFkQAA_E_001635_001642, start_frame: 81722, end_frame: 82207, expected num_frames: 243, got: 485, last event frame: 206
fixing iSQqsVFkQAA_E_001902_001909, start_frame: 95052, end_frame: 95577, expected num_frames: 263, got: 525, last event frame: 214
fixing iSQqsVFkQAA_E_002016_002023, start_frame: 100787, end_frame: 101279, expected num_frames: 246, got: 492, last event frame: 195
fixing iSQqsVFkQAA_E_002220_002226, start_frame: 110952, end_frame: 111417, expected num_frames: 233, got: 465, last event frame: 188
fixing iSQqsVFkQAA_E_002304_002312, start_frame: 115186, end_frame: 115725, expected num_frames: 270, got: 539, last event frame: 218
fixing iSQqsVFkQAA_E_002672_002678, start_frame: 133543, end_frame: 134019, expected num_frames: 238, got: 476, last event frame: 193
fixing iSQqsVFkQAA_E_002748_002754, start_frame: 137379, end_frame: 137833, expected num_frames: 227, got: 454, last event frame: 180
fixing iSQqsVFkQAA_E_002949_002955, start_frame: 147388, end_frame: 147873, expected num_frames: 243, got: 485, last event frame: 194
fixing iSQqsVFkQAA_E_003031_003038, start_frame: 151498, end_frame: 152030, expected num_frames: 266, got: 532, last event frame: 218
fixing iSQqsVFkQAA_E_003125_003130, start_frame: 156194, end_frame: 156620, expected num_frames: 213, got: 426, last event frame: 175
fixing iSQqsVFkQAA_E_003203_003209, start_frame: 160106, end_frame: 160536, expected num_frames: 215, got: 430, last event frame: 173
fixing iSQqsVFkQAA_E_003296_003303, start_frame: 164720, end_frame: 165230, expected num_frames: 255, got: 510, last event frame: 213
fixing iSQqsVFkQAA_E_003372_003379, start_frame: 168595, end_frame: 169067, expected num_frames: 236, got: 472, last event frame: 186
fixing iSQqsVFkQAA_E_007695_007740, start_frame: 384695, end_frame: 387119, expected num_frames: 1212, got: 2424, last event frame: 1173
fixing iSQqsVFkQAA_E_007926_007962, start_frame: 396261, end_frame: 398197, expected num_frames: 968, got: 1936, last event frame: 930
fixing iSQqsVFkQAA_E_008274_008306, start_frame: 413652, end_frame: 415393, expected num_frames: 871, got: 1741, last event frame: 830
fixing iSQqsVFkQAA_E_008460_008535, start_frame: 422977, end_frame: 426827, expected num_frames: 1925, got: 3850, last event frame: 1895
fixing iSQqsVFkQAA_E_008694_008719, start_frame: 434669, end_frame: 436065, expected num_frames: 698, got: 1396, last event frame: 654
fixing iSQqsVFkQAA_E_008894_008941, start_frame: 444676, end_frame: 447152, expected num_frames: 1238, got: 2476, last event frame: 1189
fixing iSQqsVFkQAA_E_009127_009164, start_frame: 456318, end_frame: 458303, expected num_frames: 993, got: 1985, last event frame: 948
fixing iSQqsVFkQAA_E_009333_009363, start_frame: 466617, end_frame: 468227, expected num_frames: 805, got: 1610, last event frame: 777
fixing qfBalcxF8JY_E_000186_000192, start_frame: 9209, end_frame: 9690, expected num_frames: 241, got: 481, last event frame: 201
fixing qfBalcxF8JY_E_000250_000260, start_frame: 12404, end_frame: 13091, expected num_frames: 344, got: 687, last event frame: 221
fixing qfBalcxF8JY_E_000357_000363, start_frame: 17772, end_frame: 18274, expected num_frames: 251, got: 502, last event frame: 212
fixing qfBalcxF8JY_E_000451_000459, start_frame: 22506, end_frame: 23020, expected num_frames: 257, got: 514, last event frame: 224
fixing qfBalcxF8JY_E_000547_000553, start_frame: 27313, end_frame: 27757, expected num_frames: 222, got: 444, last event frame: 192
fixing qfBalcxF8JY_E_000641_000648, start_frame: 32026, end_frame: 32502, expected num_frames: 238, got: 476, last event frame: 205
fixing qfBalcxF8JY_E_000733_000740, start_frame: 36571, end_frame: 37094, expected num_frames: 262, got: 523, last event frame: 228
fixing qfBalcxF8JY_E_001026_001032, start_frame: 51203, end_frame: 51699, expected num_frames: 248, got: 496, last event frame: 202
fixing qfBalcxF8JY_E_001112_001119, start_frame: 55557, end_frame: 56048, expected num_frames: 246, got: 491, last event frame: 186
fixing qfBalcxF8JY_E_001199_001206, start_frame: 59897, end_frame: 60392, expected num_frames: 248, got: 495, last event frame: 209
fixing qfBalcxF8JY_E_001753_001789, start_frame: 87595, end_frame: 89541, expected num_frames: 973, got: 1946, last event frame: 939
fixing qfBalcxF8JY_E_001919_001958, start_frame: 95892, end_frame: 97998, expected num_frames: 1053, got: 2106, last event frame: 1006
fixing qfBalcxF8JY_E_002136_002169, start_frame: 106791, end_frame: 108523, expected num_frames: 866, got: 1732, last event frame: 832
fixing qfBalcxF8JY_E_002353_002397, start_frame: 117591, end_frame: 119967, expected num_frames: 1188, got: 2376, last event frame: 1147
fixing qfBalcxF8JY_E_002522_002563, start_frame: 126016, end_frame: 128243, expected num_frames: 1114, got: 2227, last event frame: 1071
fixing qfBalcxF8JY_E_002791_002822, start_frame: 139499, end_frame: 141153, expected num_frames: 827, got: 1654, last event frame: 801
fixing qfBalcxF8JY_E_002880_002919, start_frame: 143988, end_frame: 146057, expected num_frames: 1035, got: 2069, last event frame: 993
fixing qfBalcxF8JY_E_003070_003099, start_frame: 153472, end_frame: 155071, expected num_frames: 800, got: 1599, last event frame: 751
fixing qfBalcxF8JY_E_003203_003237, start_frame: 160114, end_frame: 161952, expected num_frames: 919, got: 1838, last event frame: 891
fixing qfBalcxF8JY_E_003351_003380, start_frame: 167516, end_frame: 169105, expected num_frames: 795, got: 1589, last event frame: 753
fixing qfBalcxF8JY_E_003941_004027, start_frame: 196993, end_frame: 201434, expected num_frames: 2221, got: 4441, last event frame: 2187
fixing qfBalcxF8JY_E_004395_004483, start_frame: 219737, end_frame: 224234, expected num_frames: 2249, got: 4497, last event frame: 2207
fixing qfBalcxF8JY_E_004622_004711, start_frame: 231029, end_frame: 235624, expected num_frames: 2298, got: 4595, last event frame: 2249
fixing qfBalcxF8JY_E_004925_005011, start_frame: 246171, end_frame: 250639, expected num_frames: 2234, got: 4468, last event frame: 2172
fixing qfBalcxF8JY_E_005164_005271, start_frame: 258160, end_frame: 263646, expected num_frames: 2743, got: 5486, last event frame: 2706
fixing qfBalcxF8JY_E_005588_005677, start_frame: 279345, end_frame: 283921, expected num_frames: 2288, got: 4576, last event frame: 2223
fixing qfBalcxF8JY_E_006224_006328, start_frame: 311169, end_frame: 316475, expected num_frames: 2653, got: 5306, last event frame: 2410
fixing qfBalcxF8JY_E_006464_006567, start_frame: 323143, end_frame: 328409, expected num_frames: 2633, got: 5266, last event frame: 2385
fixing qfBalcxF8JY_E_006693_006798, start_frame: 334626, end_frame: 339978, expected num_frames: 2676, got: 5352, last event frame: 2491
fixing qfBalcxF8JY_E_006902_007010, start_frame: 345093, end_frame: 350594, expected num_frames: 2751, got: 5501, last event frame: 2565
fixing qfBalcxF8JY_E_007358_007460, start_frame: 367830, end_frame: 373078, expected num_frames: 2624, got: 5248, last event frame: 2347
fixing qfBalcxF8JY_E_007555_007659, start_frame: 377694, end_frame: 383049, expected num_frames: 2678, got: 5355, last event frame: 2389
```
## Example of SSD300 decoded by bm-ffmpeg, preprocessed by bmcv, inference by sail.

## Usage:

* Deploy on SOC mode.

```shell
make -f Makefile.arm

# bmodel: bmodel path, can be fp32 or int8 model
# input:  input path, can be image/video file or rtsp stream
# loops:  frames count to be detected, default: 1
./ssd300_ffmpeg_bmcv_sail.arm \
    --bmodel your-path-to-bmodel \
    --input your-path-to-input \
    --loops frames_count_to_detect
```

* Deploy on PCIE mode.

```shell
make -f Makefile.pcie

# bmodel: bmodel path, can be fp32 or int8 model
# input:  input path, can be image/video file or rtsp stream
# loops:  frames count to be detected, default: 1
./ssd300_ffmpeg_bmcv_sail.pcie \
    --bmodel your-path-to-bmodel \
    --input your-path-to-input \
    --loops frames_count_to_detect
```

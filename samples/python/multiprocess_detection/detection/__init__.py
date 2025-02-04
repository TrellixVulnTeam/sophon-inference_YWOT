# -*- coding:utf-8 -*-
# @author  : cbingcan
# @time    : 2021/8/24/024 11:00
SERVER_PORT= 8080

DETECTION_PROCESS_NUM = 4
PREDICT_PROCESS_NUM = 1

DETECTION_MODEL_PATH = 'models/'
DETECTION_MODEL_PATH = 'models/retina-ssh-b4-int8.bmodel'
PREDICT_MODEL_PATH = 'models/face_v3_int8.bmodel'
input_img_h = 450
input_img_w = 800
DETECTION_TPU_ID = 0
PREDICT_TPU_ID = 0

VIDEO_LIST = [
    {"id": "35050000002000001365", "name": "3#楼北面监控2", "rtsp": "rtsp://192.168.60.178/rtp/gb_play_35050000002000000107_34020000001320000001"},
    {"id": "35050000002000001367", "name": "3#楼北面监控4", "rtsp": "rtsp://192.168.60.178/rtp/gb_play_35050000002000000115_34020000001320000001"},
    {"id": "35050000002000001364", "name": "3#楼北面监控1", "rtsp": "rtsp://192.168.60.178/rtp/gb_play_35050000002000000127_34020000001320000001"},
    {"id": "35050000002000001366", "name": "3#楼北面监控3", "rtsp": "rtsp://192.168.60.178/rtp/gb_play_35050000002000000105_34020000001320000001"},
    {"id": "35050000002000001368", "name": "3#楼北面监控5", "rtsp": "rtsp://192.168.60.178/rtp/gb_play_35050000002000000119_34020000001320000001"},
    {"id": "35050000002000013106", "name": "2#6F中办公区往西", "rtsp": "rtsp://192.168.60.178/rtp/gb_play_35050000002000000114_34020000001320000001"},
    {"id": "35050000002000000012", "name": "一层电梯间", "rtsp": "rtsp://192.168.60.178/rtp/gb_play_35050000002000000103_34020000001320000001"},
    {"id": "35050000002000013104", "name": "2#6F西办公区", "rtsp": "rtsp://192.168.60.178/rtp/gb_play_35050000002000000128_34020000001320000001"},
    {"id": "35050000002000013105", "name": "2#6F东办公区", "rtsp": "rtsp://192.168.60.178/rtp/gb_play_35050000002000000126_34020000001320000001"},
    {"id": "35050000002000013105", "name": "2#6F东办公区", "rtsp": "rtsp://192.168.60.178/rtp/gb_play_35050000002000000110_34020000001320000001"},
    {"id": "35050000002000013105", "name": "2#6F东办公区", "rtsp": "rtsp://wd:Aa123456@192.168.6.171:554/ch2/main/av_stream"},
    {"id": "35050000002000013105", "name": "2#6F东办公区", "rtsp": "rtsp://wd:Aa123456@192.168.6.172:554/ch2/main/av_stream"},
]

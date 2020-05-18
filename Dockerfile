FROM docker-registry.vnpttiengiang.vn/cms/yolov3:2019.12.04

WORKDIR /app

COPY . /app

ENV YOLO_DATA_CFG models/origin/coco.data
ENV YOLO_CFG_FILE models/origin/yolov3.cfg
ENV YOLO_WEIGHTS_FILE models/origin/yolov3.weights
ENV RATE_REQUEST_PER_SECOND 100
ENV RATE_BURST_NUM 1000


CMD = ["/app/http"]
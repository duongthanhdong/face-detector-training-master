# coding: utf-8

import cv2
import io
import logging
import random
import requests
import time


LOGGER = logging.getLogger(__name__)


def letterbox_resize(img, new_width, new_height, interp=0):
    '''
    Letterbox resize. keep the original aspect ratio in the resized image.
    '''
    ori_height, ori_width = img.shape[:2]

    resize_ratio = min(new_width / ori_width, new_height / ori_height)

    resize_w = int(resize_ratio * ori_width)
    resize_h = int(resize_ratio * ori_height)

    img = cv2.resize(img, (resize_w, resize_h), interpolation=interp)
    image_padded = np.full((new_height, new_width, 3), 128, np.uint8)

    dw = int((new_width - resize_w) / 2)
    dh = int((new_height - resize_h) / 2)

    image_padded[dh: resize_h + dh, dw: resize_w + dw, :] = img

    return image_padded, resize_ratio, dw, dh


class YoloObjectDetector:

    def __init__(self, detector_url, size=(416, 416), letterbox=False, timeout=5, *args, **kwargs):
        self.__server_url = detector_url
        self.__timeout = timeout
        self.__letterbox = letterbox
        self.__size = size
        self.__kwargs = kwargs

    def detect(self, img_ori):
        if self.__letterbox:
            img, resize_ratio, dw, dh = letterbox_resize(img_ori, *self.__size)
        else:
            height_ori, width_ori = img_ori.shape[:2]
            img = cv2.resize(img_ori, self.__size)

        ret, buf = cv2.imencode('.jpg', img)
        fi = io.BytesIO(buf)
        files = {'file': fi}

        try:
            headers = {}
            if 'headers' in self.__kwargs:
                headers = self.__kwargs['headers']
            r = requests.post(self.__server_url, files=files, timeout=self.__timeout, headers=headers)

            if r.status_code == 200:
                objs = r.json() or []
                # if self.__letterbox:
                #     for obj in objs:
                #         # TODO
                return objs
            else:
                return []
        except requests.Timeout:
            # back off and retry
            LOGGER.warning('Connection timeout [{}]'.format(self.__server_url))
            return []
        except requests.ConnectionError:
            LOGGER.warning('Connection error [{}]'.format(self.__server_url))
            return []


if __name__ == '__main__':
    yolo = YoloObjectDetector('http://192.168.1.45:8080/detect')
    img = cv2.imread('AVATAR_HSzdGqQuw.jpg')
    vw = img.shape[1]
    vh = img.shape[0]
    #img = cv2.imread('demo/tgg.jpg')

    start = time.time()
    objs = yolo.detect(img)
    duration_ms = (time.time() - start) * 1000
    print('Duration: {} ms'.format(duration_ms))
    # print(objs)
    for obj in objs:
        bbox = obj['bbox']
        x = int(bbox[0] * vw)
        y = int(bbox[1] * vh)
        w = int(bbox[2] * vw)
        h = int(bbox[3] * vh)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.imwrite('result.jpg', img[y:y + h, x:x + w])
    cv2.imshow('frame', img)
    key = cv2.waitKey(0)

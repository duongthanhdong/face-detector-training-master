# coding: utf-8

import cv2
import io
import requests
import time
import numpy as np
import pickle
import json


def face_distance(face_encodings, face_to_compare):
    if len(face_encodings) == 0:
        return np.empty((0))
    #dist = np.sum(np.square(face_encodings-face_to_compare))
    return np.linalg.norm(face_encodings - face_to_compare, axis=1)
    # return dist


def compare_faces(known_face_encodings, face_encoding_to_check, tolerance=1):
    return list(face_distance(known_face_encodings, face_encoding_to_check) <= tolerance)
if __name__ == '__main__':
    data = pickle.loads(open('cam16.pickle', "rb").read())
    img_ori = cv2.imread('test.jpg')
    size = (112, 112)
    while 1:
        height_ori, width_ori = img_ori.shape[:2]
        img = cv2.resize(img_ori, size)
        ret, buf = cv2.imencode('.jpg', img)
        fi = io.BytesIO(buf)
        files = {'file': fi}
        timestart = time.time()
        test = requests.post('http://192.168.1.45:5000/embedding', files=files)
        timeend = time.time()

        # print(test.content)
        results = json.loads(test.content.decode("utf-8"))
        emb_data = np.array(results['result'])
        emb = emb_data.astype(np.float)
        # print(data["encodings"])
        # print(emb)
        name = "un"
        matches = compare_faces(np.array(data["encodings"]), emb)
        if True in matches:
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}
            for i in matchedIdxs:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1
            name = max(counts, key=counts.get)
        print(str(name))
        print(timeend - timestart)


# class YoloObjectDetector:
#     def __init__(self, detector_url, size=(416, 416), letterbox=False, timeout=5, *args, **kwargs):
#         self.__server_url = detector_url
#         self.__timeout = timeout
#         self.__letterbox = letterbox
#         self.__size = size
#         self.__kwargs = kwargs

#     def detect(self, img_ori):
#         if self.__letterbox:
#             img, resize_ratio, dw, dh = letterbox_resize(img_ori, *self.__size)
#         else:
#             height_ori, width_ori = img_ori.shape[:2]
#             img = cv2.resize(img_ori, self.__size)

#         ret, buf = cv2.imencode('.jpg', img)
#         fi = io.BytesIO(buf)
#         files = {'file': fi}

#         try:
#             headers = {}
#             if 'headers' in self.__kwargs:
#                 headers = self.__kwargs['headers']
#             r = requests.post(self.__server_url, files=files, timeout=self.__timeout, headers=headers)

#             if r.status_code == 200:
#                 objs = r.json() or []
#                 # if self.__letterbox:
#                 #     for obj in objs:
#                 #         # TODO
#                 return objs
#             else:
#                 return []
#         except requests.Timeout:
#             # back off and retry
#             LOGGER.warning('Connection timeout [{}]'.format(self.__server_url))
#             return []
#         except requests.ConnectionError:
#             LOGGER.warning('Connection error [{}]'.format(self.__server_url))
#             return []


# class FakeObjectDetector:
#     def __init__(self, *args, **kwargs):
#         pass

#     def detect(img):
#         have_detected_objs = random.randint(0, 100)
#         objs = []
#         if have_detected_objs == 1:
#             objs = [
#                 {
#                     'name': random.choice(VEHICLE_OBJS),
#                     'prob': 0.98,
#                     'bbox': [0.1, 0.1, 0.2, 0.2]
#                 },
#                 {
#                     'name': random.choice(VEHICLE_OBJS),
#                     'prob': 0.8,
#                     'bbox': [0.1, 0.1, 0.2, 0.2]
#                 }
#             ]

#         return objs

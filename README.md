# go-detector

### How to build
- Rename to yolov3.weights
- Build by docker command
```
docker build -f Dockerfile -t godetector:latest .
```
- Build by docker-compose command

### Build custom model
- Create another folder in folder `models`
- Create the same structure as orign Note: `make sure path is correct`
- Update Dockerfile to have correct ENV to new model
- Optional: Update Dockerfile to copy correct folder

### How to start docker serving for yolo model
- Run with docker command
```
docker run --runtime=nvidia -it -p 8080:8080 docker-registry.vnpttiengiang.vn/cms/yolov3:2019.12.04 /app/http
```

- Run by docker-compose command (Recommend)
```
docker-compose up
```

### Run test with client
```
➜  go-detector git:(master) ✗ python tools/yolo_client.py 
```

- Example output: bbox=[x, y, w, h]
```
[
  {
    "name": "motorbike",
    "id": 3,
    "bbox": [
      0.55043197,
      0.06635375,
      0.061476655,
      0.11651498
    ],
    "prob": 0.938211
  },
  {
    "name": "motorbike",
    "id": 3,
    "bbox": [
      0.10583589,
      0.4478267,
      0.08669074,
      0.19666366
    ],
    "prob": 0.9268994
  },
  {
    "name": "motorbike",
    "id": 3,
    "bbox": [
      0.74587643,
      0.17543647,
      0.059662346,
      0.16477545
    ],
    "prob": 0.6068728
  },
  {
    "name": "motorbike",
    "id": 3,
    "bbox": [
      0.83443004,
      0.789707,
      0.076767825,
      0.20607208
    ],
    "prob": 0.5869981
  },
  {
    "name": "car",
    "id": 2,
    "bbox": [
      0.2937834,
      0.12527406,
      0.25180393,
      0.314896
    ],
    "prob": 0.99356365
  },
  {
    "name": "car",
    "id": 2,
    "bbox": [
      -0.0051093996,
      0.6000236,
      0.18646125,
      0.3974924
    ],
    "prob": 0.82075787
  },
  {
    "name": "person",
    "id": 0,
    "bbox": [
      0.074581906,
      0.24870567,
      0.1024301,
      0.32656124
    ],
    "prob": 0.9961121
  },
  {
    "name": "person",
    "id": 0,
    "bbox": [
      0.8070243,
      0.017672993,
      0.04635683,
      0.23224281
    ],
    "prob": 0.9740752
  },
  {
    "name": "person",
    "id": 0,
    "bbox": [
      0.7416602,
      0.07376073,
      0.06476023,
      0.25476617
    ],
    "prob": 0.93546075
  },
  {
    "name": "person",
    "id": 0,
    "bbox": [
      0.7317816,
      0.014906965,
      0.05252336,
      0.16388789
    ],
    "prob": 0.92972416
  },
  {
    "name": "person",
    "id": 0,
    "bbox": [
      0.54896915,
      0.020767152,
      0.06455297,
      0.13882472
    ],
    "prob": 0.90941733
  },
  {
    "name": "person",
    "id": 0,
    "bbox": [
      0.84387743,
      0.51137626,
      0.035839655,
      0.071048446
    ],
    "prob": 0.81037015
  }
]
```
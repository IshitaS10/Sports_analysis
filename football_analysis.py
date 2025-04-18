# -*- coding: utf-8 -*-

!pip install ultralytics
!pip install roboflow

!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="Q0ClGmgxGg8H57MxqMGx")
project = rf.workspace("roboflow-jvuqo").project("football-players-detection-3zvbc")
version = project.version(1)
dataset = version.download("yolov5")

dataset.location

import shutil

shutil.move('football-players-detection-1/train',
            'football-players-detection-1/football-players-detection-1/train'
            )

shutil.move('football-players-detection-1/test',
            'football-players-detection-1/football-players-detection-1/test'
            )

shutil.move('football-players-detection-1/valid',
            'football-players-detection-1/football-players-detection-1/valid'
            )



!yolo task=detect mode=train model=yolov5l.pt data={dataset.location}/data.yaml epochs=10 imgsz=640


import torch

def generate(image):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

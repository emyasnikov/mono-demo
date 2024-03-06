import torch

device = 'cuda' if torch.cuda.is_available() else 'cpu'

def generate(image):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True).to(device)

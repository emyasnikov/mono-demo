import torch

device = 'cuda' if torch.cuda.is_available() else 'cpu'

def generate(image):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True).to(device)

    objects = model(image).pandas().xyxy[0].to_dict(orient='records')

    output = {}

    for obj in objects:
        if obj['name'] not in output:
            output[obj['name']] = 1
        else:
            output[obj['name']] += 1

    return output

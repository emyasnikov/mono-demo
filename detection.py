import torch

device = 'cuda' if torch.cuda.is_available() else 'cpu'

def generate(image):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True).to(device)

    objects = model(image).pandas().xyxy[0].to_dict(orient='records')

    count = {}

    for obj in objects:
        if obj['name'] not in count:
            count[obj['name']] = 1
        else:
            count[obj['name']] += 1

    output = []

    for key, value in count.items():
        output.append({
            'label': key,
            'count': value,
        })

    return output

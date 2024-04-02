import torch
import translation
from PIL import Image

device = 'cuda' if torch.cuda.is_available() else 'cpu'

def generate(image, type=None):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True).to(device)
    results = model(image)

    if type == 'array' or type == 'json':
        objects = results.pandas().xyxy[0].to_dict(orient='records')

        count = {}

        for obj in objects:
            if obj['name'] not in count:
                count[obj['name']] = 1
            else:
                count[obj['name']] += 1

        output = []

        if type == 'array':
            for key, value in count.items():
                output.append([translation.translate(key), value])

            return output

        for key, value in count.items():
            output.append({
                'label': translation.translate(key),
                'count': value,
            })

        return output

    image_array = results.render()[0]
    pil_image = Image.fromarray(image_array)

    return pil_image

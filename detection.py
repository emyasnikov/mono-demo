import torch
import translation
from PIL import Image

device = 'cuda' if torch.cuda.is_available() else 'cpu'

def generate(image, api=False):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True).to(device)
    results = model(image)

    if api:
        objects = results.pandas().xyxy[0].to_dict(orient='records')

        count = {}

        for obj in objects:
            if obj['name'] not in count:
                count[obj['name']] = 1
            else:
                count[obj['name']] += 1

        output = []

        for key, value in count.items():
            output.append({
                'label': translation.translate(key),
                'count': value,
            })

        return output

    image_array = results.render()[0]
    pil_image = Image.fromarray(image_array)

    return pil_image

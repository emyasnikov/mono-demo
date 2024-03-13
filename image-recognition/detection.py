import translation
from PIL import Image
from ultralytics import YOLO

def generate(image, type=None):
    model = YOLO('yolov8n')

    results = model.predict(
        source=image,
        conf=0.25,
        iou=0.45,
        show_labels=True,
        show_conf=True,
        imgsz=640,
    )

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

    for r in results:
        image_array = r.plot()
        pil_image = Image.fromarray(image_array[..., ::-1])

    return pil_image

import gradio as gr
import torch
from PIL import Image
from ultralytics import YOLO

device = 'cuda' if torch.cuda.is_available() else 'cpu'

def predict(model_name, image):
    model = YOLO(model_name).to(device)
    results = model.predict(image)
    show_boxes = '-seg' not in model_name

    for r in results:
        image_array = r.plot(boxes=show_boxes)
        pil_image = Image.fromarray(image_array[..., ::-1])

    return pil_image

demo = gr.Interface(
    allow_flagging=False,
    css='footer {visibility: hidden}',
    fn=predict,
    inputs=[
        gr.Dropdown(
            choices=[
                ('Detection', 'yolov8n.pt'),
                ('Orientation', 'yolov8n-obb.pt'),
                ('Segmentation', 'yolov8n-seg.pt'),
            ],
            label='Model',
            value='yolov8n.pt',
        ),
        gr.Image(type='pil', label='Input Image'),
    ],
    outputs=gr.Image(type='pil', label='Output Image'),
)

if __name__ == '__main__':
    demo.queue().launch()

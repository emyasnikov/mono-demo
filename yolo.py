import gradio as gr
import torch
from PIL import Image
from ultralytics import YOLO

device = 'cuda' if torch.cuda.is_available() else 'cpu'

def predict(image, model_name, show_boxes):
    model = YOLO(model_name).to(device)
    results = model.predict(image)

    for r in results:
        image_array = r.plot(boxes=show_boxes)
        pil_image = Image.fromarray(image_array[..., ::-1])

    return pil_image

demo = gr.Interface(
    allow_flagging=False,
    css='footer {visibility: hidden}',
    examples=[
        ['data/detection.jpg', 'yolov8n.pt', True],
        ['data/orientation.jpg', 'yolov8n-obb.pt', True],
        ['data/pose.jpg', 'yolov8n-pose.pt', False],
        ['data/segmentation.jpg', 'yolov8n-seg.pt', False],
    ],
    fn=predict,
    inputs=[
        gr.Image(type='pil', label='Input Image'),
        gr.Dropdown(
            choices=[
                ('Detection', 'yolov8n.pt'),
                ('Orientation', 'yolov8n-obb.pt'),
                ('Pose', 'yolov8n-pose.pt'),
                ('Segmentation', 'yolov8n-seg.pt'),
            ],
            label='Model',
            value='yolov8n.pt',
        ),
        gr.Checkbox(label='Show Boxes', value=True),
    ],
    outputs=gr.Image(type='pil', label='Output Image'),
)

if __name__ == '__main__':
    demo.queue().launch(root_path='/yolo')

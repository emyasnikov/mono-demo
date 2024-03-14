import gradio as gr
from PIL import Image
from ultralytics import YOLO

def predict(model_name, image):
    model = YOLO(model_name)
    results = model.predict(image)
    show_boxes = model_name == 'yolov8n.pt'

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

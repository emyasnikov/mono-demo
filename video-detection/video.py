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
    fn=predict,
    inputs=gr.Image(type='pil', label='Input Image'),
    outputs=gr.Image(type='pil', label='Output Image'),
)

if __name__ == '__main__':
    demo.queue().launch(root_path='/video')

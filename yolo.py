import gradio as gr
from PIL import Image
from ultralytics import YOLO

def predict(image):
    model = YOLO('yolov8n.pt')
    results = model.predict(image)

    for r in results:
        image_array = r.plot()
        pil_image = Image.fromarray(image_array[..., ::-1])

    return pil_image

demo = gr.Interface(
    allow_flagging=False,
    fn=predict,
    inputs=gr.Image(type='pil', label='Input Image'),
    outputs=gr.Image(type='pil', label='Output Image'),
)

if __name__ == '__main__':
    demo.launch()

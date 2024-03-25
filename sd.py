import gradio as gr
import torch
from diffusers import DiffusionPipeline

dtype = torch.float16 if torch.cuda.is_available() else torch.float32

def generate(prompt):
    pipeline = DiffusionPipeline.from_pretrained('segmind/small-sd', torch_dtype=dtype)
    image = pipeline(prompt).images[0]

    return image

demo = gr.Interface(
    fn=generate,
    inputs=gr.Textbox(lines=8, label="Input Text"),
    outputs=gr.Image(label="Output Image"),
)

if __name__ == '__main__':
    demo.launch()

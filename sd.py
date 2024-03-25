import gradio as gr
import torch
from diffusers import DiffusionPipeline

dtype = torch.float16 if torch.cuda.is_available() else torch.float32

def generate(model, prompt):
    pipeline = DiffusionPipeline.from_pretrained(model, torch_dtype=dtype)
    image = pipeline(prompt).images[0]

    return image

demo = gr.Interface(
    allow_flagging=False,
    css='footer {visibility: hidden}',
    fn=generate,
    inputs=[
        gr.Dropdown(
            choices=[
                ('Small', 'segmind/small-sd'),
                ('Tiny', 'segmind/tiny-sd'),
            ],
            label='Model',
            value='segmind/small-sd',
        ),
        gr.Textbox(lines=4, label="Input Text"),
    ],
    outputs=gr.Image(label="Output Image"),
    title='Stable Diffusion Demo',
)

if __name__ == '__main__':
    demo.queue().launch(root_path='/sd')

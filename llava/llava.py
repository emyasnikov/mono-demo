import gradio as gr
import ollama

def generate(image, prompt):
    model='llava:7b-v1.6-mistral-q4_0'

    for result in ollama.generate(model, prompt, images=[image], stream=False):
        return result

demo = gr.Interface(
    fn=generate,
    inputs=[
        gr.Image(type='filepath', label='Image'),
        gr.Textbox(label='Prompt'),
    ],
    outputs=gr.Textbox(label='Output', lines=10),
)

if __name__ == '__main__':
    demo.launch()

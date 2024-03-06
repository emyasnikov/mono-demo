import captioning
import classification
import detection
import gradio as gr
import json

def predict(input):
    results = {
        'captioning': captioning.generate(input),
        'classification': classification.generate(input),
        'detection': detection.generate(input),
    }

    return json.dumps(results, indent=2)

demo = gr.Interface(
    css='footer {visibility: hidden}',
    fn=predict,
    inputs=gr.Image(type='pil'),
    outputs=gr.Textbox(label='Preview', lines=10),
    title='Image Recognition Demo',
)

if __name__ == "__main__":
    demo.launch(root_path='/demo')

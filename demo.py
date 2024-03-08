import captioning
import classification
import config
import detection
import gradio as gr
import json

def predict_analyze(type, input):
    output = None

    if type == 'Captioning':
        output = captioning.generate(input)
    elif type == 'Classification':
        output = classification.generate(input)
    elif type == 'Detection':
        output = detection.generate(input)

    return output


def predict_api(input):
    results = {
        'captioning': captioning.generate(input),
        'classification': classification.generate(input),
        'detection': detection.generate(input),
    }

    return json.dumps(results, indent=2)

demo_analyze = gr.Interface(
    allow_flagging=False,
    css='footer {visibility: hidden}',
    fn=predict_analyze,
    inputs=[
        gr.Dropdown(label='Select', choices=['Captioning', 'Classification', 'Detection'], value='Captioning'),
        gr.Image(type='pil', label='Image'),
    ],
    outputs=gr.Textbox(label='Output', lines=10),
    title=config.get('APP_TITLE'),
)

demo_api = gr.Interface(
    allow_flagging=False,
    css='footer {visibility: hidden}',
    fn=predict_api,
    inputs=gr.Image(type='pil', label='Image'),
    outputs=gr.Textbox(label='Output', lines=10),
    title=config.get('APP_TITLE'),
)

demo = gr.TabbedInterface([
    demo_analyze,
    demo_api,
], [
    'Analyze',
    'API',
])

if __name__ == "__main__":
    demo.queue().launch(root_path='/demo')

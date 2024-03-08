import captioning
import classification
import config
import detection
import gradio as gr
import json


def predict_captioning(input):
    return captioning.generate(input)

def predict_classification(input):
    return classification.generate(input)

def predict_detection(input):
    return detection.generate(input)

def predict_api(input):
    results = {
        'captioning': captioning.generate(input),
        'classification': classification.generate(input),
        'detection': detection.generate(input),
    }

    return json.dumps(results, indent=2)

demo_captioning = gr.Interface(
    allow_flagging=False,
    fn=predict_captioning,
    inputs=gr.Image(type='pil', label='Image'),
    outputs=gr.Textbox(label='Output', lines=10),
    title=config.get('APP_TITLE'),
)

demo_classification = gr.Interface(
    allow_flagging=False,
    fn=predict_classification,
    inputs=gr.Image(type='pil', label='Image'),
    outputs=gr.Textbox(label='Output', lines=10),
    title=config.get('APP_TITLE'),
)

demo_detection = gr.Interface(
    allow_flagging=False,
    fn=predict_detection,
    inputs=gr.Image(type='pil', label='Image'),
    outputs=gr.Textbox(label='Output', lines=10),
    title=config.get('APP_TITLE'),
)

demo_api = gr.Interface(
    allow_flagging=False,
    fn=predict_api,
    inputs=gr.Image(type='pil', label='Image'),
    outputs=gr.Textbox(label='Output', lines=10),
    title=config.get('APP_TITLE'),
)

demo = gr.TabbedInterface([
    demo_captioning,
    demo_classification,
    demo_detection,
    demo_api,
], [
    'Captioning',
    'Classification',
    'Detection',
    'API',
], css='footer {visibility: hidden}')

if __name__ == "__main__":
    demo.queue().launch(root_path='/demo')

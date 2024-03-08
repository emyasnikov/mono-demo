import captioning
import classification
import config
import detection
import gradio as gr
import json

def predict_api(input):
    results = {
        'captioning': captioning.generate(input),
        'classification': classification.generate(input),
        'detection': detection.generate(input),
    }

    return json.dumps(results, indent=2)

demo_api = gr.Interface(
    allow_flagging=False,
    css='footer {visibility: hidden}',
    fn=predict_api,
    inputs=gr.Image(type='pil'),
    outputs=gr.Textbox(label='Preview', lines=10),
    title=config.get('APP_TITLE'),
)

demo = gr.TabbedInterface([
    demo_api,
], [
    'API',
])

if __name__ == "__main__":
    demo.queue().launch(root_path='/demo')

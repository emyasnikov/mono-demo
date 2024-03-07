import captioning
import classification
import config
import detection
import gradio as gr
import json
import translation

def predict(input):
    results = {
        'captioning': captioning.generate(input),
        'classification': classification.generate(input),
        'detection': detection.generate(input),
    }

    output = json.dumps(results, indent=2)

    return translation.translate(output)

app = gr.Interface(
    allow_flagging=False,
    css='footer {visibility: hidden}',
    fn=predict,
    inputs=gr.Image(type='pil'),
    outputs=gr.Textbox(label='Preview', lines=10),
    title=config.get('APP_TITLE'),
)

if __name__ == "__main__":
    app.queue().launch(root_path='/demo')

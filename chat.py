import gradio as gr
import json
import requests

context = []

def generate(prompt, context):
    r = requests.post(
        'http://127.0.0.1:11434/api/generate',
        json={
            'context': context,
            'model': 'phi',
            'prompt': prompt,
        },
        stream=False
    )

    r.raise_for_status()

    response = ''

    for line in r.iter_lines():
        body = json.loads(line)
        part = body.get('response', '')

        if 'error' in body:
            raise Exception(body['error'])

        response += part

        if body.get('done', False):
            return response, context

def chatbot(prompt):
    global context

    history = []
    output, context = generate(prompt, context)

    history.append((input, output))

    return history, history


demo = gr.Interface(
    fn=chatbot,
    inputs=gr.Textbox(lines=5, label="Input"),
    outputs=gr.Textbox(label="Output"),
)

if __name__ == '__main__':
    demo.launch()

import gradio as gr
import json
import requests

context = []

def generate(prompt, history):
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
            history.append((prompt, response))

            return response, history

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    message = gr.Textbox(label="Prompt")

    with gr.Row():
        clear = gr.ClearButton([message, chatbot])
        submit = gr.Button(value="Send")

    message.submit(generate, inputs=[message, chatbot], outputs=[chatbot, message])
    submit.click(generate, inputs=[message, chatbot], outputs=[chatbot, message])

if __name__ == '__main__':
    demo.launch()

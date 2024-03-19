import gradio as gr
import json
import requests

context = []
url = 'http://127.0.0.1:11434/api/generate'

def generate(prompt):
    body = {
        'context': context,
        'model': 'phi',
        'prompt': prompt,
        'stream': False,
    }

    response = requests.post(url, json=body)

    if response.status_code != 200:
        print('Error:', response.status_code, response.text)

        return None

    data = json.loads(response.text)
    context.extend(data['context'])

    return data['response']

with gr.Blocks() as demo:
    chatbot = gr.Textbox(lines=10)
    message = gr.Textbox(label="Prompt")

    with gr.Row():
        clear = gr.ClearButton([message, chatbot])

    message.submit(generate, inputs=message, outputs=chatbot)

if __name__ == '__main__':
    demo.queue().launch()

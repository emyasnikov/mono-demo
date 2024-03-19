import gradio as gr
import json
import requests

history = []
url = 'http://127.0.0.1:11434/api/generate'

def generate(prompt):
    history.append(prompt)
    context = '\n'.join(history)
    data = {
        'model': 'phi',
        'prompt': context,
        'stream': False,
    }

    response = requests.post(url, json=data)

    if response.status_code != 200:
        print('Error:', response.status_code, response.text)

        return None

    text = json.loads(response.text)['response']
    history.append(text)

    return text

with gr.Blocks() as demo:
    chatbot = gr.Textbox(lines=10)
    message = gr.Textbox(label="Prompt")

    with gr.Row():
        clear = gr.ClearButton([message, chatbot])

    message.submit(generate, inputs=message, outputs=chatbot)

if __name__ == '__main__':
    demo.launch()

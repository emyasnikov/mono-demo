import gradio as gr
import ollama

def append(prompt, history):
    chat = []

    for query, response in history:
        chat.append({'role': 'user', 'content': query})
        chat.append({'role': 'assistant', 'content': response})

    chat.append({'role': 'user', 'content': prompt})

    return chat

def generate(prompt, history):
    chat = append(prompt, history)
    message = ''
    model='llava:7b-v1.6-mistral-q4_0'
    response = ollama.chat(model=model, stream=True, messages=chat)

    for part in response:
        token = part['message']['content']
        message += token

        yield message

demo = gr.Interface(
    fn=generate,
    inputs=gr.Textbox(label='Prompt'),
    outputs=gr.Chatbot(),
)

if __name__ == '__main__':
    demo.launch()

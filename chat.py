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
    response = ollama.chat(model='phi', stream=True, messages=chat)

    for part in response:
        token = part['message']['content']
        message += token

        yield message

demo = gr.ChatInterface(
    clear_btn='Clear',
    fn=generate,
    retry_btn='Retry',
    submit_btn='Send',
    title='Chat',
    undo_btn='Undo',
)

if __name__ == '__main__':
    demo.queue().launch(root_path='/chat')

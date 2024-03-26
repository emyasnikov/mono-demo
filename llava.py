import gradio as gr
import ollama

def generate(prompt):
    chat = [{'role': 'user', 'content': prompt}]
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

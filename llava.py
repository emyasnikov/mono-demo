import gradio as gr
import ollama

def generate(prompt):
    message = ''
    response = ollama.chat(model='llava', stream=True, messages=[prompt])

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

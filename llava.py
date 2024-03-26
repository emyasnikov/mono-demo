import gradio as gr
import ollama

def generate(prompt):
    message = ''
    response = ollama.chat(model='llava:7b-v1.6-mistral-q4_0', stream=True, messages=[{
        'content': prompt,
        'role': 'user',
    }])

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

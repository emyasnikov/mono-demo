import gradio as gr
import ollama

def generate(prompt):
    chat = [{'role': 'user', 'content': prompt}]
    model='llava:7b-v1.6-mistral-q4_0'
    output = [('user', prompt)]
    response = ollama.chat(model=model, stream=True, messages=chat)

    for part in response:
        token = part['message']['content']
        output.append(('assistant', token))

        yield output

demo = gr.Interface(
    fn=generate,
    inputs=gr.Textbox(label='Prompt'),
    outputs=gr.Chatbot(),
)

if __name__ == '__main__':
    demo.launch()

import gradio as gr
import ollama

def generate(prompt):
    chat = [{'role': 'user', 'content': prompt}]
    model='llava:7b-v1.6-mistral-q4_0'
    output = [(prompt)]
    response = ollama.chat(model=model, stream=False, messages=chat)

    for part in response:
        token = part['message']['content']
        output.append((token))

        return output

demo = gr.Interface(
    fn=generate,
    inputs=gr.Textbox(label='Prompt'),
    outputs=gr.Textbox(label='Output'),
)

if __name__ == '__main__':
    demo.launch()

import gradio as gr

def generate(prompt, history):
    return prompt

demo = gr.Interface(
    fn=generate,
    inputs=gr.Textbox(label='Prompt'),
    outputs=gr.Chatbot(),
)

if __name__ == '__main__':
    demo.launch()

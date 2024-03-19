import gradio as gr

def generate(prompt, history):
    return prompt

demo = gr.ChatInterface(generate)

if __name__ == '__main__':
    demo.launch()

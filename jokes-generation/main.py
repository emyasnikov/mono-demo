import gradio as gr
import ollama


def generate():
    model="llama3.1:latest-jokes"

    return ollama.generate(model, "Erzähle ein Witz", stream=False)["response"]


with gr.Blocks() as demo:
    with gr.Column():
        output = gr.Textbox(interactive=False, label="Output", lines=10)
        button = gr.Button(value="Generate")

    button.click(fn=generate, inputs=[], outputs=output)

if __name__ == "__main__":
    demo.queue().launch(root_path="/witze/")

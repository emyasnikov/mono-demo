import gradio as gr
import ollama


def generate():
    model="llama3.1:8b-jokes"

    for result in ollama.generate(model, "", stream=False):
        return result


demo = gr.Interface(
    title="Witzegenerator",
    fn=generate,
    inputs=gr.Button("Generieren"),
    outputs=gr.Textbox(label="Output", lines=10),
)


if __name__ == "__main__":
    demo.queue().launch(root_path="/witze")

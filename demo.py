import gradio as gr

def predict():
    return "test"

demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(),
    outputs=gr.Textbox(label="Preview", lines=10),
)

demo.launch()

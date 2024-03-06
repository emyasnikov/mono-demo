import gradio as gr

def predict():
    return "test"

demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(),
    outputs=gr.Textbox(label='Preview', lines=10),
)

if __name__ == "__main__":
    demo.launch(root_path='/demo')

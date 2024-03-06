import caption
import gradio as gr

def predict(input):
    return caption.generate(input)

demo = gr.Interface(
    css='footer {visibility: hidden}',
    fn=predict,
    inputs=gr.Image(),
    outputs=gr.Textbox(label='Preview', lines=10),
    title='Image Recognition Demo',
)

if __name__ == "__main__":
    demo.launch(root_path='/demo')

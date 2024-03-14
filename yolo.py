import gradio as gr

def predict(image):
    return image

demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(type='pil', label='Input Image'),
    outputs=gr.Image(type='pil', label='Output Image'),
)

if __name__ == '__main__':
    demo.launch()

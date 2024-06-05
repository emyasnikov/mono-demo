import gradio as gr
from transformers import pipeline
import numpy as np

def transcribe(model_name, stream, new_chunk):
    transcriber = pipeline("automatic-speech-recognition", model=model_name)
    
    sr, y = new_chunk
    y = y.astype(np.float32)
    y /= np.max(np.abs(y))

    if stream is not None:
        stream = np.concatenate([stream, y])
    else:
        stream = y

    return stream, transcriber({"sampling_rate": sr, "raw": stream})["text"]


models = [
    "openai/whisper-small",
    "openai/whisper-medium",
    "openai/whisper-large-v2",
    "primeline/whisper-large-v3-german"
]

model_dropdown = gr.Dropdown(models, label="Select ASR Model")

demo = gr.Interface(
    transcribe,
    [
        model_dropdown,
        "state",
        gr.Audio(sources=["microphone"], streaming=True)
    ],
    [
        "state",
        "text"
    ],
    live=True,
)

demo.launch()

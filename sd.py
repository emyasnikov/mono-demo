import torch
from diffusers import DiffusionPipeline

pipeline = DiffusionPipeline.from_pretrained('segmind/small-sd', torch_dtype=torch.float32)
prompt = ''
image = pipeline(prompt).images[0]
image.save('image.png')

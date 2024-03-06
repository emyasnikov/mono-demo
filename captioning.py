import torch
from transformers import GPT2TokenizerFast, VisionEncoderDecoderModel, ViTImageProcessor

device = 'cuda' if torch.cuda.is_available() else 'cpu'

models = [
    'Abdou/vit-swin-base-224-gpt2-image-captioning',
    'nlpconnect/vit-gpt2-image-captioning',
    'ydshieh/vit-gpt2-coco-en',
]

def generate(image, greedy=True, model_name=None):
    model = models[model_name] if not model_name == None else models[1]

    model_raw = VisionEncoderDecoderModel.from_pretrained(model).to(device)
    tokenizer = GPT2TokenizerFast.from_pretrained(model)
    image_processor = ViTImageProcessor.from_pretrained(model)

    preprocessed = image_processor(images=image, return_tensors='pt').to(device)

    if greedy:
        output = model_raw.generate(**preprocessed, max_length=64)
    else:
        output = model_raw.sample(**preprocessed, do_sample=True, max_new_tokens=64, top_k=5)

    caption = tokenizer.batch_decode(output, skip_special_tokens=True)[0]

    return caption

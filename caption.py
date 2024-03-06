from transformers import GPT2TokenizerFast, VisionEncoderDecoderModel, ViTImageProcessor

models = [
    'Abdou/vit-swin-base-224-gpt2-image-captioning',
    'nlpconnect/vit-gpt2-image-captioning',
    'ydshieh/vit-gpt2-coco-en',
]

def generate(model_name=None):
    model = models[model_name] if not model_name == None else models[0]

    model_raw = VisionEncoderDecoderModel.from_pretrained(model)
    tokenizer = GPT2TokenizerFast.from_pretrained(model)
    image_processor = ViTImageProcessor.from_pretrained(model)

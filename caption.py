from transformers import GPT2TokenizerFast, VisionEncoderDecoderModel, ViTImageProcessor

models = [
    'Abdou/vit-swin-base-224-gpt2-image-captioning',
    'nlpconnect/vit-gpt2-image-captioning',
    'ydshieh/vit-gpt2-coco-en',
]

def generate(image, model_name=None):
    model = models[model_name] if not model_name == None else models[0]

    model_raw = VisionEncoderDecoderModel.from_pretrained(model)
    tokenizer = GPT2TokenizerFast.from_pretrained(model)
    image_processor = ViTImageProcessor.from_pretrained(model)

    preprocessed = image_processor(images=image, return_tersors='pt')
    output = model_raw.generate(**preprocessed, max_length=64)
    caption = tokenizer.batch_decode(output, skip_special_tokens=True)[0]

    return caption

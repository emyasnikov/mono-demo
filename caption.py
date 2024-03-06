models = [
    'Abdou/vit-swin-base-224-gpt2-image-captioning',
    'nlpconnect/vit-gpt2-image-captioning',
    'ydshieh/vit-gpt2-coco-en',
]

def generate(model_name=None):
    model = models[model_name] if not model_name == None else models[0]

import os.path
import torchvision
import urllib.request

LABELS_URL = 'https://storage.googleapis.com/bit_models/ilsvrc2012_wordnet_lemmas.txt'

def download_labels():
    filename = 'labels.txt'

    if not os.path.exists(filename):
        urllib.request.urlretrieve(LABELS_URL, filename)

    return filename

def generate(image):
    labels = download_labels()

    label_map = dict(enumerate(open(labels)))

    model = torchvision.models.resnet50(pretrained=True)
    model.eval()

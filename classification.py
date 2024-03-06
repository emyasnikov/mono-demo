import os.path
import torch
import torchvision
import urllib.request
from torchvision import transforms

LABELS_URL = 'https://storage.googleapis.com/bit_models/ilsvrc2012_wordnet_lemmas.txt'

device = 'cuda' if torch.cuda.is_available() else 'cpu'

transform = transforms.Compose([
    transforms.Resize(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

def download_labels():
    filename = 'labels.txt'

    if not os.path.exists(filename):
        urllib.request.urlretrieve(LABELS_URL, filename)

    return filename

def generate(image):
    labels = download_labels()

    label_map = dict(enumerate(open(labels)))

    model = torchvision.models.resnet50(pretrained=True).to(device)
    model.eval()

    logits = model(transform(image).unsqueeze(0)).to(device)
    probs = torch.nn.Softmax(dim=-1)(logits)
    sorted_probs = torch.argsort(probs, dim=-1, descending=True)

    output = {}

    for prob in sorted_probs[0, :10]:
        output[label_map[prob.item()].strip()] = "{:.2f}%".format(probs[0, prob.item()].item() * 100)

    return output

import config
import os.path
import torch
import torchvision
import translation
import urllib.request
from torchvision import transforms

device = 'cuda' if torch.cuda.is_available() else 'cpu'

transform = transforms.Compose([
    transforms.Resize(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

def download_labels():
    filename = config.get('LABELS_FILE')

    if not os.path.exists(filename):
        urllib.request.urlretrieve(config.get('LABELS_URL'), filename)

    return filename

def generate(image):
    labels = download_labels()

    label_map = dict(enumerate(open(labels)))

    model = torchvision.models.resnet50(pretrained=True).to(device)
    model.eval()

    logits = model(transform(image).unsqueeze(0)).to(device)
    probs = torch.nn.Softmax(dim=-1)(logits)
    sorted_probs = torch.argsort(probs, dim=-1, descending=True)

    output = []

    for prob in sorted_probs[0, :10]:
        label = label_map[prob.item()].strip()
        label = label.replace(',', ', ').replace('_', ' ')

        entry = {
            'label': translation.translate(label),
            'probability': '{:.2f}%'.format(probs[0, prob.item()].item() * 100),
        }

        output.append(entry)

    return output

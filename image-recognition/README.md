# Image Recognition Demo

## Installation

### Python

```bash
sudo apt update
sudo apt install libgl1-mesa-glx nginx tmux -y
sudo apt install python3-{pip,venv} -y
```

#### Environment

```bash
cp .env.example .env
mkdir ~/.venv
python3 -m venv ~/.venv/demo
source ~/.venv/demo/bin/activate
```

#### Dependencies

```bash
pip install deepl gradio opencv-python python-dotenv transformers
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

### Nginx

```bash
sudo cp demo.conf /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/demo.conf /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
sudo systemctl restart nginx
```

## Run

```bash
tmux new -d -s demo ~/.venv/demo/bin/python demo.py
```

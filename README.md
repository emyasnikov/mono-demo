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
mkdir ~/.venv
python3 -m venv ~/.venv/demo
source ~/.venv/demo/bin/activate
```

#### Dependencies

```bash
pip install gradio opencv-python transformers
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

### Nginx

```bash
sudo cp demo.conf /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/demo.conf /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
sudo systemctl restart nginx
```

### Tmux

```bash
tmux new -s demo
```

## Run

```bash
tmux attach -t demo
source ~/.venv/demo/bin/activate
python demo.py
```

# Stable Diffusion Demo

## Installation

### Ubuntu/Debian

```bash
sudo apt update
sudo apt install nginx python3-{pip,venv} tmux -y
```

### Environment

```bash
mkdir ~/.venv
python3 -m venv ~/.venv/sd
source ~/.venv/sd/bin/activate
```

### Packages

```bash
pip install accelerate diffusers gradio transformers
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

### Nginx

```bash
sudo cp sd.conf /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/sd.conf /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
sudo systemctl restart nginx
```

## Run

```bash
tmux new -d -s sd ~/.venv/sd/bin/python sd.py
```

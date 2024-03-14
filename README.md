# Object Detection Demo

## Installation

### Ubuntu/Debian

```bash
sudo apt update
sudo apt install nginx python3-{pip,venv} tmux -y
```

### Environment

```bash
mkdir ~/.venv
python3 -m venv ~/.venv/yolo
source ~/.venv/yolo/bin/activate
```

### Packages

```bash
pip install gradio ultralytics
pip install torch --index-url https://download.pytorch.org/whl/cu118
```

### Nginx

```bash
sudo cp yolo.conf /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/yolo.conf /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
sudo systemctl restart nginx
```

### Tmux

```bash
tmux new -s yolo
```

### Run

```bash
tmux attach -t yolo
source ~/.venv/yolo/bin/activate
python yolo.py
```

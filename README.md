# Object Detection Demo

## Installation

### Ubuntu/Debian

```bash
sudo apt update
sudo apt install nginx python3-{pip,venv} -y
```

### Environment

```bash
mkdir ~/.venv
python3 -m venv ~/.venv/yolo
source ~/.venv/yolo/bin/activate
```

### Packages

```bash
pip install gradio ultralytics -y
```

### Nginx

```bash
sudo cp yolo.conf /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/yolo.conf /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
sudo systemctl restart nginx
```

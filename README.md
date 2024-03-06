# Image Recognition Demo

## Installation

### Python

```bash
sudo apt install nginx -y
sudo apt install python3-{pip,venv} -y
```

#### Environment

```bash
python3 -m venv ~/.demo
source ~/.demo/bin/activate
```

#### Dependencies

```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
pip install transformers
```

### Nginx

```bash
sudo cp demo.conf /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/demo.conf /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
sudo systemctl restart nginx
```

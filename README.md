# LLaVA Demo

## Installation

### Ubuntu/Debian

```bash
sudo apt update
sudo apt install curl nginx python3-{pip,venv} -y
```

### Ollama

```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

### Environment

```bash
mkdir ~/.venv
python3 -m venv ~/.venv/llava
source ~/.venv/llava/bin/activate
```

### Packages

```bash
pip install gradio ollama
```

### Nginx

```bash
sudo cp llava.conf /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/llava.conf /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
sudo systemctl restart nginx
```

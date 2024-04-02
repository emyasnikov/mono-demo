# Chat Demo

## Installation

### Ubuntu/Debian

```bash
sudo apt update
sudo apt install curl nginx python3-{pip,venv} tmux -y
```

### Ollama

```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

### Environment

```bash
mkdir ~/.venv
python3 -m venv ~/.venv/chat
source ~/.venv/chat/bin/activate
```

### Packages

```bash
pip install gradio ollama
```

### Nginx

```bash
sudo cp chat.conf /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/chat.conf /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
sudo systemctl restart nginx
```

## Run

### CLI

```bash
ollama run phi
```

### API

Test the API with `curl`:

```bash
curl http://localhost::11434/api/generate -d '{
  "model": "phi",
  "prompt": "What is AI?"
}'
```

If the API doesn't work, try to run the following command:

```bash
sudo systemctl stop ollama
tmux new -d -s ollama ollama serve
```

### Interface

```bash
tmux new -d -s chat ~/.venv/chat/bin/python chat.py
```

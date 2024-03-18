# Chat Demo

Based on [Create your own chatbot with Llama2, Ollama and Gradio](https://bibek-poudel.medium.com/create-your-own-chatbot-with-llama2-ollama-and-gradio-5c60ecb1aad0)

## Installation

### Ubuntu/Debian

```bash
sudo apt update
sudo apt install curl nginx python3-{pip,venv} -y
```

### Ollama

```bash
curl https://ollama.ai/install.sh | sh
```

### Packages

```bash
pip install gradio
```

### Environment

```bash
mkdir ~/.venv
python3 -m venv ~/.venv/chat
source ~/.venv/chat/bin/activate
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

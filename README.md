# Stable Diffusion Demo

## Installation

### Ubuntu/Debian

```bash
sudo apt update
sudo apt install python3-venv
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

## Run

```bash
~/.venv/sd/bin/python sd.py
```

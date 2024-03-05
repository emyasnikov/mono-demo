# Image Recognition Demo

## Installation

### Miniconda

```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
```

```bash
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh
```

### Environment

```bash
conda create -n demo -y
conda activate demo
```

### Dependencies

```bash
conda install -n demo -c conda-forge gradio -y
conda install -n demo -c pytorch pytorch torchvision transformers -y
```

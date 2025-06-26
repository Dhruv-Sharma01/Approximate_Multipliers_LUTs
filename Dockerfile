# 1. Base image with CUDA & PyTorch
FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-runtime

# 2. System utilities (optional)
RUN apt-get update && apt-get install -y \
      git \
      build-essential \
    && rm -rf /var/lib/apt/lists/*

# 3. Python dependencies
RUN pip install --no-cache-dir \
      git+https://github.com/etrommer/torch-approx.git \
      torchvision \
      matplotlib \
      psutil

# 4. Set working directory
WORKDIR /workspace

# 5. Default shell
CMD ["/bin/bash"]

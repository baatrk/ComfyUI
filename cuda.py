import torch

print("CUDA elérhetőség:", torch.cuda.is_available())
print("GPU neve:", torch.cuda.get_device_name(0))
print("CUDA verzió:", torch.version.cuda)
print("PyTorch CUDA verzió:", torch.version.cuda)
print("PyTorch verzió:", torch.__version__)
print("cuDNN verzió:", torch.backends.cudnn.version())

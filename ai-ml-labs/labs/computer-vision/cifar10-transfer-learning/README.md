# CIFAR-10 Transfer Learning with VGG19-BN

A cleaned-up transfer-learning experiment for CIFAR-10 using VGG19-BN.

The lab fine-tunes a pretrained VGG19-BN classifier for the 10 CIFAR-10 classes.

## Modernization

- current TorchVision weights API replaces `pretrained=True`
- preprocessing comes directly from `VGG19_BN_Weights.DEFAULT.transforms()`
- deterministic train/validation split
- CUDA, Apple MPS, or CPU device selection
- evaluation avoids unnecessary softmax computation
- checkpoints store a `state_dict` instead of pickling the complete model
- no Google Drive / Colab dependency

Run:

```bash
pip install -e ".[torch]"
python labs/computer-vision/cifar10-transfer-learning/train.py
```

## Historical result

The original README reported:

- validation accuracy: **94.41%**
- test accuracy: **93.96%**

Those numbers are retained as **historical reported results**. They have not yet been rerun under the modernized environment, so this lab does not claim that the new script reproduces them until a fresh experiment is recorded.

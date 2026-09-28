import argparse
from pathlib import Path

import torch
from torch import nn
from torch.utils.data import DataLoader, random_split
from torchvision import datasets
from torchvision.models import VGG19_BN_Weights, vgg19_bn


def build_model(num_classes: int = 10) -> nn.Module:
    model = vgg19_bn(weights=VGG19_BN_Weights.DEFAULT)
    model.classifier[6] = nn.Linear(model.classifier[6].in_features, num_classes)
    return model


def make_loaders(
    root: Path,
    *,
    batch_size: int,
    seed: int,
) -> tuple[DataLoader, DataLoader, DataLoader]:
    transform = VGG19_BN_Weights.DEFAULT.transforms()
    full_train = datasets.CIFAR10(
        root=root,
        train=True,
        download=True,
        transform=transform,
    )
    test_set = datasets.CIFAR10(
        root=root,
        train=False,
        download=True,
        transform=transform,
    )

    train_size = int(0.8 * len(full_train))
    eval_size = len(full_train) - train_size
    generator = torch.Generator().manual_seed(seed)
    train_set, eval_set = random_split(
        full_train,
        [train_size, eval_size],
        generator=generator,
    )

    return (
        DataLoader(train_set, batch_size=batch_size, shuffle=True),
        DataLoader(eval_set, batch_size=batch_size, shuffle=False),
        DataLoader(test_set, batch_size=batch_size, shuffle=False),
    )


def accuracy(model: nn.Module, loader: DataLoader, device: torch.device) -> float:
    model.eval()
    correct = 0
    total = 0
    with torch.inference_mode():
        for images, labels in loader:
            images = images.to(device)
            labels = labels.to(device)
            predictions = model(images).argmax(dim=1)
            correct += predictions.eq(labels).sum().item()
            total += labels.shape[0]
    return correct / total


def train(
    model: nn.Module,
    loader: DataLoader,
    *,
    epochs: int,
    device: torch.device,
) -> None:
    model.to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(
        model.parameters(),
        lr=1e-3,
        momentum=0.9,
    )

    for epoch in range(1, epochs + 1):
        model.train()
        running_loss = 0.0
        examples = 0
        for images, labels in loader:
            images = images.to(device)
            labels = labels.to(device)

            optimizer.zero_grad(set_to_none=True)
            logits = model(images)
            loss = criterion(logits, labels)
            loss.backward()
            optimizer.step()

            batch_size = labels.shape[0]
            running_loss += loss.item() * batch_size
            examples += batch_size

        print(f"epoch={epoch} loss={running_loss / examples:.4f}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, default=Path("data"))
    parser.add_argument("--output", type=Path, default=Path("artifacts/cifar10-vgg19.pt"))
    parser.add_argument("--epochs", type=int, default=4)
    parser.add_argument("--batch-size", type=int, default=32)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    if torch.cuda.is_available():
        device = torch.device("cuda")
    elif torch.backends.mps.is_available():
        device = torch.device("mps")
    else:
        device = torch.device("cpu")

    train_loader, eval_loader, test_loader = make_loaders(
        args.data,
        batch_size=args.batch_size,
        seed=args.seed,
    )
    model = build_model()
    train(model, train_loader, epochs=args.epochs, device=device)

    print(f"validation_accuracy={accuracy(model, eval_loader, device):.4f}")
    print(f"test_accuracy={accuracy(model, test_loader, device):.4f}")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    torch.save({"state_dict": model.state_dict()}, args.output)


if __name__ == "__main__":
    main()

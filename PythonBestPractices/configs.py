import json


def load_data(path: str) -> None:
    print(f"Loading data from {path} ...")


def setup_logging(path: str) -> None:
    print(f"Setting up logging to {path} ..")


def train_model(epochs: int, learning_rate: float):
    print(f"Training {epochs} at {learning_rate}")


def main():
    data = json.load(open(file="./config.json", encoding="UTF-8"))
    load_data((data["data_path"]))

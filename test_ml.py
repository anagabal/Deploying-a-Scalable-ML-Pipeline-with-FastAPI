import numpy as np
import pandas as pd
import pytest
from sklearn.model_selection import train_test_split
from ml.data import process_data
from train_model import train_model, inference, compute_model_metrics


data = pd.read_csv("data/census.csv")
train, test = train_test_split(data, test_size=0.20, random_state=42)

categorical_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]

label = "salary"

X_train, y_train, encoder, lb = process_data(
    train,
    categorical_features=categorical_features,
    label=label,
    training=True
)

X_test, y_test, _, _ = process_data(
    test,
    categorical_features=categorical_features,
    label=label,
    training=False,
    encoder=encoder,
    lb=lb
)

model = train_model(X_train, y_train)
preds = inference(model, X_test)

def test_train_model():
    """
    Test if train_model() returns a trained model object
    """
    assert model is not None


def test_inference():
    """
    Test if inference() returns predicitons with the right length
    """
    assert len(preds) == len(y_test)


def test_compute_model_metrics():
    """
    Test if compute_model_metrics() returns numeric metric values
    """
    p, r, fb = compute_model_metrics(y_test, preds)
    assert isinstance(p, (float, np.floating))
    assert isinstance(r, (float, np.floating))
    assert isinstance(fb, (float, np.floating))

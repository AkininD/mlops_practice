import pytest
from model import model, dataset1, dataset2, dataset3, noisy_dataset

def test_model_quality(dataset):
    prediction = model.predict(dataset[0].reshape(-1, 1))
    mse = ((prediction - dataset[1]) ** 2).mean()
    assert mse < 0.5, "Model's quality is unsatisfactory"

def test_datasets():
    test_model_quality(dataset1)
    test_model_quality(dataset2)
    test_model_quality(dataset3)
    test_model_quality(noisy_dataset)

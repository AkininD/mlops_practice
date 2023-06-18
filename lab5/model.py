import numpy as np
from sklearn.linear_model import LinearRegression

def create_dataset():
    xs = np.linspace(0, 10, 100)
    ys = xs + np.random.random(100) * 2 - 1
    return xs, ys

dataset1 = create_dataset()
dataset2 = create_dataset()
dataset3 = create_dataset()

model = LinearRegression()
model.fit(dataset1[0].reshape(-1, 1), dataset1[1])

def create_noisy_dataset():
    xs = np.linspace(0, 10, 100)
    ys = xs + np.random.random(100) * 2 - 1
    ys[25:45] *= 2
    return xs, ys

noisy_dataset = create_noisy_dataset()

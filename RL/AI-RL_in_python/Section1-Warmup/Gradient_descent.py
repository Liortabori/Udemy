import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def generate_data(n, alpha, x_size=1):
    X = np.random.randint(0, 100, (n,x_size)).reshape((n,x_size))
    noise = (alpha * np.random.normal(size=n)).reshape((n,1))
    y = np.add(np.array([sum(x) for x in X]).reshape((n,1)), noise)
    columns = ["X_" + str(i) for i in range(x_size)] + list("y")
    return pd.DataFrame(data=np.concatenate((X, y), axis=1), columns=columns)


def plot_data(df):
    plt.scatter(df["X_0"], df.y)
    perfect_line = np.linspace(0,100,100)
    plt.plot(perfect_line,perfect_line, color="k")
    plt.show()


def step(X, y, weights, lr):
    n = X.shape[0]
    Yhat = np.dot(X, weights)
    err = Yhat - y
    grad = np.dot(X.T, err) / n
    weights = weights - (lr * grad)
    return weights


def gd(data, lr, iterations):
    X = data[data.columns[data.columns != "y"]]
    y = data.y
    weights = np.random.normal(size=X.shape[1])
    loss = [np.square(np.dot(X, weights) - y).mean()]
    for i in range(iterations):
        weights = step(X, y, weights, lr)
        loss.append(np.square(np.dot(X, weights) - y).mean())
    return loss


def plot_loss(loss):
    plt.scatter(range(len(loss)), loss)
    plt.show()


lr = 1e-5
iterations = 100
x_size = 1

data = generate_data(500, 5, x_size)
#plot_data(data) #only works for 1 dimensional X's
loss = gd(data, lr, iterations)
plot_loss(loss)
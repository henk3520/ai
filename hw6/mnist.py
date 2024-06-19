from keras.datasets import mnist
import keras
import numpy as np

(x_train, y_train), (x_test, y_test) = mnist.load_data()
train_images = np.asarray(x_train, dtype=np.float32) / 255.0
test_images = np.asarray(x_test, dtype=np.float32) / 255.0
train_images = train_images.reshape(60000, 784)
test_images = test_images.reshape(10000, 784)
y_train = keras.utils.to_categorical(y_train)

def forward(X, Y, W):
    y_pred = X.matmul(W)
    probs = y_pred.softmax()
    loss = probs.cross_entropy(Y)
    return loss

batch_size = 32
steps = 20000

X = Tensor(train_images)
Y = Tensor(y_train)
W = Tensor(np.random.randn(784, 10))

for step in range(steps):
    ri = np.random.permutation(train_images.shape[0])[:batch_size]
    Xb, yb = Tensor(train_images[ri]), Tensor(y_train[ri])
    loss = forward(Xb, yb, W)
    loss.backward()
    if step % 1000 == 0 or step == steps - 1:
        full_loss = forward(X, Y, W).data
        print(f'Loss at step {step}: {full_loss}')
    W.data -= 0.01 * W.grad
    W.grad = np.zeros_like(W.grad)

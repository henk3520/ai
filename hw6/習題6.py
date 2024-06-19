#參考chatgpt
import numpy as np

class Tensor:
    def __init__(self, data, _children=(), _op=''):
        self.data = np.array(data)
        self.grad = np.zeros_like(self.data)
        self._backward = lambda: None
        self._prev = set(_children)
        self._op = _op

    @property
    def shape(self):
        return self.data.shape

    def __add__(self, other):
        other = other if isinstance(other, Tensor) else Tensor(other)
        out = Tensor(self.data + other.data, (self, other), '+')

        def _backward():
            self.grad += out.grad
            other.grad += out.grad
        out._backward = _backward

        return out

    def __mul__(self, other):
        other = other if isinstance(other, Tensor) else Tensor(other)
        out = Tensor(self.data * other.data, (self, other), '*')

        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad
        out._backward = _backward

        return out

    def __pow__(self, other):
        assert isinstance(other, (int, float)), "only supporting int/float powers for now"
        out = Tensor(self.data ** other, (self,), f'**{other}')

        def _backward():
            self.grad += (other * self.data ** (other - 1)) * out.grad
        out._backward = _backward

        return out

    def relu(self):
        out = Tensor(np.maximum(0, self.data), (self,), 'relu')

        def _backward():
            self.grad += (self.data > 0) * out.grad
        out._backward = _backward

        return out

    def matmul(self, other):
        other = other if isinstance(other, Tensor) else Tensor(other)
        out = Tensor(np.dot(self.data, other.data), (self, other), 'matmul')

        def _backward():
            self.grad += np.dot(out.grad, other.data.T)
            other.grad += np.dot(self.data.T, out.grad)
        out._backward = _backward

        return out

    def softmax(self):
        exps = np.exp(self.data - np.max(self.data, axis=1, keepdims=True))
        out_data = exps / np.sum(exps, axis=1, keepdims=True)
        out = Tensor(out_data, (self,), 'softmax')

        def _backward():
            for i, (yi, gi) in enumerate(zip(out.data, out.grad)):
                yi = yi.reshape(-1, 1)
                self.grad[i] += (np.diagflat(yi) - np.dot(yi, yi.T)).dot(gi)
        out._backward = _backward

        return out

    def log(self):
        out = Tensor(np.log(self.data), (self,), 'log')

        def _backward():
            self.grad += (1 / self.data) * out.grad
        out._backward = _backward

        return out

    def sum(self, axis=None):
        out = Tensor(np.sum(self.data, axis=axis), (self,), 'sum')

        def _backward():
            self.grad += np.ones_like(self.data) * out.grad
        out._backward = _backward

        return out

    def cross_entropy(self, yb):
        log_probs = self.log()
        loss = - (log_probs * yb).sum(axis=1).mean()
        out = Tensor(loss, (self,), 'cross_entropy')

        def _backward():
            n = yb.data.shape[0]
            self.grad += (log_probs.data - yb.data) / n
        out._backward = _backward

        return out

    def backward(self):
        topo = []
        visited = set()

        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    build_topo(child)
                topo.append(v)
        build_topo(self)

        self.grad = np.ones_like(self.data)
        for v in reversed(topo):
            v._backward()

    def __neg__(self):
        return self * -1

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return other + (-self)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        return self * other ** -1

    def __rtruediv__(self, other):
        return other * self ** -1

    def __repr__(self):
        return f"Tensor(data={self.data}, grad={self.grad})"

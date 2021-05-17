import random
from functions import *

class Perceptron:
    def __init__(self, n):
        self.weights = [random.uniform(-1, 1) for i in range(n)]

        self.learning_rate = 0.01

    def predict(self, inputs):
        sum = 0
        #w0*x0 + w1*x1
        for i in range(0, len(self.weights)):
            sum += inputs[i] * self.weights[i]

        #activation function
        output = Activate(sum)
        return output

    def guessY(self, x):
        w0, w1, w2 = self.weights[0], self.weights[1], self.weights[2]
        # 1 is the bias
        return  - (w0/w1) * x - (w2/w1) * 1

    def train(self, inputs, target):
        #supervised learning process
        guess = self.predict(inputs)
        error = target - guess

        for i in range(0, len(self.weights)):
            self.weights[i] +=  error * inputs[i] * self.learning_rate

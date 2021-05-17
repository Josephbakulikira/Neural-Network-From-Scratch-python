from Matrix import *
import math

def Sigmoid(x):
    return 1 / (1 + math.exp(-x))

def derivativeSigmoid(x):
    return Sigmoid(x) * (1 - Sigmoid())

def dSigmoid(y):
    return y * (1 - y)

class NeuralNetwork:
    def __init__(self, n_inputs, n_hiddenLayers, n_outputs):
        self.input_layers = n_inputs
        self.hidden_layers = n_hiddenLayers
        self.output_layers = n_outputs

        self.learning_rate = 0.1

        self.hiddenInputWeights = Matrix(self.hidden_layers, self.input_layers)
        self.hiddenInputWeights.randomize()
        self.hiddenOutputWeights = Matrix(self.output_layers, self.hidden_layers)
        self.hiddenOutputWeights.randomize()

        self.hiddenBias = Matrix(self.hidden_layers, 1)
        self.hiddenBias.randomize()
        self.outputBias = Matrix(self.output_layers, 1)
        self.outputBias.randomize()



    def FeedForward(self, inputs):
        inputs = Matrix.fromArray(inputs)

        hidden = Matrix.matrix_multiplication(self.hiddenInputWeights, inputs)
        hidden.add(self.hiddenBias)
        hidden.map(Sigmoid)

        output = Matrix.matrix_multiplication(self.hiddenOutputWeights , hidden)
        output.add(self.outputBias)
        output.map(Sigmoid)


        return output.toArray()

    def Train(self, inputs, targets, debug = False):
        inputs = Matrix.fromArray(inputs)

        hidden = Matrix.matrix_multiplication(self.hiddenInputWeights, inputs)
        hidden.add(self.hiddenBias)
        hidden.map(Sigmoid)

        outputs = Matrix.matrix_multiplication(self.hiddenOutputWeights , hidden)
        outputs.add(self.outputBias)
        outputs.map(Sigmoid)

        # outputs = self.FeedForward(inputs)

        # outputs = Matrix.fromArray(outputs)
        outputs.label = "Outputs"
        targets = Matrix.fromArray(targets)
        targets.label = "Targets"

        err = targets - outputs
        err.label = "Error"

        gradient = Matrix.staticMap(outputs, dSigmoid)
        if err.rows == 1 and err.cols == 1:
            gradient.multiply(err.matrix[0][0])
        else:
            gradient.HadamartProduct(err)
        gradient.multiply(self.learning_rate)

        hidden_transposed = Matrix.transpose(hidden)
        w_hiddenOuputSlope = Matrix.matrix_multiplication(gradient, hidden_transposed)

        # adjust the hidden output layers weights by the slope
        self.hiddenOutputWeights.add(w_hiddenOuputSlope)
        # adjust the bias output by the its deltas(gradient)
        self.outputBias.add(gradient)

        transposed_hiddenOutputs = Matrix.transpose(self.hiddenOutputWeights)
        hidden_errors = None
        if err.rows == 1 and err.cols == 1:
            hidden_errors = transposed_hiddenOutputs
            hidden_errors.multiply(err.matrix[0][0])
        else:
            hidden_errors = Matrix.matrix_multiplication(transposed_hiddenOutputs, err)

        hidden_gradient = Matrix.staticMap(hidden, dSigmoid)
        hidden_gradient.HadamartProduct(hidden_errors)
        hidden_gradient.multiply(self.learning_rate)

        transposed_inputs = Matrix.transpose(inputs)
        w_hiddeninputSlope = Matrix.matrix_multiplication(hidden_gradient, transposed_inputs)

        self.hiddenInputWeights.add(w_hiddeninputSlope)
        self.hiddenBias.add(hidden_gradient)

        #debug
        if debug == True:
            outputs.Debug()
            targets.Debug()
            err.Debug()

# Kelas Layer
class Layer():
    def __init__(self, act_function, arr_weight, arr_bias):
        self.act_function = act_function
        self.weight = arr_weight
        self.bias = arr_bias
        
    def solve():
        if(act_function == "linear"):
            print("linear")
        elif(act_function == "sigmoid"):
            print("sigmoid")
        elif(act_function == "relu"):
            print("relu")
        else:
            print("softmax")

# ini main
data_training, target = readData()
activation, bias, weight = readModel()
neural_network = NeuralNetwork()

layer.append(Layer(weight[i], bias[i], this.act_function, threshold=0.1))
print("")
for data in data_training:
    layer.insert(0, InputLayer(data))
    neural_network.base_layer = layer
    neural_network.solve()
    result.append(neural_network.current_layer[-1].result)
    neural_network.deque_layer()

print("")
print("Target Class \t: ", target)
print("Predict Class \t: ", result)
print("=================================")
if (result == target):
    print("Result :")
else:
    print("Result : Wrong Predict")


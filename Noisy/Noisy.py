import numpy as np
import math
import ast

# constraints of network heirarchy
class neuralNet:
    def __init__(self,k,layer,r1,r2):
        self.k = k
        self.layers = layer
        self.n = pow(self.k,self.layers)
        self.learning_rate = 1/(4*self.k)
        self.threshold = (r1+r2)*math.sqrt(self.k)/2

        # weights are initialized
        self.weights = []
        for i in range(self.layers-1):
            layer_weight = []
            for j in range(self.n):
                neuron_weight = []
                for k in range(self.n):
                    neuron_weight.append(1/self.n)
                layer_weight.append(neuron_weight)
            self.weights.append(layer_weight)

        self.weights = np.array(self.weights,dtype='float')


        # states of neuron initialized
        self.states = []
        for i in range(self.layers):
            layer_neuron = []
            for j in range(self.n):
                layer_neuron.append(0)
            self.states.append(layer_neuron)

        self.states = np.array(self.states,dtype='float')
    

    # Oja's rule applied
    def update(self,layer_num,neuron_num,potential):
        self.weights[layer_num-1,neuron_num] = self.weights[layer_num-1,neuron_num] + self.learning_rate*potential*(self.states[layer_num-1]-potential*self.weights[layer_num-1,neuron_num])

    def find_potential(self,layer_num,neuron_num):
        potential = np.matmul(self.weights[layer_num-1,neuron_num].transpose(),self.states[layer_num-1])
        return potential

    def train(self,filename):
        open_file = open(filename,"r")
        training_set = open_file.readlines()
        training_set = [i.strip() for i in training_set]
        # print(training_set)
        training_set = [ast.literal_eval(i) for i in training_set]

        for j in training_set:
            concept_list = j[:-1]
            level = j[-1]
            curr_layer = 0
            self.states[0] = np.array(concept_list)
            print(self.states)
            while curr_layer!=level:
                curr_layer+=1
                max_potential = -1
                max_potential_neuron = 0
                for i in range(self.n):
                    neuron_potential = self.find_potential(curr_layer,i)
                    if(neuron_potential>=self.threshold):
                        self.states[curr_layer][i] = 1
                    else:
                        self.states[curr_layer][i] = 0
                    if(neuron_potential>max_potential):
                        max_potential_neuron = i
                        max_potential = neuron_potential
                print(self.states)
                
            self.update(curr_layer,max_potential_neuron,max_potential)
            self.states[:][:] = 0
            print(self.states)

    def test(self,filename):
        open_file = open(filename,"r")
        test_set = open_file.readlines()
        test_set = [i.strip() for i in test_set]
        test_set = [ast.literal_eval(i) for i in test_set]

        for j in test_set:
            self.states[0] = np.array(j)
            # print(self.states)
            curr_layer = 0
            while curr_layer!=self.layers-1:
                curr_layer+=1
                for i in range(self.n):
                    neuron_potential = self.find_potential(curr_layer,i)
                    if(neuron_potential>=self.threshold):
                        # print("Yeah")
                        self.states[curr_layer][i] = 1
                    else:
                        # print(self.threshold)
                        # print(neuron_potential)
                        self.states[curr_layer][i] = 0
                # print(self.states)
            # self.states[:][:] = 0
            print(self.states)
            self.states[:][:] = 0

# uncomment this and run

# a = neuralNet(2,3,1,1)
# a.train("training.txt")
# print("Training ends here")
# a.test("testing.txt")
# print(a.weights)








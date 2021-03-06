# Code to produce histogram of weights from array
import os
import torch
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

LAYER = int(input("Enter layer index: "))
NRN_INDX = int(input("Enter neuron index: "))

state_dict = torch.load("saved_l2.net")
wts = []
flag = True

while (flag == True):
    if (LAYER == 1):
        for i in range(2):
            for j in range(5):
                for wt in state_dict["conv1.weight"][NRN_INDX,i,j,:]:
                    wts.append(wt.item())
        num_wts = 50
        thr = 10
        flag = False
    elif (LAYER == 2):
        for i in range(32):
            for j in range(2):
                for wt in state_dict["conv2.weight"][NRN_INDX,i,j,:]:
                    wts.append(wt.item())
        num_wts = 128
        thr = 1
        flag = False
    else:
        print("Please enter layer index of 1 or 2")


(n, bins, patches) = plt.hist(wts, bins=20, range=(0.00, 1.00))
sparsity = n[19] / num_wts
exp_spars = thr / num_wts
print("sparsity = {}".format(sparsity))
print("expected sparsity = {}".format(exp_spars))
plt.title("Histogram of c{}n{} neuron's weight distribution\nsparsity = {}   thr/num weights = {}".format(LAYER, NRN_INDX, sparsity, exp_spars))
plt.xlabel('weight')
plt.ylabel('number weights')
plt.show()

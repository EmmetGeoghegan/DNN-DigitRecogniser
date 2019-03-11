"""
Emmet Geoghegan
The goal is to create a machine learning algorithm so that when given training
data set it can determine on the test set what number is written
"""

import tensorflow as tf
import keras.utils as ku
import os as os
import numpy as np
import pandas as pd
import sklearn as sk
import matplotlib.pyplot as plt


train = pd.read_csv("C:/Users/16496666/Desktop/Github Projects/Kaggle-ML-DigitRecognizer/input/train.csv")
test = pd.read_csv("C:/Users/16496666/Desktop/Github Projects/Kaggle-ML-DigitRecognizer/input/test.csv")

print(train.shape)         # Prints the dimensions of the train sheet
# print(test.shape)          # Prints the dimensions of the test sheet


# print(train.head(5))  # Print the first n rows of the xl doc
# print(test.head(5))   # Print the first n rows of the xl doc

tans = train["label"]  # Our solutions to training set

tdata = train.drop(columns=["label"])  # Training data without answer col
# print(datacols.head(5))    # Test it worked

# Now we want to display the data on screen
# Using matplotlib which takes rgb values (255,255,255)
# We want to normalise all our data to this format

tdata = tdata/255
test = test/255

# Now we want to turn each row into a 28x28 pandas dataframe [0][:, :, 0]
tdata = tdata.values.reshape(-1, 28, 28, 1)
test = test.values.reshape(-1, 28, 28, 1)

# Now we reshape each of the data labels to be vectors
# eg 4 would now be repesented by [0,0,0,0,1,0,0,0,0,0]
tans = ku.to_categorical(tans, num_classes=10)


# Set a random seed for our nnet so we can see the effect our changes have on
# our tests ruling out a better random start giving better results

seed = 8

# Now we want to split our training set into two other sets
# One is 85% of our data so we can train on it
# The other is the remaning 15% that we can test to see how well we do
# Take our results and make adjustments to our nnet

#tdata, tdataval, tans, tansval = train_test_split(tdata, tans, test_size=0.85, random_state=seed)


"""    ----- Displays all the numbers in the training set -----
for i in range(0, 42000, 1):
    displayarray = np.array(datacols[i])
    g = plt.imshow(displayarray[i][:, :, 0], cmap="Greys")
    plt.show()
"""

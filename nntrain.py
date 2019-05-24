"""
Emmet Geoghegan
The goal is to create a machine learning algorithm so that when given training
data set it can determine on the test set what number is written
"""
# Imports
import tensorflow as tf
import pandas as pd
import numpy as np
import keras
import matplotlib.pyplot as plt
from keras.utils.np_utils import to_categorical
from sklearn.model_selection import train_test_split
import os


def main():
    # Get our train and test data sets from the import files
    train = pd.read_csv("C:/Users/Emmet/Desktop/Github/Kaggle-ML-DigitRecognizer/input/train.csv")
    test = pd.read_csv("C:/Users/Emmet/Desktop/Github/Kaggle-ML-DigitRecognizer/input/test.csv")

    # Visualise our dataset
    # print(train.head())
    # input()
    # print(test.head())

    # Isolate our solutions to Y_train
    y_train = train["label"]

    # Remove our solutions from the test data
    x_train = train.drop(labels=["label"], axis=1)

    # Check for any empty data values that have to be removed (Nothing returned so all good)
    print("Null values in the training set:", x_train.isnull().any().sum())
    print("Null values in the test set:", test.isnull().any().sum())

    # Reshape our data to 28x28 pixel grids
    x_train = x_train.values.reshape(-1, 28, 28, 1)
    test = test.values.reshape(-1, 28, 28, 1)

    # Normalize the data, Were given pixel values from 1-255, We convert so pixel values are 0-1
    # print(x_train[0])
    x_train = x_train / 255.0
    test = test / 255.0
    # print(x_train[0])

    # Now we "Normalise" our solutions by converting them to vectors eg 7 is now [0,0,0,0,0,0,0,1,0,0]
    y_train = to_categorical(y_train, num_classes=10)

    # Set a random seed so we can see if we are making a difference as we change things
    seed = 2

    # Split our training set into a training and validation set 90-10 ratio respectivly
    x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.1, random_state=seed)

    # Plot all training images
    # for i in range(0, 42000, 1):
    #    trainingimage = plt.imshow(x_train[i][:, :, 0], cmap="Greys")
    #    plt.show()

    # Now we have all our data seperated, we can start making a model (Going with a simple sequential model)
    model = tf.keras.models.Sequential()
    # Flatten layer turns our 28x28 images into vectors so the neural net can process them
    model.add(tf.keras.layers.Flatten())
    # Add our hidden layers were using 2, 1st param: Number of neurons 2nd param: Activation fn, ie what makes the neuron Fire (rectified linear (relu))
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    # Output layer (For classifications its the number of options we have) ie 10 0-9 we want to get the most likely so use softmax which is prob distribution
    model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

    # Training parameters, Adam is default optimiser, loss is default categorical type, we want to track accuracy as we train
    model.compile(optimizer="adam",
                  loss="categorical_crossentropy",
                  metrics=["accuracy"])

    # Train the network
    batch_size = 90
    epochs = 5
    # We now have a trained network
    model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_data=(x_val, y_val))

    # We now export the model to a JSON so we dont have to re-train every time
    model_json = model.to_json()
    with open("mymodel.json", "w") as json_file:
        json_file.write(model_json)
    model.save_weights("mymodel.h5")
    print("Saved model to disk")


if __name__ == "__main__":
    main()

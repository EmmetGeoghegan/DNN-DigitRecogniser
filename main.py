# Goal is to create a gui that has a 280x280 pixel grid that can be drawn on
# Drawings will be saved as a 28x28 array with values of 0-1
# GUI has a submit button where the drawing array is passed to the neural net
# And the screen displays what the network thinks you drew

import paint
import imageprocessor as ip
import numpy as np
import nntrain as nn
import matplotlib.pyplot as plt
import tensorflow as tf


def testingloop(nnmodel, testimage):
    yournumber = mymodel.predict(image_matrix)
    results = np.argmax(yournumber, axis=1)
    print("Your number was {}".format(results))


def showdrawing(image):
    plt.imshow(image[0][:, :, 0], cmap="Greys")
    plt.show()

# If you need to train a new nural net un-comment this
# nn.main()


# load our NN from the json and h5 files
modeljson = open("model.json", "r")
loadedmodel = modeljson.read()
modeljson.close()
mymodel = tf.keras.models.model_from_json(loadedmodel)
mymodel.load_weights("model.h5")
print("Loaded model from disk")

# Send our new drawing and see what it predicts
# Loop to test multiple images
while True:
    paint.main()
    image_matrix = ip.main()
    # showdrawing(image_matrix)           # show what were submitting to the nn
    testingloop(mymodel, image_matrix)

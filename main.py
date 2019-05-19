# Goal is to create a gui that has a 280x280 pixel grid that can be drawn on
# Drawings will be saved as a 28x28 array with values of 0-1
# GUI has a submit button where the drawing array is passed to the neural net
# And the screen displays what the network thinks you drew

import paint
import imageprocessor

# paint.py generates the 280x280 image
# impageprocessor.py takes that image and turns it into a 28x28 image then generates an array to represent that image


print(imageprocessor.image_matrix)

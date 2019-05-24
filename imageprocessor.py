# Script to take the output from paint program and process for the neural net into a 28x28 matrix

from PIL import Image
from resizeimage import resizeimage
import numpy as np


def resizer(input):                                          # Func to resize images
    output = resizeimage.resize_contain(input, [28, 28])
    output.save("28x28.png")
    print("==========================")
    print("Image Sucessfully Re-Sized")
    print("==========================")


def getpixelvals(inputdata):                                      # Takes the resized images and gets pixel values
    pixelvalues = []
    rawpixelvalues = list(inputdata.getdata())
    for i in range(0, 784, 1):                                      # Normalises the pixelvalues
        pixelvalues.append(1-int(rawpixelvalues[i][0])/255)
    pixelvalues = np.array(pixelvalues)                             # Turns the list into an array for re-shaping
    pixelarray = pixelvalues.reshape(28, 28)                        # Re-shapes list into a 28x28 array for the nn
    return(pixelarray)                                              # Returns the array


def main():
    input = Image.open("usersublarge.png")
    resizer(input)
    processedinput = Image.open("28x28.png")
    image_matrix = getpixelvals(processedinput)


if __name__ == "__main__":
    main()

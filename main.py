# Goal is to create a gui that has a 280x280 pixel grid that can be drawn on
# Drawings will be saved as a 28x28 array with values of 0-1
# GUI has a submit button where the drawing array is passed to the neural net
# And the screen displays what the network thinks you drew

import paint
import imageprocessor as ip
import nntrain as nn
import matplotlib.pyplot as plt

# paint.py generates the 280x280 image
# impageprocessor.py takes that image and turns it into a 28x28 image then generates an array to represent that image


# Plot our image so we can see all is good
def imagechecker(drawing):
    plt.imshow(drawing, cmap="Greys")
    plt.show()
# imagechecker()


# Get the users drawing
paint.main()
ip.main()
# imagechecker(ip.main())        # View users submitted number

# If you need to train a new nural net un-comment this
# nn.main()
# Our data we want to check is ip.image_matrix its the 28x28 image the user drew
# We want to pass this to the trained nn
# And see what we get

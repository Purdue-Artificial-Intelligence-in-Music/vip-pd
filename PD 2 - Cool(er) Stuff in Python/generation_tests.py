from image_generator import *
import unittest
import numpy as np

# Make a UnitTest class called generation_tests.

# Write the following tests and make sure your generators pass the tests (because they work).
# Use assertions.
# test_diagonal: creates a diagonal image generator, generates a random image, and makes sure it is diagonally symmetric
# test_gradient: create a gradient image generator, generate a random image, calculate the angle used to generate the image from the seed (you can use your own method here),
#                sample 50 random points from the image, calculate their position along the gradient, make sure the values are close
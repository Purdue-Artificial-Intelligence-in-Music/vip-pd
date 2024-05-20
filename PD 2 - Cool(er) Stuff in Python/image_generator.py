import numpy as np

# In this class, image values are grayscale from 0.0 to 1.0 (black to white).

class Image_Generator:
    '''
    Image_Generator is a basic class that generates images.
    '''
    def __init__(self, image_size: int, name: str):
        self.image_size = image_size
        self.name = name
        # TODO: other initialization as needed

    def generate_image(self, seed: int) -> np.array:
        # Returns an image_size x image_size array filled with numbers sampled from a Normal distribution with mean 0.5 and variance 0.1.
        # Hint: use numpy.
        # TODO: Write this code.
        pass

class Diagonal_Pattern_Generator(Image_Generator):
    '''
    Diagonal_Pattern_Generator is a class that generates cool diagonally symmetric patterns.
    '''
    # TODO: Write an __init__ method that initializes the superclass object.
    # TODO: Also write a generate_image method that takes in a numerical seed and generates an image that's symmetric across the diagonals and is NOT a solid color.
    # TODO: Make the design randomly vary with the seed.
    # Your choice of what the design is. Spend as little or as much time as you want.
    # Hint: if you're lazy, what are some of the cheapest ways you can take an existing image and make it diagonally symmetric?
    pass

class Gradient_Generator(Image_Generator):
    '''
    Diagonal_Pattern_Generator is a class that generates black to white gradients in random directions.
    '''
    # TODO: Write an __init__ method that initializes the superclass object.
    # TODO: Also write a generate_image method that generates a gradient from black to white in a specified angle.
    # TODO: Make the angle randomly vary with the seed.
    # TODO: Also draw a line on top of the image in all gray (0.5) that is parallel to the gradient and passing through the middle of the image.
    pass
from image_generator import *
import threading
import numpy as np
import matplotlib.pyplot as plt
import os

# TODO: Write ABSL flags for the command line to control the parameters of this app.
# Flags you need are image sizes for both generators plus a starting seed value
# Write a comment explaining how to use the flags.

class GeneratorThread(threading.Thread):
    '''
    GeneratorThread is a thread that manages the generation of images based on a Image_Generator.
    It generates one image every second, plots it, and saves it to disk.
    '''

    def __init__(self, generator: Image_Generator, start_seed: int):
        super(GeneratorThread, self).__init__()
        self.generator = generator
        self.counter = 0
        self.start_seed = start_seed
        # TODO: do any other initialization here.

    def run(self):
        # TODO: while not stopped, generate one image every 3 seconds, using the seed = start_seed + counter
        # TODO: plot this image using plt including axes labels for the pixel number and a title stating the name of the generator
        # TODO: save this plot with the filename "<generator_name>_image<counter>.png", increment the counter, and start generating the next image
        pass

def main(argv):
    if not os.path.exists("image_outputs/"):
        os.mkdir("image_outputs/")

    # TODO: add an option to specify a seed in the command line using ABSL
    seed = int(np.random.uniform(0, 10000))

    # TODO: Create two GeneratorThreads, one with a Diagonal generator and one with a Gradient generator.
    try:
        # TODO: Start both and let them run
        pass
    except KeyboardInterrupt:
        # TODO: Stop both GeneratorThreads without requiring a force-kill from the system
        pass
    
if __name__ == "__main__":
    # TODO: what goes here?
    pass
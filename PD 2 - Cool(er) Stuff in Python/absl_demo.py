from absl import app, flags

# Flags are the command line arguments your program is expecting
# The syntax follows the format (name, default, (enum options if an enum), help_text)
# Several common options are:
# Enum: choose from a few preset programmer-defined choices
# String: self explanatory
# Integer: self explanatory
flags.DEFINE_enum('cool_letter', 'A', ['A', 'B','C'], 'A cool letter (one of the first three in the English alphabet)')
flags.DEFINE_string('name', 'Marty McFly', None)
flags.DEFINE_integer('number', 0, None)

# For programming ease
FLAGS = flags.FLAGS

def main(argv):
    print("Hi my name is %s, my favorite letter is %s and my number is %d!" % (FLAGS.name, FLAGS.cool_letter, FLAGS.number))

# Need this bit to run the code properly
if __name__ == "__main__":
    app.run(main)
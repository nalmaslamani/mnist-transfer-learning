# import the necessary packages
import os

# initialize the path to the *original* input directory of images
ORIG_INPUT_DATASET = "MNIST_Labels"

# initialize the base path to the *new* directory that will contain
# our images after computing the training and testing split
BASE_PATH = "mnist_dataset"

# define the names of the training, testing, and validation
# directories
TRAIN = "mnist_training"
TEST = "mnist_evaluation"
VAL = "mnist_validation"

# initialize the list of class label names
CLASSES = ["0", "1", "2", "3", "4", "5", "6", "7","8", "9"]

# set the batch size
BATCH_SIZE = 32

# initialize the label encoder file path and the output directory to
# where the extracted features (in CSV file format) will be stored
LE_PATH = os.path.sep.join(["output", "le.cpickle"])
BASE_CSV_PATH = "output"

# set the path to the serialized model after training
MODEL_PATH = os.path.sep.join(["output", "model.cpickle"])

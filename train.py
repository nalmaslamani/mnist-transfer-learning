# USAGE
# python3 train.py

# import the necessary packages
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from pyimagesearch import config
import numpy as np
import pickle
import os

def load_data_split(splitPath):
	# initialize the data and labels
	data = []
	labels = []

	# loop over the rows in the data split file
	for row in open(splitPath):
		# extract the class label and features from the row
		row = row.strip().split(",")
		label = row[0]
		features = np.array(row[1:], dtype="float")

		# update the data and label lists
		data.append(features)
		labels.append(label)

	# convert the data and labels to NumPy arrays
	data = np.array(data)
	labels = np.array(labels)

	# return a tuple of the data and labels
	return (data, labels)

# derive the paths to the training and testing CSV files
trainingPath = ('./output/mnist_training.csv')
testingPath = ('./output/mnist_evaluation.csv')

# load the data from disk
print("[INFO] loading data...")
(trainX, trainY) = load_data_split(trainingPath)
(testX, testY) = load_data_split(testingPath)

# normalisation

trainX=trainX/np.amax(trainX)
testX=testX/np.amax(trainX)

# Test Prent

# load the label encoder from disk
le = pickle.loads(open(config.LE_PATH, "rb").read())

# train the model
print("[INFO] training model...")
model = LogisticRegression(solver="lbfgs", multi_class="auto", max_iter=150) #150
model.fit(trainX, trainY)

# evaluate the model
print("[INFO] evaluating...")
preds = model.predict(testX)
print(classification_report(testY, preds, target_names=['0','1','2','3','4','5','6','7','8','9']))#le.classes_

# serialize the model to disk
print("[INFO] saving model...")
f = open(config.MODEL_PATH, "wb")
f.write(pickle.dumps(model))
f.close()



# The Problem:
Create a <i>Machine</i> that received an input a sequence of play can predict who is the winner (X or O)

# The Data:

The dataset is a collection of game sequences formed by (X, O, B), each one matches a label with the result of the match.

For data and further information click here
https://archive.ics.uci.edu/ml/datasets/Tic-Tac-Toe+Endgame


# The Solution:

I've create a Python module that transform the literal initial dataset into a numeric dataset, then I’ve divided this dataset into training set and validation set with Cross Validation technique.

I've compared the performances of some machine learning models e.g. SVM, Decision Tree and Neural Network, using three values for the training set: 20%, 50%, 80%

The result is in the image below.



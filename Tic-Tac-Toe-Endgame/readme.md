# The Problem:
Create a <i>Machine</i> that received an input a sequence of play can predict who is the winner (X or O)

This picture summarize the problem
<img src="https://github.com/gentilew/Machine-Learning-Pills/blob/master/Tic-Tac-Toe-Endgame/game_seq.png" alt="">

# The Data:

The dataset is a collection of game sequences formed by (X, O, B), each one matches a label with the result of the match.

For data and further information click here
https://archive.ics.uci.edu/ml/datasets/Tic-Tac-Toe+Endgame


# The Solution:

I've create a Python module that transform the literal initial dataset into a numeric dataset, then I’ve divided this dataset into training set and validation set with Cross Validation technique.

I've compared the performances of some machine learning models e.g. SVM, Decision Tree and Neural Network, using three values for the training set: 20%, 50%, 80%

The result is in the image below.

<img src="https://github.com/gentilew/Machine-Learning-Pills/blob/master/Tic-Tac-Toe-Endgame/output.png" width="60%" height="60%" alt="">

## How To Use:

Download 
<ul>
<li>TicTacToe_Predictor.py</li> 
<li>TicTacToe_Dataset.csv </li>
</ul>

## Requirements
<ul>
<li>Python V. 2.7 or later</li>
<li>pandas V. 0.19 or later</li>
<li>matplotlib V. 1.5 or later</li>
<li>scikit_learn V.0.18 or later </li>
</ul>

### Acknowledgement
Lichman, M. (2013). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science. 

##############################################################################################################################################################################################
#Created by: Walter Gentile on September 2017
# 
#Ver. 1.0
#
#Credits for data: Lichman, M. (2013). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science. 
#Dataset: https://archive.ics.uci.edu/ml/datasets/Tic-Tac-Toe+Endgame
#
#Released under
#MIT License
#
#Copyright (c) [year] [fullname]
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
##############################################################################################################################################################################################
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier

from sklearn.model_selection import train_test_split

# Retrieve integer position of a symbol in a game sequence
def getPositionOfSymbol(seq, symbol, pos):
    i = -1
    for j in xrange(pos):
        i = seq.index(symbol, i + 1)
    return i + 1;
    

# Transform a literal sequence of game (x,o,b) in a integer sequence
def getNumericSequenceOfGame(seq):
    numX = seq.count('x');
    numO = seq.count('o');
    numB = seq.count('b');
    count   = 0
    sog     = []

    for i in xrange(1,min(numX,numO)+1):
        sog.append(getPositionOfSymbol(seq,'x',i))
        sog.append(getPositionOfSymbol(seq,'o',i))
        count = count + 1;

    if(numX > numO):
        sog.append(getPositionOfSymbol(seq,'x',numX));

    elif(numX < numO):    
        sog.append(getPositionOfSymbol(seq,'o',numO));
                                     
    if(numB != 0):
        for k in xrange(1,numB+1):
            sog.append(getPositionOfSymbol(seq,'b',k));
            
    return(sog);            


# Load initial data from CSV file
def LoadDataFromCSV(fileName):
    
    #Data Load from file
    df = pd.read_csv(fileName, delimiter=',', header=None)

    sequenceGame = []
    labels       = []

    #Split data in sequence game and label class
    for row in df.itertuples():
        sequenceGame.append(row[1].split(';')[0:9])
        labels.append(row[1].split(';')[9:10])

    return sequenceGame,labels;     

################################################################################# MAIN PROGRAM ##################################################################################                                  

# Retrieve literal data from CSV
sequence, labels = LoadDataFromCSV('<%your_local_folder%>\TicTacToe_Dataset.csv')

# Trasform literal data into numeric data
numericLabels = [1 if l[0] == 'positive' else -1 for l in labels]

numericSequences = []
for sq in sequence:
    numericSequences.append(getNumericSequenceOfGame(sq));


# Machine Learning section: this is a Supervised Classification problem.
# In order to find the best solution, we compare three classification models: Support Vector Machine, Decision Tree, Neural Network 
names = ["SVM","Decision Tree","Neural Network"]
classifiers = [SVC(),DecisionTreeClassifier(),MLPClassifier(alpha=1,activation='relu')]

# Split the data by CrossValidation using several size of test set
test_size = [0.30,0.50,0.80]

for ts in test_size:
    X_train, X_test, y_train, y_test = train_test_split(numericSequences, numericLabels, test_size=ts,random_state=0)

# For each data of test set we calculate the score of all machine learning models
    scores = []
    for clf in classifiers:
        clf.fit(X_train,y_train)
        scores.append(clf.score(X_test,y_test))


    plt.plot(scores)
    plt.xticks(range(len(names)), names)

# Plot the results into one figure in order to compare the performaces
plt.grid()
plt.legend(test_size)
plt.show()        
    
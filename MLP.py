import numpy as np
import pandas as pd
import os
# Load data
data=pd.read_csv('dataset.csv')

X=data[['age','react','javascript','html','css','python', 'experience', 'language']]
print(X)
y=data['status']

# Import train_test_split function
from sklearn.model_selection import train_test_split

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state=42)  # 70% training and 30% test
from sklearn.neural_network import MLPClassifier

# Create model object
clf = MLPClassifier(hidden_layer_sizes=(6,5),random_state=5,verbose=True,learning_rate_init=0.03)

# Fit data onto the model
clf.fit(X_train,y_train)

ypred=clf.predict(X_test)

# Import accuracy score
from sklearn.metrics import accuracy_score

# Calcuate accuracy
print(accuracy_score(y_test,ypred))

#########################################

resume_csv = pd.read_csv('test.csv')

resume_status = clf.predict(resume_csv)

########################################

if resume_status[0]==1:
    print("ACCEPTED")
    no_f = open("./ACCEPTED/number","r")
    no = int(no_f.read()) + 1
    os.system("cd ./ACCEPTED && touch "+str(no)+".txt && cd .. && cat ./input/resume.txt > ./ACCEPTED/"+str(no)+".txt")
    os.system("echo "+str(no)+" > ./ACCEPTED/number")
else:
    print("REJECTED")
    no_f = open("./REJECTED/number","r")
    no = int(no_f.read()) + 1
    os.system("cd ./REJECTED && touch "+str(no)+".txt && cd .. && cat ./input/resume.txt > ./REJECTED/"+str(no)+".txt")
    os.system("echo "+str(no)+" > ./REJECTED/number")

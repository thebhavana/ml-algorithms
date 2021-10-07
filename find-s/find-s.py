import pandas as pd
df = pd.read_csv("data.csv")
dataset = df.values.tolist()
rows = len(dataset)
columns = len(dataset[0])-1
print("\nThe initial value of hypothesis:")
#Initialize the hypothesis
hypothesis = ['phi'] * columns
print(hypothesis)
#Training with the first instance
for i in range(0,columns):
    hypothesis[i] = dataset[0][i]
#Training the dataset
for i in range(0,rows):
    if dataset[i][columns]=='YES':
        for j in range(0,columns):
            if dataset[i][j]!=hypothesis[j]:
                    hypothesis[j]='?'
            else:
                    hypothesis[j]=dataset[i][j]
            print("\n After {0} iteration, the hypothesis is :".format(i),hypothesis)
print("\nHypothesis after training :")
print(hypothesis)

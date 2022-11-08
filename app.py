# IMPORT MODULES
# Numpy & Pandas
import pandas as pd
import numpy as np
# Selected Model
from sklearn.ensemble import RandomForestClassifier

# IMPORT DATA
# Train
train = pd.read_csv('data/train.csv', delimiter=';')
# Test
test = pd.read_csv('data/test.csv', delimiter=';')

# X Y SPLIT
X = train.drop(['target', 'feature5', 'feature7', 'feature8'], axis=1)
y = train['target']

# MODEL
# Fine Tune Model
rf = RandomForestClassifier(random_state = 5)

#fit Model
rf.fit(X, y)

#preprocess test
test = test.drop(['feature5', 'feature7', 'feature8'], axis=1)

#Prediction
prediction = rf.predict(test)

#EXPORTAR PREDICCIÓN
df_prediction = pd.DataFrame(prediction, columns=['target'])

#export a csv
df_prediction.to_csv(r'predictions.csv', index = False)

#export a json
json_prediction = df_prediction.to_json()
with open('predictions.json', 'w') as outfile:
    outfile.write(json_prediction)
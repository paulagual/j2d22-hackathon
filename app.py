# IMPORT MODULES
# Numpy & Pandas
import pandas as pd
import numpy as np
# Selected Model
from sklearn.ensemble import ExtraTreesClassifier

# IMPORT DATA
# Train
train = pd.read_csv('data/train.csv', delimiter=';')
# Test
test = pd.read_csv('data/test.csv', delimiter=';')

# X Y SPLIT
X = train.drop(['target'], axis=1)
y = train['target']

# MODEL
# Fine Tune Model
et_hh = ExtraTreesClassifier(random_state = 5,criterion = 'entropy', n_estimators=100, class_weight='balanced')
#fit Model
et_hh.fit(X, y)
#Prediction
prediction = et_hh.predict(test)

#JSON EXPORT TO FILE
df_prediction = pd.DataFrame(prediction, columns=['target'])
json_prediction = df_prediction.to_json()
with open('predictions.json', 'w') as outfile:
    outfile.write(json_prediction)
# Got the mobile price classification dataset from kaggle.com
from sklearn.feature_selection import chi2
from sklearn.feature_selection import SelectKBest
import numpy as np 
import pandas as pd

data=pd.read_csv('train.csv')
data

X = data.drop('price_range',axis=1)
X.shape

y=data['price_range']
y.shape

"""## Selecting the top 10 features using chi2 method"""

# selecting the top ten features
best_features = SelectKBest(score_func=chi2,k=10).fit(X,y)

# now we are applying our SelectKBest on our training data
feature_score = best_features.fit(X,y)

# Now we will get the importance of each feature in terms of numbers
feature_score = feature_score.scores_

feature_score

df_scores = pd.DataFrame(data = feature_score)
df_scores

df_columns = X.columns
df_columns = pd.DataFrame(data = df_columns)
df_columns

df_feature_score = pd.concat([df_columns,df_scores],axis=1)
df_feature_score.columns=['Features','Importance_Score']
df_feature_score

df_feature_score = df_feature_score.sort_values(by=['Importance_Score'],ascending = False)

df_feature_score

new_X = df_feature_score.head(10)['Features'].values
new_X

X = X[new_X]
X

from sklearn.ensemble import RandomForestClassifier


rfc = RandomForestClassifier()

model = rfc.fit(X,y)

test_data = pd.read_csv('test.csv')
test_data

test_X = test_data[new_X]

test_X

predictions = model.predict(test_X)
predictions

model.score(X,y)

model.predict([[3,1440,3000,720,145,32,6,6,5,5]])


import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)

columns_read = ['Profile', 'Player', 'Season', 'Year', 'Team', 'Winner',
                'Goals', 'Assists', 'Plus', 'Minus', 'Penalties',
                'Shots', 'Hits', 'Shots_blocked',
                'Penalties_against', 'Icetime_seconds', 'Rating'
                ]
data = pd.read_csv('../forward/forwards_match_with_rating.csv', usecols=columns_read)

data = data[data['Icetime_seconds'] >= 480]
data = data[data.groupby(['Profile', 'Year']).Profile.transform('count') >= 20]

forwards_data = data.groupby(['Profile', 'Year'])

y = data['Rating'].copy()
X = data.drop('Profile', 'Player', 'Season', 'Year', 'Team', 'Winner', 'Rating', axis=1).copy()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print(X_test.head())

linear = LinearRegression(n_jobs=-1)
linear.fit(X_train, y_train)
y_pred = linear.predict(X_test)

print('MSE:', mean_squared_error(y_pred, y_test, squared=True))
print('RMSE:', mean_squared_error(y_pred, y_test, squared=False))
print('MAE:', mean_absolute_error(y_pred, y_test))
print('R_squared:', r2_score(y_pred, y_test))

linear_coef = pd.DataFrame(zip(X.columns, linear.coef_))
linear_coef.columns = ['Feature', 'Coefficient']
print(linear_coef)

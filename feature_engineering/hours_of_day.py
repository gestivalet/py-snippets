#--- create some simulated data
from random import randint
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ser = pd.Series([randint(0, 23) for i in range(1_000)])
df = pd.DataFrame(ser, columns=['hour_of_day'])



#--- sin/cos transformation for hours of day
def transform_hour_sin(value, max_value):
    '''The sine function provides symmetrically opposite weights to corresponding AM and PM hours.
       It captures the cyclical nature of hours of the day.'''
    return np.sin(value * (2.*np.pi/max_value))

def transform_hour_cos(value, max_value):
    '''The cosine function provides symmetrically equal weights to corresponding AM and PM hours.
       It captures the cyclical nature of hours of the day.'''
    return np.cos(value * (2.*np.pi/max_value))


#--- apply transformations
max_hour = df['hour_of_day'].max()
print(max_hour) # could be 23 or 24 (or even on AM/PM format)

df['hour_sin'] = df['hour_of_day'].apply(lambda x: transform_hour_sin(x, max_hour))
df['hour_cos'] = df['hour_of_day'].apply(lambda x: transform_hour_cos(x, max_hour))



#--- Plot: visualize the transformation
arr_sin = df.loc[:, ['hour_of_day', 'hour_sin']].drop_duplicates().sort_values(by='hour_of_day')['hour_sin'].values
arr_cos = df.loc[:, ['hour_of_day', 'hour_cos']].drop_duplicates().sort_values(by='hour_of_day')['hour_cos'].values

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(arr_sin, label='sin')
ax.plot(arr_cos, label='cos')
plt.legend()
plt.show()
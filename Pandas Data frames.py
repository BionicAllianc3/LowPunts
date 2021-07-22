import numpy as np
import pandas as pd

players = ['Mane', 'Abraham', 'Martial', 'Salah', 'Kane']
goals = ['Goals', 'Apps', 'Shots', 'Min/Goal']
data = pd.DataFrame(data = {'Goals':[14,10,9,9,9], 'Apps':[13,16,12,13,16], 'Shots':[26,32,21,21,25],
                            'Min/Goal':[74.71,33.40,100,106.22,155.56]}, index= players, columns=goals )
print(data)

print(data['Goals'])
#To printout the column for goals
print(data.loc['Mane'])
print(data.iloc[1:4])
print(data[0:4])
states = {'lagos':{'population': 5534, 'job opportunities': 'Maximum', 'stress levels': 'Maiximum'},
          'Ogun': {'population': 5100, 'job opportunitues': 'above average', 'stress levels': 'not up to maximum'},
          'Ibadan': {'population': '5400', 'job opportunities': 'near maximum', 'stress levels': 'no stress'}}
print(states)
print(states.keys())
print(states['Ogun'])
del states['Ogun']
print(states)
states['Ogun'] = {'population': 5300, 'jobOpportunities': 'improving', 'stressLevels': 'no where near that of lagos'}
print(states)
print(states['lagos'])

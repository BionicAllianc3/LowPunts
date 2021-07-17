europe = {'spain': {'population': 56.4, 'capital': 'madrid',},
          'france': {'population': 45.3, 'capital': 'paris'},
          'nigeria': {'population': 96.2, 'capital': 'abuja'},
          'england': {'population': 32.8, 'capital':'london'}}

print(europe)
print(europe['spain']['capital'])
newCountry = {'population': 29.5, 'capital': 'accra'}
europe['ghana'] = newCountry
print(europe)
anothercountry = {'population':67, 'capital':'porto'}
europe['portugal'] = anothercountry
print(europe)
newlycreatedcountry = {'population': 36.3, 'capital': 'Johannesburg'}
europe['South Africa'] = newlycreatedcountry
print(europe)
del(europe['ghana'])
print(europe)
europe['portugal'] = {'popluation': 78, 'capital': 'porto'}
print(europe)
africa = {'nigeria': 'Abuja', 'tribe': ['yoruba', 'hausa', 'Igbo'], 'population': '355',}
del(africa['population'])

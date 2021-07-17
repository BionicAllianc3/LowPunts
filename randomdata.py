import random

#random to get a random value between 0 and 1 (0 is inclusive and 1 isn't)
#value = random.random()
#print(value)

# to get a random value between ranges
#uniform is for floats and randint is for integers
#note that these two take arguments

#values = random.uniform(4,7)
#print(values)

#number = random.randint(4,7)
#print(number)

#choice picks a randon value for a list of values
#example
'''greeting = ['Hello', 'Hola', 'E kaaro']
value = random.choice(greeting,)
print(value)
'''
#to get multiple values form a list we use choices
'''color = ['Red', 'Blue', 'Pink']
results = random.choices(color, weights= [23, 23, 10], k = 23)
#k means how many times /results
print(results)
'''

#to randomly shuffle a list of values

#print(deck)

#to shuffle
'''deck = list(range(1,53))
random.shuffle(deck)
print(deck)
'''

#to get a random list of unique numbers without repitition we use "sample"

'''
deck = list(range(1,53))
hand = random.sample(deck, k = 4)
print(hand)
'''
import random

firstNames = ['Oreoluwa', 'Samuel', 'Joseph', 'Bola', 'Kemi', 'Michael', 'John', 'Dami', 'Ruth', 'Tosin', 'Yemi',
              'Caroline', 'Bolu', 'Tolu', 'Praise', 'Queen', 'Precious', 'Limon', 'Escobar', 'Biola', 'Peju', 'Segun',
              'Christian']
lastNames = ['Akinbo', 'Adeyemi', 'Ayeni', 'Ositelu', 'Elewa', 'Olatunji', 'Babatunde', 'Ajumobi', 'Lawal', 'Fiona',
             'Akeredolu', 'Adurosakin', 'Fadele', 'Falade', 'Olukoya', 'Iwealor', 'Daniels', 'Igboho', 'Raine', 'Odejobi',
             'Mojolaoluwa']
fakestates = ['Lagos', 'Ogun', 'Ekiti', 'Niger', 'Kano', 'Edo', 'Benin', 'Adamawa', 'Kaduna', 'Jos', 'Oyo', 'Osun', 'Abuja',
          'Rivers', 'Kwara', 'Kogi', 'Nassarawa']
fakestreet = ['Pastor Ayeni Avenue', 'Aletile', 'Church road', 'Mystique close', 'Jonathan Akpan close', 'Unity street',
          'Adesan', 'Peace estate', 'Aba Erinfun']

'''
for num in range(50):
    first = random.choice(firstNames)
    last = random.choice(lastNames)

    streetnum = random.randint(1,30)
    streets = random.choice(fakestreet)
    states = random.choice(fakestates)
    address = f'{streetnum}, {streets} st.,\n{states}'
    phoneNumber = f'0813-{random.randint(234,967)}-{random.randint(1000,4000)}'
    print(f'{first} {last}\n{address}\n{phoneNumber}\n')
'''
value = random.random()
print(value)
valo = int(random.random()*50)
print(valo)
#A dictionary of Manchester united's first team lineup with their jersey numbers
#Starting with Centrebacks

manchesterUnited = {'David de Gea': 1, 'Aaaron Wan Bissaka': 29, 'Victor Lindelof': 2, 'Harry Maguire': 5,
                    'Luke Shaw':23, 'Fred': 17, 'Paul Pogba': 6, 'Bruno Fernandes': 18}

print(manchesterUnited)

#Lets's add to the dictionary, the front 3!

leftwinger = 10
manchesterUnited['Marcus Rashford'] = leftwinger
rightwinger = 11
manchesterUnited['Mason Greenwood'] = rightwinger
centreforward = 7
manchesterUnited['Edison Cavani'] = centreforward

#now let's print out an updated list of our dictionary

print(manchesterUnited)

#to print the keys of this dictionary, we make use of the .keys fuction

print(manchesterUnited.keys())

#to print the values of this dictionary, we make use of the .values fuction

print(manchesterUnited.values())






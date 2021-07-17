cost = [12000, 28210, 23800, 60500, 76500]
modelInRam = [21039.3, 423233, 10932.44, 3642.44,]
phonemake = cost+modelInRam
summed = sorted(phonemake, reverse=False)
anotherSum = sorted(phonemake, reverse= True)
print(anotherSum)
print(summed)


wholeNumber = [5, 8, 23, 35]
improperNumber = [4.5, 7.8, 66.5, 70.2]
mix=wholeNumber+improperNumber
mixed = sorted(mix, reverse=True)
print(mixed)


first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]
full = first + second
fullSorted = sorted(full, reverse = False)
print(fullSorted)

#False is for ascending order, true is for descending order

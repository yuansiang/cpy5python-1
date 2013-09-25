Animal = []
Animal.append("SNAKE")
Animal.append("CAT")
Animal.append("LION")
Animal.append("WOLF")
Animal.append("TIGER")
Animal.append("GIRAFFE")
Animal.append("HORSE")
Animal.append("ZEBRA")
Animal.append("LIZARD")
Animal.append("BEAR")
Animal.append("CROCODILE")
Animal.append("AARDVARK")
Animal.append("ALLIGATOR")

swapped = True
while swapped:
	swapped = False
	for i in range(1,len(Animal)):
		if Animal[i-1] > Animal[i]:
			Animal[i-1],Animal[i] = Animal[i],Animal[i-1]
			swapped = True
print(Animal)
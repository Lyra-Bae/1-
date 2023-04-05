# 4. 
animals = ('lion', 'tiger', 'penguin', 'dog', 'cat')
animals = list(animals)

tmp = list()

for animal in animals: 
    if animal.find('e') != -1:
        tmp.append(animal)

animals = tuple(tmp)

print(animals)
# let's create a dictionary with its key value pair

fav_novel = {
    'steve': 'Factfullness',
    'Amisha': 'Kafka on the shore',
    'amit': 'The Trail',
    'mick': 'Art of war'
}

# let's print something from key value pair.

print(fav_novel)
novel = fav_novel['Amisha'].upper()
print(f"Amisha's favorite book is {novel}.")

# let's use get method to pull out value of a key

john_fav = fav_novel.get('john', 'No book assign')
print(john_fav)

# let's loop through each key value pair and print names and novels separately

fav_novel = {
    'steve': 'Factfullness',
    'Amisha': 'Kafka on the shore',
    'amit': 'The Trail',
    'mick': 'Art of war'
}
for name in fav_novel.keys():
    print(name)

# using loop to print novels

for novel in fav_novel.values():
    print(novel)

# let's print key value pair together for each element in the dictionary.

for key, value in fav_novel.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

#

fav_novel = {
    'steve': 'Factfullness',
    'Amisha': 'Kafka on the shore',
    'amit': 'The Trail',
    'mick': 'Art of war'
}

for name in fav_novel:
    print(name.title())

fav_novel = {
    'steve': 'Factfullness',
    'Amisha': 'Kafka on the shore',
    'amit': 'The Trail',
    'mike': 'Art of war'
}

friends = ['steve', 'mike']

for name in fav_novel:
    print(f"Hi {name.title()}")

    if name in friends:
        book = fav_novel[name].title()
        print(f"\t{name.title()}, I see you love {book}!")

#

if 'Eric' not in fav_novel.keys():
    print("Eric, Please take our poll.")

#

fav_novel = {
    'steve': 'Factfullness',
    'Amisha': 'Kafka on the shore',
    'amit': 'The Trail',
    'mike': 'Art of war',
    'Jordan': 'Kafka on the shore'
}

for name in sorted(fav_novel.keys()):
    print(f"{name.title()}, Thank you for taking the poll.")


# Print the values of the keys, Un-Uniquely , return a results if values(all of it)
print("\nThese are the Books People mentioned:")
for novel in fav_novel.values():
    print(novel.title())

#  Print the values of the key using set method, Uniquely , returns non-repetitive values of the key.
print("\nThese are the Books People mentioned:")
for novel in set(fav_novel.values()):
    print(novel.title())

















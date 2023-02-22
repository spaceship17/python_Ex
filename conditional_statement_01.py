# let's create a list of items and use for and if statement together to loop through each items.

requested_toppings = ['macroni', 'jalpino', 'extracheese', 'panner']
for requested_topping in requested_toppings:
    if requested_topping == 'jalpino':
        print(f"Sorry we ran out of {requested_topping}")
    else:
        print(f"Adding {requested_topping}")

print(f"\nFinished making your pizza!")

# let's create an empty list and find the items in the empty list.
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}")
    print(f"Finished making your pizza")
else:
    print("Are you sure you want plain pizza?")

# let's loop through multiple lists using for loop and if statements

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"sorry we dont have {requested_topping}")

print(f"\nFinished making your pizza")

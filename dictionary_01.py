# let's create a dictionaries of aliens and print them

alien_01 ={'color': 'green', 'point': 5}
alien_02 ={'color': 'red', 'point': 8}
alien_03 ={'color': 'orange', 'point': 4}
print(alien_01, alien_02, alien_03)

# let's print the value of color(key) of each pair.
print(alien_01['color'])
print(alien_02['color'])
print(alien_03['color'])

# let's print the value of another key using variable assigning method
new_point_01 = alien_01['point']
print(new_point_01)

new_point_02 = alien_02['point']
print(new_point_02)


print(alien_03['point'])

# let's use different ways of printing the key value pair in different-different fashion
print(alien_01['color'], alien_02['color'], alien_03['color'])

# let's add some more keys and it's respective pairs in one of the exiting dictionary named alien_01
alien_01['style'] = 'defensive'
alien_01['x_position'] = 2
alien_01['y_position'] = -1
print(alien_01)

# let's create an empty dictionary and add the key value pairs thereafter
alien_00 = {}
alien_00['color'] = 'white'
alien_00['point'] = 6
print(alien_00)
print(f"\nThe alien is now {alien_00['color']}.")

# let's create one more dictionary and use if statement to play around with the key and its pair
alien_00 = {'color': 'white', 'point': 6, 'x_position': 2, 'y_position': 10, 'speed': 'medium'}

if alien_00['speed'] == 'slow':
    x_increment = 1
elif alien_00['speed'] == 'medium':
    x_increment = 3
else:
    x_increment = 5
alien_00['x_position'] += x_increment
print(alien_00['x_position'])

alien_00 = {'color': 'white', 'point': 6, 'x_position': 2, 'y_position': 10, 'speed': 'fast'}

if alien_00['speed'] == 'slow':
    x_increment, y_increment = 1, 2
elif alien_00['speed'] == 'medium':
    x_increment, y_increment = 3, 5
else:
    x_increment, y_increment = 6, 7
alien_00['x_position'] += x_increment
alien_00['y_position'] += y_increment
print(alien_00['x_position'])
print(alien_00['y_position'])


alien_00 = {'color': 'white', 'point': 6, 'x_position': 2, 'y_position': 10, 'speed': 'medium'}
alien_01 = {'color': 'green', 'point': 5, 'x_position': 3, 'y_position': 12, 'speed': 'fast'}

if alien_00['speed'] == 'slow' or alien_01['speed'] == 'slow':
    x_increment, y_increment = 1, 2
elif alien_00['speed'] == 'medium' or alien_01['speed'] == 'medium':
    x_increment, y_increment = 3, 5
else:
    x_increment, y_increment = 6, 7
alien_00['x_position'] += x_increment
alien_00['y_position'] += y_increment

alien_01['x_position'] += x_increment
alien_01['y_position'] += y_increment

# This code reflects to the idea where i want to print the both x and y positions of a alien_00 and alien_01
# in one single line of code.
print(alien_00['x_position'], alien_00['y_position'])
#print(alien_00['y_position'])

print(alien_01['x_position'], alien_01['y_position'])
#print(alien_01['y_position'])










"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with 
lists!). 

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictinaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "Texas"
    }, 
    {
        "lat": 41,
        "lon": -123,
        "name": "Cali"
    }, 
    {
        "lat": 43,
        "lon": -122,
        "name": "Houston"
    }
]

# Add a new waypoint to the list
waypoints.append({
    "lat": 49,
    "lon": -180,
    "name": "PEI"
})
print(waypoints)

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# YOUR CODE HERE

# Write a loop that prints out all the field values for all the waypoints
for item in waypoints:
    print(item.values())
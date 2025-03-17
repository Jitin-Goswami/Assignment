# Random Story Generator


import random

# Lists of story elements
characters = ["a wizard", "a pirate", "an astronaut", "a detective", "a dragon", "a knight"]
places = ["in a haunted castle", "on a mysterious island", "in outer space", "in a deep jungle", "in an underground cave"]
actions = ["found a hidden treasure", "discovered a secret door", "fought a giant monster", "made a surprising discovery", "escaped from danger"]
objects = ["a magical sword", "an ancient map", "a talking cat", "a golden key", "a mysterious book"]

# Function to generate a random story
def generate_story():
    character = random.choice(characters)
    place = random.choice(places)
    action = random.choice(actions)
    obj = random.choice(objects)

    return f"One day, {character} was {place} and {action} with {obj}."

# Generate and display a random story
print(generate_story())

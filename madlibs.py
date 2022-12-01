from random import choice


# Ask input from user for the adjective, verbs and the name.
adjective = input("Please enter an adjective: ")
verb1 = input("Please enter a verb: ")
verb2 = input("Please enter another verb: ")
name = input("Please enter the name of someone you admire: ")

# Create a list with a few paragraphs to form phrases. Leave 1 adjective, 2 verbs and one name as a variable.
options = [
    f"My job is so {adjective}, that sometimes I'd like to {verb1},\
 but then I cool down and it passes. But maybe I should just {verb2} like {name}.",
    f"I'm a {adjective} person, I try to be like {name}.\
 I {verb1} all the time and {verb2} whenever I can.",
    f"I {verb1} the zoo, it's so {adjective}.\
 I want to {verb2} all day long, until {name} appears."
]

# Select a random paragraph from the list.
phrase = choice(options)

# Print the result.
print(phrase)

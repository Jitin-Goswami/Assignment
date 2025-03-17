# Acronyms Creator


def generate_acronym(phrase):
    words = phrase.split()
    acronym = "".join(word[0].upper() for word in words)
    return acronym

# Get user input
phrase = input("Enter a phrase to generate an acronym: ").strip()
if phrase:
    print(f"Acronym: {generate_acronym(phrase)}")
else:
    print("Please enter a valid phrase!")

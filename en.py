import re

# Pattern to match three uppercase letters separated by spaces
acronym3_re = re.compile(r'([A-Z])\s*([A-Z])\s*([A-Z])')

# Example name
name = "A B C D E F G H I"

# Perform substitution to remove spaces between the letters
name = acronym3_re.sub(r'\1\2\3', name)

print(name)  # Output will be: "ABCDEF GHI"

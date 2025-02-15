import re

#regular String 
text = "Contact me at 123-456-89"

digits = re.findall(r"\d+", text)
print(digits)
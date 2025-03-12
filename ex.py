import re
def ali(s):
   return re.findall(r'[A-Z][a-z]+', s)
print(ali("Hello World test"))
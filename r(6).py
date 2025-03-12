import re
def zulk(s):
    return re.sub(r'[ ,.]' , ':', s)
print (zulk("Hello, world. How are you?"))
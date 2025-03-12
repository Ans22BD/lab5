import re
def stringg(s):
    return re.findall(r'\b[a-z]+_[a-z]+\b',s)
print(stringg("hello_world test_case"))



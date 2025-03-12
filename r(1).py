import re
def ali(s):
    apai = (r'^a*b*')
    return bool(re.fullmatch(apai,string))
   
   
print(ali("abbbb"))
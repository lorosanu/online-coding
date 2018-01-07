import re
text = input()
print(bool(
    re.search(r"^[MDCLXVI]+$", text) and 
    re.search(r"^M{,3}(CM|CD|D?C{,3})(XC|XL|L?X{,3})(IX|IV|V?I{0,3})$", text)))

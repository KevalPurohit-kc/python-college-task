import re

text = "Python was released in 1991. Python is popular and easy to learn."

print("match:", re.match(r"Python", text))
print("search:", re.search(r"popular", text).group())
print("findall:", re.findall(r"Python", text))

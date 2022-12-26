#string are immutable
a =  "Robin"
print(len(a))
print(a.upper())
print(a.lower())
b = "robin!!!!!!!!!!"
print(b.rstrip("!"))
print(a.replace("robin", "poonia"))

c = "robin pooniA is coder"
print(c.split(" "))
print(c.capitalize())
print(c.find("is"))
print(c.index("is"))
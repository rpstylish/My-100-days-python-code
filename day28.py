# f-string 
letter = "hey my name is {} and i form {}"
name = "robin"
country = "india"
print(letter.format(name, country))
print(f"hey my name is {name} and i form {country}")
print(f"hey my name is {{name}} and i form {{country}}")


prices = 49.359516
text = f"for only {prices: .2f} dollars!"
print(text)


print(f"{2 * 30}")
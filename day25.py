# # tuple manipulating
# countries = ("Spain","Italy","India","England","Germany")
# temp = list(countries)
# temp.append("Russia")  #add country
# temp.pop(3)      #remove country
# temp[2] = "Finland"
# countries = tuple(temp)
# print(countries)


# countries2 = ("Vietnam", "Intia", "China")
# southEastAsia = countries + countries2
# print(southEastAsia)


tuple1 = (0,1,2,3,2,3,1,3,2)
res = tuple1.count(3)
print('count of 3 in tuple1 is:', res)
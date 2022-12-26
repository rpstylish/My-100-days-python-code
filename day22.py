#list
l = [ 3,5,6, "robin"]
# print(l)
# print(l[0])
# print(l[1])
# print(l[2])
# l.append(4)
# print(l[3])
# print(l[4])
print(l[-3])

if 7 in l:
    print("yes")
else:
    print("no")
if "in" in "robin":
    print("yes")
else:
    print("no")
print(l[1:4])
print(l[1:4:2])
# list comprehension

list = [i for i in range(5)]
print(list)
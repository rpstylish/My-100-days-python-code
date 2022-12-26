# default argument
# def average(a, b=1): # a is required agument
#     print("the average is", (a+b)/2)

# average(5, 6)    
# average(6)    
# average(b=7)    
# average(b=7, a=21)    


# def average(*number):
#     sum = 0
#     for i in number:
#         sum = sum + i
#     print("average is:", sum / len(number))    

# average(4, 6)

def name(**name):
    print("Hello", name["fname"], name["lname"])

name(lname = "poonia", fname = "robin")    

    
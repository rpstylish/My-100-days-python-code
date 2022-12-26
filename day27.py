list1 = [  ['my name is', "robin poonia"], ['what are you studing now', "BCA 1st"], ['who many masks you get in 12th', "91%"], ['I have a question harry bhai, i am a hanhicap(50%) preson and i want be a SDE. now i am working as a web devloper ', 'yes or no'], ['i love DSA and i want to work at', 'google'], ['plz help me harry bhai', "thanks"],['youtube pe koi video nhi ki ek handicap bhi SDE ban sakta h kya', ' plz make a video']]

r = 0
print("KBC\n")
for i in list1:
    print(f"Ques: {i[0]}")
    ans = str(input("Ans: "))
    
    if str(i[1]) == ans:
        print("Congratulations! It is the correct answer\n")
        r += 50
        
    elif str(i[1]) != ans:
        print(f"Oops it is the wrong answer! Total Money Won: Rs. {r}")
        exit()
        
print(f"Congratulations! You won: {r}")
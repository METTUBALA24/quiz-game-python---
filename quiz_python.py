d={}
c1=0
c2=0
c3=0
c4=0
c5=0
q1="what is the minimum legal age for girls in india"
q2=" when we celebrate independents day"
q3=" when we celebrate teachers day"
q4="zphs full form"
q5="who is the head of union governament in india"
while True:
    print("welcome to the quiz")
    print("1.store Q ON dic 2.TRACK SCORE 3.start quiz 4.check dic: 5.exit quiz")
    ch=int(input("Enter the above choice:"))
    if ch==3:
        print(" what is the minimum legal age for girls in india :")
        print("a.16   b. 18 c.21 d.17 ")
  
        option=input("Enter the option:")
        if option=="a":
            print("wrong answer:")
        elif option=="b":
            print("correct answer:")
            c1+=1
        elif option=="c":
            print("wrong answer:")
        elif option=="d":
            print("wrong answer:")
        else:
            print("invalid input")
    
        print(" when we celebrate independents day:")
        print("a. aug 15  b. dec 3   c. july 30 d. aug 14")
        option=input("Enter the option:")
        if option=="b":
            print("wrong answer:")
        elif option=="a":
            print("correct answer:")
            c2+=1
        elif option=="c":
                print("wrong answer:")
        elif option=="d":
                print("wrong answer:")
        else:
            print("invalid input")
        
        print(" when we celebrate teachers day:")
        print("a. aug 14  b. dec 20   c. sep 5 d. aug 14")
        option=input("Enter the option:")
        if option=="b":
            print("wrong answer:")
        elif option=="a":
             print("wrong answer:")
        elif option=="c":
            print("correct answer:")
            c3+=1
        elif option=="d":
                print("wrong answer:")
        else:
            print("invalid input")
        
        print(" zphs full form:")
        print("a.zilla parishad  b.zella perminent   c. zenda parlament d. zeera poul")
        option=input("Enter the option:")
        if option=="b":
            print("wrong answer:")
        elif option=="a":
             print("correct answer:")
             c4+=1
        elif option=="c":
            print("wrong answer:")
            
        elif option=="d":
                print("wrong answer:")
        else:
            print("invalid input")
            
        print(" who is the head of union governament in india:")
        print("a.president  b.cm    c.governer   d. prime minister")
        option=input("Enter the option:")
        if option=="b":
            print("wrong answer:")
        elif option=="a":
             print("wrong answer:")
        elif option=="c":
             print("wrong answer:")
        elif option=="d":
             print("correct answer:")
             c5+=1
        else:
            print("invalid input")
    elif ch==1:
        print("To store u need to follow the steps:")
        qch=input("Enter q number to save that perticuler question like q1,q2:")
        if qch=="q1":
            print(q1)
            d["q1"]=q1
            print("q1 added")
        elif qch=="q2":
            print(q2)
            d["q2"]=q2
            print("q2 added")
        elif qch=="q3":
            print(q3)
            d["q3"]=q3
            print("q3 added")
        elif qch=="q4":
            print(q4)
            d["q4"]=q4
            print("q4 added")
        elif qch=="q5":
            print(q5)
            d["q5"]=q5
            print("q5 added")
    elif ch==2:
         totalcount=c1+c2+c3+c4+c5
         print(f"tracked:{totalcount} is corrected from all quesions")
    elif ch==4:
        print(f"your dictionary:{d}")
        if d=={}:
            print("empty")
    elif ch==5:
        print("end of quiz")
        break
    else:
        print("Invalid syntax")
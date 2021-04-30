def kbc(Question_list,solution_list,option_list,Ans,i,r,y,count,amount):
    print("WellCome to kbc")
    while i<len(Question_list):
        i1=Question_list[i]
        print(i1)
        j=0
        k=i
        while j<len(option_list[i]):
            l=option_list[k][j]
            print(j+1,l)
            j=j+1
        lifeline1=input("do you want 5050 lifeline")
        if lifeline1=="yes":
            print("50-50")
            if count==0:
                print(Ans[y+i])
                print(Ans[y+r])
                n=int(input("inter the answer"))
                if n==solution_list[i]:
                    print("your answer is correct",amount[i])
                else:
                    print("worng")
                    break 
                count+=1
            else:
                print("you already used lifeline")
                m=int(input("enter the answer"))
                if m==solution_list[i]:
                    print("right")
                else:
                    print("wrong")
        elif lifeline1=="no":
           u=int(input("chose the answer"))
           if u==solution_list[i]:
             print("your answer is correct")
           else:
             print("your answer is worng") 
        else:
            print("error") 
        i=i+1
        r=r+1
        y=y+1  
kbc=(["how many continentes are there?",
"what is the capital of india?",
"NG me konse course pdaye jate hai?"],
[["four","nine","seven","eight"],
["Chandighad","Bhopal","Chennai","Delhi"],
["Software engineering","Counseling","tourisum","Agriculture"]],
[3,4,1],["3.seven","4.eight","2.bhopal","4.delhi","1.software engineering","3.torism"],0,1,0,0,[1000,5000,10000])      
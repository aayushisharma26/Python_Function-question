def a(list):
    i=0
    s=[]
    while i<len(list):
        m=list[i]
        if m not in s:
            s.append(m)
        i=i+1
    print(s)        
a([1,2,3,4,5,5,6,7,7,8,9,10,1,2,4,3])        
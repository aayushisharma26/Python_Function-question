def prime(num):
   i=0
   sum=0
   while i<num:
      if num%i==0:
         print(i)
         sum=sum+num
      i=i+1
   if sum==num:
      print(sum,"prime number") 
   else:
      print(sum,"not")
prime(int(input("enter the number")))                



v=int(input())
sum=0
temp=v
while(v>0):
    dig=v%10
    sum=sum*10+dig
    v=v//10
if(temp==sum):
    print("yes")
else:
    print("no")

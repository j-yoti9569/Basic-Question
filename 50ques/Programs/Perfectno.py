n=28
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+1
    if sum==n:
        print("The number is a perfect number")
    else:
        print("The number is not a perfect number")        
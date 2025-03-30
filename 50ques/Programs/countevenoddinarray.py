arr=[1,7,8,4,5,16,8]
n=len(arr)
countEven=0
countodd=0
for i in range(0,n):
    if arr[i]&1==0:
        countEven +=1
    else:
        countodd +=1
print("Even element count:") 
print(countEven)
print("odd element count:")
print(countodd)           
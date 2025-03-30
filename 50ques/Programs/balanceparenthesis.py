def isbalance(s):
    while(len(s)!=0):
        s=s.replace('()','')
        s=s.replace('[]','')
        s=s.replace('{}','')
    if(len(s)==0):
        return True
    else:
        return False
s=input("Enter a string of brackets:") 
print("Given string is balanced :",isbalancing(s))   
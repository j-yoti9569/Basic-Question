decimal=14
octal=[]
while decimal>0:
    r=decimal %8
    octal.append(r)
    decimal=decimal
    for i in reversed(octal):
        print(i,end=" ")
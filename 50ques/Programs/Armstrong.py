def is_armstrong(number):
    num_str=str(number)
    power=len(num_str)
    sum_of_digits=sum(int(digit)**power for digit in num_str)
    return sum_of_digit==number
num=int(input("Enter a number:"))
if is_armstrong(num):
    print(f"{num}is an Armstrong number.")
else:
    print(f"{num}is not an Armstrong number.")

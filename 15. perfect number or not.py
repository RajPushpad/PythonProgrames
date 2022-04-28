# Program of given number is perfect or not

MinValue = int(input("Enter any Minimum Value: "))
MaxValue = int(input("Enter any Maximum Value: "))

print("\nPerfect Number Between {0} to {1}".format(MinValue,MaxValue))

for Number in range(MinValue, MaxValue - 1):
    Sum = 0
    for n in range(1, Number - 1):
        if(Number % n == 0):
            Sum = Sum + n
    if(Sum == Number):
        print("%d " %Number)
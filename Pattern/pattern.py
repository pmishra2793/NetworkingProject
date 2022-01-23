'''
    1
    3 2
    6 5 4
    10 9 8 7
'''

num1 = 1
num2 = 2
currentNumber = num2
for row in range(2, 6):
    for col in range(num1, num2):
        currentNumber -= 1
        print(currentNumber, end=' ')
    print("")
    num1 = num2
    num2 += row
    currentNumber = num2
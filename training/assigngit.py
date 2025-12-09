total = 0
num = int(input("Enter the numbers to add: "))
for i in range(num):
    num = int(input("Enter number{}: ".format(i + 1)))
    total += num
print("The sum of numbers2 is:", total)
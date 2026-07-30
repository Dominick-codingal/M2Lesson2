number = int(input("Enter a number to find the sum of: "))

sum = 0

#Iterates for n+1 times:

for i in range (1, number+1):
    sum = sum+i
    
    print(f"\nSum = {sum}")
    
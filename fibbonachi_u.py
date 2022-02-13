number1 = 1
number2 = 1
 
n = input("Fibbonachi element number: ")
n = int(n)
 
i = 0
while i < n - 2:
    fibbonachi_sum = number1 + number2
    number1 = number2
    number2 = fibbonachi_sum
    i = i + 1
 
print( number2)
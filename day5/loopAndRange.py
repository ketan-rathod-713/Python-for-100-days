# using for loop with range functuon 

# for number in range(a,b):
#     print(number)

for number in range(1,10): #not included last digit
    print(number)
    
for number in range(1,10,3): # Here 3 is the step i += 3 , initially it was 1 by default
    print(number)
    
total = 0
for number in range(1,101):
    total += number
print(total)
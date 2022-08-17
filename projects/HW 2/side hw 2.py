a = 8  # Replace the assignment with a positive integer to test your code.
lst = [1, 2, 3, 4, 5]  # Replace the assignment with other lists to test your code.

# Write the rest of the code for question 1 below here.
notex = True
for num in lst:
    if num % a == 0:
        print (lst.index(num))
        notex = False
        break
if notex:
    print ("-1")

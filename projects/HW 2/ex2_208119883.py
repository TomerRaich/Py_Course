""" Exercise #2. Python for Engineers."""

#########################################
# Question 1 - do not delete this comment
#########################################

a = 3  # Replace the assignment with a positive integer to test your code.
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

# End of code for question 1

#########################################
# Question 2 - do not delete this comment
#########################################
lst2 = ['hello', 'world', 'course', 'python', 'day']
# Replace the assignment with other lists of strings (str) to test your code.


# Write the code for question 2 using a for loop below here.
summ = 0
for word in lst2:
    summ = summ + len(word)

avg = summ/len(lst2)
bigger = 0
for word in lst2:
    if len(word) > avg:
        bigger = bigger + 1
print (f"The number of strings longer than the average is: {bigger}")
        

# Write the code for question 2 using a while loop below here.

wsumm = 0
long = 0
while long < len(lst2):
    wsumm = wsumm + len(lst2[long])
    long = long+1

wavg = wsumm/len(lst2)
wbigger = 0
long = 0
while long < len(lst2):
        if len(lst2[long]) > wavg:
            wbigger = wbigger + 1           
        long = long+1
print (f"The number of strings longer than the average is: {wbigger}")


# End of code for question 2

#########################################
# Question 3 - do not delete this comment
#########################################

lst3 = [0, 1, 2, 3, 4]  # Replace the assignment with other lists to test your code.


# Write the rest of the code for question 3 below here.
sums = 0
if len(lst3) == 1:
    print (lst3[0])
else:
    for ind in range(len(lst3)-1):
      sums = sums + (lst3[ind]*lst3[ind+1])
    print(sums)


    




# End of code for question 3


#########################################
# Question 4 - do not delete this comment
#########################################

lst4 = [1, 2, 4, 7]  # Replace the assignment with other lists to test your code.

# Write the rest of the code for question 4 below here.
lst4_2 = [lst4[0]]
max_d = 0
for numb in lst4:
    if numb - lst4_2[-1] > max_d:
        
        max_d = numb - lst4_2[-1]
        lst4_2.append(numb)
        continue
    elif  lst4_2[-1] - numb > max_d:
       
        max_d = lst4_2[-1] - numb
        lst4_2.append(numb)
print (lst4_2)


# End of code for question 4

#########################################
# Question 5 - do not delete this comment
#########################################

my_string = 'abaadddefggg'  # Replace the assignment with other strings to test your code.
k = 3  # Replace the assignment with a positive integer to test your code.

# Write the rest of the code for question 5 below here.
letter = list(my_string)
nothing = True
for i in range(0,len(letter)-k+1):
    str1 = letter[i]*k
    str2 = my_string[i:i+k]
    if str1 == str2:
        print(f"For length {k}, found the substring {str1}!")
        nothing = False
        break
if nothing:
    print (f"Didn't find a substring of length {k}")
    
        
# End of code for question 5

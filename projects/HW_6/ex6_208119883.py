#########################################
# Question 1 - do not delete this comment
#########################################
def reverse_string(s):
    if len(s) == 1:
        return s
    return reverse_string(s[1:]) + s[0]

#########################################
# Question 2 - do not delete this comment
#########################################
def find_maximum(lst):
    if len(lst) == 0:
        return int(-1)
    x = find_maximum(lst[:-1])
    if  x > lst[-1]:
        return x
    return lst[-1]


#########################################
# Question 3 - do not delete this comment
#########################################
def is_palindrome(s):
    if len(s) == 2:
        return s[0] == s[1]
    if len(s) == 1:
        return True
    if s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])

#########################################
# Question 4 - do not delete this comment
#########################################
def climb_combinations(n):
    if n ==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 2
    return climb_combinations(n-1) + climb_combinations(n-2)




#########################################
# Question 5 - do not delete this comment
#########################################
def is_valid_paren(s, cnt=0):
    if len(s) == 0:
        if cnt != 0:
            return False
        return True
    if s[0] == ('('):
        cnt += 1
    if s[0] == (')'):
        cnt -= 1
    if cnt<0:
        return False
    return is_valid_paren(s[1:],cnt)



#########################
# main code - do not delete this comment
# Tests have been added for your convenience.
# You can add more tests below.
#########################
if __name__ == "__main__":
    #you can add tests for your code here.
    
    assert(reverse_string("abc") == 'cba')
    assert(reverse_string("Hello!") == '!olleH')
    assert (reverse_string("hello world") == 'dlrow olleh')

    assert (reverse_string("abs") == 'sba')
    assert (reverse_string("a") == 'a')
    assert (reverse_string("dg4#rrt") == 'trr#4gd')
    assert (reverse_string("reVERSe") == 'eSREVer')


    assert(find_maximum([9,3,0,10]) == 10)
    assert(find_maximum([9,3,0]) == 9)
    assert(find_maximum([]) == -1)
    assert (find_maximum([24, 3, 43, 10, 23,22]) == 43)

    assert (find_maximum([1,2,3,4]) == 4)
    assert (find_maximum([0]) == 0)
    assert (find_maximum([100, 10, 100]) == 100)
    assert (find_maximum([100, 100]) == 100)
    assert (find_maximum([5, 7.5]) == 7.5)

    assert(is_palindrome("aa") == True)
    assert(is_palindrome("aa ") == False)
    assert(is_palindrome("caca") == False)
    assert(is_palindrome("abcbbcba") == True)
    assert (is_palindrome("abcbbcbaa") == False)

    assert (is_palindrome("aa") == True)
    assert (is_palindrome("aa ") == False)
    assert (is_palindrome("caca") == False)
    assert (is_palindrome("abcbbcba") == True)
    assert (is_palindrome("abcbbcbaa") == False)

    assert(climb_combinations(3) == 3)
    assert(climb_combinations(10) == 89)

    assert(is_valid_paren("(.(a)") == False)
    assert(is_valid_paren("p(()r((0)))") == True)
    assert(is_valid_paren("") == True)
    assert (is_valid_paren("(.(a)))") == False)

# ============================== END OF FILE =================================

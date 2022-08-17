''' Exercise #6. Python for Engineers.'''

#########################################
# Question 1.a - do not delete this comment
#########################################
def four_bonacci_rec(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 3
    return (four_bonacci_rec(n-1) + four_bonacci_rec(n-2) + four_bonacci_rec(n-3) + four_bonacci_rec(n-4))

#########################################
# Question 1.b - do not delete this comment
#########################################
def four_bonacci_mem(n, memo=None):
    if n==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 3
    if memo == None:
        memo = {}
    key = n
    if key not in memo:
        memo[key - 4] = four_bonacci_mem(n - 4, memo)
        memo[key - 3] = four_bonacci_mem(n - 3, memo)
        memo[key - 2] = four_bonacci_mem(n - 2, memo)
        memo[key - 1] = four_bonacci_mem(n - 1, memo)
        memo[key] = memo[key-1] +memo[key-2] +memo[key-3] +memo[key-4]
        return memo[key]
    return memo[key]

#########################################
# Question 2 - do not delete this comment
#########################################
def climb_combinations_memo(n, memo=None):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if memo == None:
        memo = {}
    key = n
    if key not in memo:
        memo[key - 2] = climb_combinations_memo(n - 2, memo)
        memo[key - 1] = climb_combinations_memo(n - 1, memo)
        memo[key] = memo[key - 1] + memo[key - 2]
        return memo[key]
    return memo[key]


#########################################
# Question 3 - do not delete this comment
#########################################
def catalan_rec(n,memo=None):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if memo == None:
        memo = {}
    key = n
    if key not in memo:
        memo[key] = 0
        for i in range(n):
            memo[key] = memo[key]+ catalan_rec(i,memo) * catalan_rec((n-1)-i, memo)
        return memo[key]
    return memo[key]

    

#########################################
# Question 4.a - do not delete this comment
#########################################
def find_num_changes_rec(n, lst):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if lst == []:
        return 0
    return find_num_changes_rec(n-lst[-1],lst) + find_num_changes_rec(n,lst[:-1:])

    

#########################################
# Question 4.b - do not delete this comment
#########################################
def find_num_changes_mem(n, lst, memo=None):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if lst == []:
        return 0
    if memo == None:
        memo = {}
    key = (n , str(lst))
    if key not in memo:
        memo[key] = find_num_changes_mem(n - lst[-1], lst , memo) + find_num_changes_mem(n, lst[:-1:] , memo)
        return memo[key]
    return memo[key]

#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################
if __name__ == "__main__":
    #Question 1.a tests - you can and should add more


    print(four_bonacci_rec(0) == 0)
    print(four_bonacci_rec(5) == 12)
    print(four_bonacci_rec(8) == 85)

    #Question 1.b tests - you can and should add more

    print(four_bonacci_mem(0) == 0)
    print(four_bonacci_mem(5) == 12)
    print(four_bonacci_mem(8) == 85)
    
    from timeit import default_timer as timer

    n = 28
    start = timer()
    four_bonacci_rec(n=n)
    end = timer()
    print('Time without memoization for ', n, ':', end - start)
    start = timer()
    four_bonacci_mem(n=n)
    end = timer()
    print('Time with memoization for ', n, ':', end - start)

    #Question 2 tests - you can and should add more


    print(climb_combinations_memo(4) == 5)
    print(climb_combinations_memo(42) == 433494437)
    print(climb_combinations_memo(7) == 21)
    print(climb_combinations_memo(2) == 2)

    #Question 3 tests - you can and should add more

    cat_list = [1,1,2,5,14,42,132,429]
    for n,res in enumerate(cat_list):
        print(catalan_rec(n) == res)


    #Question 4.a tests - you can and should add more

    print(find_num_changes_rec(5,[1,2,5,6]) == 4)
    print(find_num_changes_rec(4,[1,2,5,6]) == 3)
    print(find_num_changes_rec(0.9,[1,2,5,6]) == 0)
    print(find_num_changes_rec(105,[1,105,999,100]) ==3)

    #Question 4.b tests - you can and should add more

    print(find_num_changes_mem(5,[1,2,5,6]) == 4)
    print(find_num_changes_mem(4,[1,2,5,6]) == 3)
    print(find_num_changes_mem(105,[1,105,999,100]) ==3)
    print(find_num_changes_mem(1430, [1, 2, 5, 6, 13]) == 231919276)

    from timeit import default_timer as timer

    lst = [1, 2, 5, 6, 13]
    n = 143
    start = timer()
    find_num_changes_rec(n, lst)
    end = timer()
    print('Time without memoization for ', n, lst, ':', end - start)
    start = timer()
    find_num_changes_mem(n, lst)
    end = timer()
    print('Time with memoization for ', n, lst, ':', end - start)

    pass
# ============================== END OF FILE =================================

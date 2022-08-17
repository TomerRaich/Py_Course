''' Exercise #6. Python for Engineers.'''


#########################################
# Question 1.a - do not delete this comment
#########################################
def four_bonacci_rec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    return (four_bonacci_rec(n - 1) + four_bonacci_rec(n - 2) + four_bonacci_rec(n - 3) + four_bonacci_rec(n - 4))


#########################################
# Question 1.b - do not delete this comment
#########################################
def four_bonacci_mem(n, memo=None):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    if memo == None:
        memo = {}
    key = n
    if key not in memo:
        memo[key - 4] = four_bonacci_mem(n - 4, memo)
        memo[key - 3] = four_bonacci_mem(n - 3, memo)
        memo[key - 2] = four_bonacci_mem(n - 2, memo)
        memo[key - 1] = four_bonacci_mem(n - 1, memo)
        memo[key] = memo[key - 1] + memo[key - 2] + memo[key - 3] + memo[key - 4]
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
def catalan_rec(n, memo=None):
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
            memo[key] = memo[key] + catalan_rec(i, memo) * catalan_rec((n - 1) - i, memo)
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
    return find_num_changes_rec(n - lst[-1], lst) + find_num_changes_rec(n, lst[:-1:])


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
    key = (n, str(lst))
    if key not in memo:
        memo[key] = find_num_changes_mem(n - lst[-1], lst, memo) + find_num_changes_mem(n, lst[:-1:], memo)
        return memo[key]
    return memo[key]


#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################
if __name__ == "__main__":
    # Question 1.a tests - you can and should add more

    print(four_bonacci_rec(0) == 0)
    print(four_bonacci_rec(5) == 12)
    print(four_bonacci_rec(8) == 85)

    # Question 1.b tests - you can and should add more

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

    # Question 2 tests - you can and should add more

    print(climb_combinations_memo(4) == 5)
    print(climb_combinations_memo(42) == 433494437)
    print(climb_combinations_memo(7) == 21)
    print(climb_combinations_memo(2) == 2)

    # Question 3 tests - you can and should add more

    cat_list = [1, 1, 2, 5, 14, 42, 132, 429]
    for n, res in enumerate(cat_list):
        print(catalan_rec(n) == res)

    # Question 4.a tests - you can and should add more

    print(find_num_changes_rec(5, [1, 2, 5, 6]) == 4)
    print(find_num_changes_rec(4, [1, 2, 5, 6]) == 3)
    print(find_num_changes_rec(0.9, [1, 2, 5, 6]) == 0)
    print(find_num_changes_rec(105, [1, 105, 999, 100]) == 3)

    # Question 4.b tests - you can and should add more

    print(find_num_changes_mem(5, [1, 2, 5, 6]) == 4)
    print(find_num_changes_mem(4, [1, 2, 5, 6]) == 3)
    print(find_num_changes_mem(105, [1, 105, 999, 100]) == 3)
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


import sys
import timeit


def did_pass(question, errors, warnings=None):
    if warnings == None:
        warnings = []
    if not errors:
        message = f'question {question} passed the tests'
        print(message, f'but with warnings: {warnings}' if warnings else '')
    else:
        print(
            f'question {question} failed the tests, with {len(errors)} errors:', errors)


def is_recursive(function, large_case, errors):
    previous_limit = sys.getrecursionlimit()
    sys.setrecursionlimit(50)
    try:
        if type(large_case) == list:
            function(*large_case)
        else:
            function(large_case)
        errors.append('not recursive')
    except RecursionError as error:
        if 'maximum recursion depth exceeded' not in error.args[0]:
            errors.append('an unexpected error has occurred')
    except Exception as err:
        print(err)
        errors.append('an unexpected error has occurred')
    finally:
        sys.setrecursionlimit(previous_limit)


def execution_time(function, arguments):
    start = timeit.default_timer()
    function(*arguments)
    return timeit.default_timer() - start


def is_faster(large_case, fun_rec, fun_memo, warnings):
    min_time_diff = 1
    rec_time = execution_time(fun_rec, large_case)
    memo_time = execution_time(fun_memo, large_case)
    if not memo_time < rec_time - min_time_diff:
        warnings.append(
            f'memo version took: {memo_time} seconds and the simple one took: {rec_time} seconds')


def q1_test(function):
    errors = []
    is_recursive(function, 200, errors)
    cases = {0: 0, 1: 1, 2: 2, 3: 3, 4: 6, 5: 12,
             6: 23, 7: 44, 10: 316, 12: 1174}
    for case, result in cases.items():
        if function(case) != result:
            errors.append(f'doesn\'t work with n = {case}')
    return errors


def q1_part_a_test():
    try:
        return did_pass('1 part a', q1_test(four_bonacci_rec))
    except:
        print('question 1 part a raised an unexpected error')


def q1_part_b_test():
    try:
        warnings = []
        is_faster([26], four_bonacci_rec, four_bonacci_mem, warnings)
        return did_pass('1 part b', q1_test(four_bonacci_mem), warnings)
    except:
        print('question 1 part b raised an unexpected error')


def q2_test():
    try:
        errors = []
        is_recursive(climb_combinations_memo, 200, errors)
        cases = {1: 1, 2: 2, 3: 3, 11: 144, 29: 832040}
        for case, result in cases.items():
            if climb_combinations_memo(case) != result:
                errors.append(f'doesn\'t work with n = {case}')
        warnings = []
        is_faster([31], climb_combinations_rec,
                  climb_combinations_memo, warnings)
        return did_pass(2, errors, warnings)
    except:
        print('question 2 raised an unexpected error')


def climb_combinations_rec(n):
    if n < 2:
        return 1
    return sum(climb_combinations_rec(n-i) for i in range(1, 3))


def q3_test():
    try:
        errors = []
        is_recursive(catalan_rec, 100, errors)
        cases = {0: 1, 1: 1, 2: 2, 11: 58786, 20: 6564120420}
        for n, res in cases.items():
            if catalan_rec(n) != res:
                errors.append(f'doesn\'t work with n = {n}')
        return did_pass(3, errors)
    except:
        print('question 3 raised an unexpected error')


def q4_test(function):
    errors = []
    is_recursive(function, [200, [1, 2, 3, 4, 5]], errors)
    cases = {(0, tuple()): 1, (0, (1,)): 1, (1, tuple()): 0, (1, (1,)): 1, (2, (1, 2)): 2, (1, (2,)): 0, (40, (10, 5, 2, 7, 1)): 438}
    for (num, coins), res in cases.items():
        if function(num, list(coins)) != res:
            errors.append(
                f'doesn\'t work with num = {num} and coins = {list(coins)}')
    return errors


def q4_part_a_test():
    try:
        return did_pass('4 part a', q4_test(find_num_changes_rec))
    except:
        print('question 4 part a raised an unexpected error')


def q4_part_b_test():
    try:
        warnings = []
        is_faster([150, [1, 3, 5, 4, 2]], find_num_changes_rec,
                  find_num_changes_mem, warnings)
        return did_pass('4 part b', q4_test(find_num_changes_mem), warnings)
    except:
        print('question 4 part b raised an unexpected error')


q1_part_a_test()
q1_part_b_test()
q2_test()
q3_test()
q4_part_a_test()
q4_part_b_test()

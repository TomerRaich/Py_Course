''' Exercise #4. Python for Engineers.'''


#########################################
# Question 1 - do not delete this comment
#########################################
def most_popular_character(my_string):

    dic1 = {}
    for let in my_string:
        if let in dic1:
            dic1[let] = dic1[let] + 1
        elif let!= " ":
            dic1[let] = 1
    sorted_d = sorted(dic1, key=dic1.get,reverse=True)
    max_let = sorted_d[0]
    maxims = []
    for i in sorted_d:
        if dic1[i] == dic1[max_let]:
            maxims.append(i)
    x = sorted(maxims)[0]
    return x   


#########################################
# Question 2 - do not delete this comment
#########################################
def diff_sparse_matrices(lst):
    dicA = lst[0]
    for i in range(len(lst)-1):
        dic_pry = lst[i+1]
        for key in dic_pry:
            if key in dicA:
                dicA[key] = dicA[key] - dic_pry[key]
            else:
                dicA[key] = 0 - dic_pry[key]
            if dicA[key] == 0:
                dicA.pop(key)
    return dicA


#########################################
# Question 3 - do not delete this comment
#########################################
def find_substring_locations(s, k):
    dic1 = {}
    for i in range(len(s)-k+1):
        str_temp = s[i:i+k]
        if str_temp not in dic1:
            dic1[str_temp] = [i]
        else:
            dic1[str_temp].append(i)
    return dic1


#########################################
# Question 4 - do not delete this comment
#########################################
def courses_per_student(tuples_lst):

    dic = {}
    for tup in tuples_lst:
        if tup[0].lower() not in dic:
            dic[tup[0].lower()] = [tup[1].lower()]
        else:
            dic[tup[0].lower()].append(tup[1].lower())
    return dic
        


def num_courses_per_student(stud_dict):
    for key in stud_dict:
        stud_dict[key] = len(stud_dict[key])

#########################
# main code - do not delete this comment
# Tests have been added for your convenience.
# You can add more tests below.
#########################

if __name__ == '__main__': #Do not delete this line!
	# Q1
	print(most_popular_character('aabbAA') == 'A')
	print(most_popular_character("HelloWorld") == 'l')
	print(most_popular_character("gggcccbb")== 'c')

	# Q2
	print(diff_sparse_matrices([{(1, 3): 2, (2, 7): 1}, {(1, 3): 6}]) == {(1, 3): -4, (2, 7): 1})
	print(diff_sparse_matrices([{(1, 3): 2, (2, 7): 1}, {(1, 3): 6, (9,10): 7}, {(2,7): 0.5, (4,2): 10}]) == {(1, 3): -4, (2, 7): 0.5, (9, 10): -7, (4,2): -10})	
	# Q3
	print(find_substring_locations('TTAATTAGGGGCGC', 2) == {'TT': [0, 4], 'TA': [1, 5], 'AA': [2], 'AT': [3], 'AG': [6], 'GG': [7, 8, 9], 'GC': [10, 12], 'CG': [11]})
	print(find_substring_locations('TTAATTAGGGGCGC', 3) == {'TTA': [0, 4], 'TAA': [1], 'AAT': [2], 'ATT': [3], 'TAG': [5], 'AGG': [6], 'GGG': [7, 8], 'GGC': [9], 'GCG':
[10], 'CGC': [11]})

	print(find_substring_locations('Hello World', 3)=={'Hel': [0], 'ell': [1], 'llo': [2], 'lo ': [3], 'o W': [4], ' Wo': [5], 'Wor': [6], 'orl': [7], 'rld': [8]})
      
	# Q4
	stud_dict = courses_per_student([('Tom', 'Math'), ('Oxana', 'Chemistry'), ('Scoobydoo', 'python'), ('Tom', 'pYthon'), ('Oxana', 'biology')])
		
	print(stud_dict == {'tom': ['math', 'python'], 'oxana': ['chemistry', 'biology'], 'scoobydoo': ['python']})
		
	num_courses_per_student(stud_dict)
	print(stud_dict == {'tom': 2, 'oxana': 2, 'scoobydoo': 1})


# ============================== END OF FILE =================================


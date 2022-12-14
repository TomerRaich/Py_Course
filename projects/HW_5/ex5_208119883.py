''' Exercise #5. Python for Engineers.'''

#########################################
# Question 1 - do not delete this comment
#########################################
def sum_nums(file_name):
    f = open(file_name, "r" )
    line = f.readline()
    f.close()
    nums = line.split(" ")
    sum_s = 0
    for num in nums:
        sum_s = sum_s + int(num)
    return sum_s

#########################################
# Question 2 - do not delete this comment
#########################################
def copy_lines_with_str(in_file_name, out_file_name, target_str):
    infile = None
    outfile = None
    try:
            infile = open(in_file_name, "r")
            outfile = open(out_file_name, "w")
            for line in infile:
                for i in range(len(line)-len(target_str)):
                    if line[i:i+len(target_str)]== target_str:
                        outfile.write(line)
                        continue
    except IOError:
             raise IOError("error") 
    finally:
        if infile != None:
            infile.close()
        if outfile != None:
            outfile.close()

#########################################
# Question 3 - do not delete this comment
#########################################
def write_twin_primes(num, out_file_name):
    if num > 0:
        try:
            outfile = open(out_file_name, "w")
            count = num-1
            pry_nums = {0:(3,5)}
            outfile.write(str(pry_nums[0][0])+ "," +str(pry_nums[0][1])+ "\n")
            while count!=0:
                ind = num-count
                couple = pry_num_d_ind(ind, pry_nums)
                pry_nums[ind] = couple
                outfile.write(str(pry_nums[ind][0])+ "," +str(pry_nums[ind][1])+ "\n")
                count = count-1
        except IOError:
            raise ValueError("Cannot write to {}".format(out_file_name))
        finally:
            outfile.close()
    else:
        raise ValueError("Illegal value num={}".format(num))

    
def pry_num_d_ind(ind, pry_nums):
    num1 = pry_nums[ind-1][0]
    num2 = pry_nums[ind-1][1]
    num1is = False

    while num1is != True:
        num1is = True
        num1 = num1+1
        for div in range(2,(int(num1**0.5))+1):
            if num1 % div == 0:
                num1is = False
                break
        if num1is == True and abs(num1 - num2) == 2:
            return (min(num1,num2), max(num1, num2))
        elif num1is == True:
            num2 = num1
            num1is = False
                
                    #if  num1 - num2 == 2:
         #   count = count-1
          #  continue
        
    # use the following code to raise the errors you need:
    # raise ValueError("Illegal value num={}".format(num))
    # raise ValueError("Cannot write to {}".format(out_file_name))???
    pass


#########################################
# Question 4 - do not delete this comment
#########################################
def calc_avg_position_per_band(in_file_name):
    try:
        file = open(in_file_name, "r")
        bands = {"Radiohead": 0 ,"The Beatles": 0 ,"ABBA" : 0 }
        count = {"Radiohead": 0 ,"The Beatles": 0 ,"ABBA" : 0 }
        for line in file:
            l = line.split(",")
            bands[l[1].strip("'")] = bands[l[1].strip("'")] + int(l[2].strip("\n""'"))
            count[l[1].strip("'")] = count[l[1].strip("'")] + 1
        for band in bands:
            if count[band] == 0:
                raise ValueError("At least one of the bands does not appear in the file {}".format(in_file_name))
        for band in bands:
            
            bands[band] = round(bands[band]/count[band])
        
        return bands

    finally:
        file.close()
    
   
            
    # use the following code to raise the error you need:
    # raise ValueError("At least one of the bands does not appear in the file {}".format(in_file_name))
    pass


#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################
if __name__ == "__main__":
    # Q1
    q1_input_file_name = "q1_input_1.txt"
    print(sum_nums(q1_input_file_name) == 139)

    # Q2
    # compare manually your output files with the correct output files
    copy_lines_with_str("q2_input_1.txt", "q2_output_1_Rocky_res.txt", "Rocky")
    copy_lines_with_str("q2_input_1.txt", "q2_output_1_ere_res.txt", "ere")
    copy_lines_with_str("q2_input_2.txt", "q2_output_2_Rocky_res.txt", "Rocky")
    copy_lines_with_str("q2_input_2.txt", "q2_output_2_boy_res.txt", "boy")
    copy_lines_with_str("q2_input_2.txt", "q2_output_2_Nancy_res.txt", "Nancy")

    # Q3
    write_twin_primes(4, "q3_output_1_res.txt")
    write_twin_primes(20, "q3_output_2_res.txt")
    try:
        num = 0
        write_twin_primes(num, "q3_output_2_res.txt")  # this line should raise an exception
        print("Exception must be raised for this input")
    except ValueError as ex:
        correct_error_message = "Illegal value num={}".format(num)
        if ex.args[0] == correct_error_message:
            print("True")
        else:
            print("Wrong message in raise exception. \nExpected:\t{}\ngot:\t\t{}".format(correct_error_message,
                                                                                         ex.args[0]))

    # Q4
    res_1 = calc_avg_position_per_band("q4_input_1.txt")
    print(res_1['The Beatles'] == 23 and res_1['Radiohead'] == 11 and res_1['ABBA'] == 4)
    try:
        input_file = "q4_input_2.txt"
        res_1 = calc_avg_position_per_band(input_file)
        print("Exception must be raised for this input")
    except ValueError as ex:
        correct_error_message = "At least one of the bands does not appear in the file {}".format(input_file)
        if ex.args[0] == correct_error_message:
            print("True")
        else:
            print("Wrong message in raise exception. \nExpected:\t{}\ngot:\t\t{}".format(correct_error_message,
                                                                                         ex.args[0]))



# add more tests here

# ============================== END OF FILE =================================

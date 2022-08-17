''' Exercise #10. Python for Engineers.'''

import numpy as np
import pandas as pd
import imageio
import matplotlib.pyplot as plt


#########################################
# Question 1 helper functions - do not delete
# this comment or change these functions
#########################################

#helper1----------------------------------------------------------------------
def np_array_to_ascii(darr):
    return ''.join([chr(item) for item in darr])


#helper2----------------------------------------------------------------------
def ascii_to_np_array(s):
    return np.frombuffer(s.encode(), dtype=np.uint8)


#########################################
# Question 1 - do not delete this comment
#########################################


#1----------------------------------------------------------------------------
def arr_dist(a1, a2):
    return (np.abs(np.array(a1,dtype=int)-np.array(a2,dtype=int))).sum()


#2----------------------------------------------------------------------------
def find_best_place(im, np_msg):
    l = len(np_msg)
    rows = im.shape[0]
    cols = im.shape[1]
    row = min(256,rows)
    col = min(256, cols-l)
    best = (1,1)
    best_dist = arr_dist(im[1,1:1+l], np_msg)
    for i in range(row):
        for j in range(col):
            if (i,j) not in [(0,0),(0,1),(0,2)]:
                a1 = im[i,j : j+l]
                kur = arr_dist(np_msg, a1)
                if kur <= best_dist:
                    best_dist = kur
                    best = (i,j)
    return best



#3----------------------------------------------------------------------------
def create_image_with_msg(im, img_idx, np_msg):
     im_cop = im.copy()
     im_cop [img_idx[0], img_idx[1]: len(np_msg)+img_idx[1]] = np.array(np_msg)
     im_cop[0,0] = img_idx[0]
     im_cop[0,1] = img_idx[1]
     im_cop[0,2] = len(np_msg)
     return im_cop


#4----------------------------------------------------------------------------
def put_message(im, msg):
    msg_np = ascii_to_np_array(msg.strip())
    best = find_best_place(im, msg_np)
    new_im  = create_image_with_msg(im,best, msg_np)
    return new_im


#5----------------------------------------------------------------------------
def get_message(im):
    mes_np = im[im[0,0],im[0,1]:im[0,1]+im[0,2]]
    msg = np_array_to_ascii(mes_np)
    return msg


##############################################################################
##############################################################################


#########################################
# Question 2 - do not delete this comment
#########################################

#A----------------------------------------------------------------------------
def read_missions_file(file_name):
    try:
        df = pd.read_csv(file_name)
        df.set_index("Kingdom")
        return df
    except IOError: ("occurred error IO A")
#B----------------------------------------------------------------------------
def add_daily_gain_col(bounties):
    bounties["daily gain"] = (bounties["Bounty"] - bounties["Expenses"]) / bounties["Duration"]
    return bounties

#C----------------------------------------------------------------------------
def sum_rewards(bounties):
    return (bounties["Bounty"] - bounties["Expenses"]).sum()


#D----------------------------------------------------------------------------
def find_best_kingdom(bounties):
    new_bount = add_daily_gain_col(bounties)
    return new_bount.loc[new_bount["daily gain"].idxmax(),["Kingdom"]]


#E----------------------------------------------------------------------------
def find_best_duration(bounties):
    new_bount = add_daily_gain_col(bounties)
    return new_bount.groupby(["Duration"])["daily gain"].mean().idxmax()


#########################################
# A test for Question 1 - do not delete this comment 
#########################################


def question_A_test():
    msg1 = 'Hello, NUMPY!'
    orig_file_name = 'parrot.png'

    im1 = imageio.imread(orig_file_name)
    im2 = put_message(im1, msg1)

    plot_image = np.concatenate((im1, im2), axis=1)

    plt.figure()
    plt.imshow(plot_image, cmap=plt.cm.gray)
    plt.show()

    msg2 = get_message(im2)
    return msg2

#########################
# main code - do not delete this comment
# Add test cases below
#########################
if __name__ == "__main__":
    # ****write test cases only here****
	
    # Uncomment the following test after implementing Question 1
    #assert(question_A_test() == "Hello, NUMPY!")

    #print(question_A_test())
    """
    filename = "missions.csv"
    df = read_missions_file(filename)
    print(df)
    print(add_daily_gain_col(df))
    print(sum_rewards(df))
    print(find_best_kingdom(df))
    print(find_best_duration(df))



"""


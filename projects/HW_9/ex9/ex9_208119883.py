''' Exercise #9. Python for Engineers.'''

import numpy as np
import matplotlib.pyplot as plt
import imageio
import math

#########################################
# Question 1 - do not delete this comment
#########################################

class Roman():

    def get_int_from_roman(self):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        roman_string = self.roman_value.strip('-')
        int_val = 0
        for counter in range(len(roman_string)):
            if counter > 0 and rom_val[roman_string[counter]] > rom_val[roman_string[counter - 1]]:
                int_val += rom_val[roman_string[counter]] - 2 * rom_val[roman_string[counter - 1]]
            else:
                int_val += rom_val[roman_string[counter]]
        int_val = -int_val if self.is_neg else int_val
        return int_val

    def get_roman_from_int(self):
        num = self.int_value if not self.is_neg else -self.int_value
        roman_num = '' if not self.is_neg else '-'
        counter = 0

        roman_char = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        int_vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        while num > 0:
            for _ in range(num // int_vals[counter]):
                roman_num += roman_char[counter]
                num -= int_vals[counter]
            counter += 1
        return roman_num

    def __init__(self, input_value):
        if type(input_value) is int:
            self.int_value = input_value
            if self.int_value < 0:
                self.is_neg = True
            else:
                self.is_neg = False
            self.roman_value = self.get_roman_from_int()
        else:
            self.roman_value = input_value
            if self.roman_value[0] == "-":
                self.is_neg = True
            else:
                self.is_neg = False
            self.int_value = self.get_int_from_roman()


    def __str__(self):
        return (f"The integer value is {self.int_value} and the Roman Numeral is denoted by '{self.roman_value}'")

    def __repr__(self):
        return self.roman_value


    def __neg__(self):
        return Roman(- self.int_value).roman_value


    def __add__(self, other):

        if type(other) is int:
            if self.int_value + other == 0 :
                raise ValueError("type Roman cant be Zero")
            sum_rom = Roman(self.int_value + other)
        elif type(other) is Roman:
            if self.int_value + other.int_value == 0 :
                raise ValueError("type Roman cant be Zero")
            sum_rom = Roman(self.int_value + other.int_value)
        else:
            raise ValueError("other must be type Roman \ int")
        return sum_rom.roman_value



    def __lt__(self, other):
        if type(other) is int:
            if self.int_value < other:
                return  True
            return False
        elif type(other) is Roman:
            if self.int_value < other.int_value:
                return True
            return False
        else:
            raise ValueError("other must be type Roman \ int")


    def __gt__(self, other):
        if type(other) is int:
            if self.int_value > other:
                return True
            return False
        elif type(other) is Roman:
            if self.int_value > other.int_value:
                return True
            return False
        else:
            raise ValueError("other must be type Roman \ int")


    def __floordiv__(self, other):
        if type(other) is int:
            if self.int_value//other == 0:
                raise ValueError("zero cant be a soulotion")
            dev_rom = Roman(self.int_value // other)
        elif type(other) is Roman:
            if self.int_value//other.int_value == 0:
                raise ValueError("zero cant be a soulotion")
            dev_rom = Roman(self.int_value // other.int_value)
        else:
            raise ValueError("other must be type Roman \ int")
        return dev_rom.roman_value



#########################################
# Question 2 - do not delete this comment
#########################################

def load_training_data(filename):
    lines = open(filename, 'r').readlines()
    dict_training = {}
    names = []
    data = []
    for line in lines:
        line = line.rstrip("\n")
        line1 = line.split(',')
        names.append(line1[0])
        data.append(line1[1:])
    dict_training["data"] = np.array((data[1:]), dtype=float)
    dict_training["column_names"] = np.array((data[0] ))
    dict_training["row_names"] = np.array(names)
    return dict_training


def get_highest_weight_loss_trainee(data_dict):
    weights_beg = data_dict["data"][:, 0].astype(np.float)
    weights_end = data_dict["data"][:, -1].astype(np.float)
    weights_loss = np.subtract(weights_beg, weights_end)
    maxim = weights_loss.argmax()
    return data_dict["row_names"][maxim+1]

def get_diff_data(data_dict):
    i = data_dict["data"][:,:-1]
    iplus = data_dict["data"][:,1:]
    diff = - (i - iplus)
    return diff


def get_highest_loss_month(data_dict):
    diff = get_diff_data(data_dict)
    sums = diff.sum(axis = 0)
    return data_dict["column_names"][sums.argmax()]


def get_relative_diff_table(data_dict):
    lose= get_diff_data(data_dict)
    iplus = data_dict["data"][:,1:]
    return lose/iplus



#########################################
# Question 3 - do not delete this comment
#########################################
def occurance(nparr):
    occ = []
    for i in range(265):
        mask = (nparr == i)
        if mask.any():
            occ.append(mask.sum())
    return occ

def compute_entropy(img):
    im = imageio.imread(img)
    occ = occurance(im)
    size = int(im.size)
    occ_dev = []
    for num in occ:
        occ_dev.append((num/size))
    pi = []
    for i in occ_dev:
        pi.append((-i) * (np.log(i)/np.log(2)))
    s = sum (pi)
    return s


def nearest_enlarge(img, a):
    im = imageio.imread(img)
    new_n = im.shape[0] * a
    new_m = im.shape[1] * a
    new_mat = np.zeros((new_n,new_m), dtype=int)
    n_cros = im.shape[0]/new_n
    m_cros = im.shape[1]/new_m
    for n in range(new_n):
        for m in range(new_m):
            new_mat[n,m] = im[math.floor(n*(n_cros)), math.floor(m*(m_cros))]
    print(new_mat)
    return new_mat



if __name__ == '__main__':
    """
    print(Roman(2))
    print(repr(Roman(2)))
    print(-Roman("IV"))
    r = Roman(2) + 3
    print(repr(r))

    print(Roman(6) // Roman(5))

    print(Roman("VI") // 5)

    print(Roman(6) // Roman("-V"))

    print(Roman(6) // -5)

    ###print(Roman(2) // Roman(3))  # this should raise a ValueError

    """
    """
    data_dict = load_training_data("D:\TAU\python\projects\HW_9\ex9\weight_input.csv")
    print(data_dict["data"])
    print(data_dict["column_names"])
    print(data_dict["row_names"])
    print(get_highest_weight_loss_trainee(data_dict))

    print(get_diff_data(data_dict))

    print(get_highest_loss_month(data_dict))

    print(get_relative_diff_table(data_dict))
    

    print(compute_entropy('cameraman.tif'))

    I = nearest_enlarge("cameraman.tif",2)
    plt.figure()
    plt.imshow(I,cmap = plt.get_cmap("gray"), vmin=0, vmax=255)
    plt.show()
    """

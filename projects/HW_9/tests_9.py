###########################################################################
##########################      DISCLAIMER      ##########################
###########################################################################

# this tests aren't official test,
# so you should take any success or error
# with the benefit of the doubt

############################# may be usefull ##############################

# https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html
# https://numpy.org/doc/stable/reference/generated/numpy.argmax.html
# https://numpy.org/doc/stable/reference/generated/numpy.bincount.html

###########################################################################
##########################      DISCLAIMER      ###########################
###########################################################################

###########################################################################
#############################      CODE      ##############################
###########################################################################
import numpy as np
import matplotlib.pyplot as plt
import imageio
import math

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
        return Roman(- self.int_value).__repr__()


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
        return sum_rom.__repr__()



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
        return dev_rom.__repr__()



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


###########################################################################
#############################      CODE      ##############################
###########################################################################
import copy
import os
############ the following libraries must be imported with those names #################
# import numpy as np
# import imageio


def did_pass(question, errors, warnings=None):
    if warnings == None:
        warnings = []
    if not errors:
        print(f'question {question} passed the tests')
    else:
        print(
            f'question {question} failed the tests, with {len(errors)} errors:\n{prettify_errors(errors)}')


def prettify_errors(errors):
    errors_str = ''
    for i, error in enumerate(errors):
        errors_str += f'    {i + 1}) {error}\n'
    return errors_str


def catch_error(fun, errors, error_message):
    try:
        fun()
    except Exception as error:
        errors.append(error_message + f', error: {error}')


def strings_diff(expected, received, line=None, indent=0):
    diffs = []
    longer = expected if len(expected) > len(
        received) else received if len(received) > len(expected) else ''
    for i, (s1, s2) in enumerate(zip(expected, received)):
        if s1 != s2:
            diffs.append(
                (f'in line: {line + 1} ' if line else '') + f'at index: {i}, "{s1}" vs "{s2}"')
            return diffs
    if longer:
        diffs.append(
            (f'in line: {line + 1} ' if line else '') +
            f'one is longer with the following text: "{longer[min(len(expected), len(received)):]}"')
    return diffs


def get_file_name(extension='txt'):
    i = 0
    while True:
        name = f'test_file_{i}.{extension}'
        if not os.path.exists(name):
            return name
        i += 1


def remove_files(*files_name):
    for file_name in files_name:
        if os.path.exists(file_name):
            os.remove(file_name)


def q1_test():
    errors = []

    def part_1():
        errors = []
        cases = [[1, 'I', False], [-1, '-I', True],
                 [33, 'XXXIII', False], [-33, '-XXXIII', True]]
        for i in range(2):
            for case in cases:
                r = Roman(case[i])
                if r.int_value != case[0]:
                    errors.append(
                        f'wrong int_value when input_value is {case[i]}')
                if r.roman_value != case[1]:
                    errors.append(
                        f'wrong roman_value when input_value is {case[i]}')
                if r.is_neg != case[2]:
                    errors.append(
                        f'wrong is_neg when input_value is {case[i]}')
        return errors

    def part_2():
        errors = []
        cases = [['I', 1], ['-I', -1], ['XXXIII', 33], ['-XXXIII', -33]]
        for case in cases:
            errors.extend(strings_diff(
                f"The integer value is {case[1]} and the Roman Numeral is denoted by '{case[0]}'", str(Roman(case[0]))))
        for case in cases:
            errors.extend(strings_diff(case[0], repr(Roman(case[0]))))
        return errors

    def match_romans(first, second):
        if not isinstance(first, Roman):
            return True
        return isinstance(second, Roman) and first.int_value == second.int_value and first.roman_value == second.roman_value and first.is_neg == second.is_neg

    def part_3():
        errors = []
        cases = [['I', 1, False], ['-I', -1, True]]
        for i, case in enumerate(cases):
            a = Roman(case[i])
            prev_state = Roman(case[i])
            r = -a
            if not isinstance(r, Roman):
                errors.append(
                    f'__neg__didn\'t return an instance of type Roman for input {case[i]}')
                continue
            if r.int_value != cases[(i+1) % 2][1]:
                errors.append(
                    f'wrong int_value from __neg__ when Roman is {case[i]}')
            if r.roman_value != cases[(i+1) % 2][0]:
                errors.append(
                    f'wrong roman_value from __neg__ when Roman is {case[i]}')
            if r.is_neg != cases[(i+1) % 2][2]:
                errors.append(
                    f'wrong is_neg from __neg__ when Roman is {case[i]}')
            if not match_romans(prev_state, a):
                errors.append(
                    f'__neg__ shouldn\'t change the given Roman, only return a new one')
        return errors

    def part_4():
        errors = []
        cases = [(Roman(2), Roman(3), True), (Roman(2), Roman(1),
                                              False), (Roman(2), 3, True), (Roman(2), 1, False)]
        for case in cases:
            if (case[0] < case[1]) != case[2]:
                text = 'Roman' if isinstance(case[1], Roman) else 'int'
                num = case[1].int_value if isinstance(
                    case[1], Roman) else case[1]
                errors.append(
                    f'wrong response from __lt__ for Roman({case[0].int_value}) < {text}({num})')
            if (case[0] > case[1]) == case[2]:
                text = 'Roman' if isinstance(case[1], Roman) else 'int'
                num = case[1].int_value if isinstance(
                    case[1], Roman) else case[1]
                errors.append(
                    f'wrong response from __gt__ for Roman({case[0].int_value}) > {text}({num})')
            if Roman(2) < Roman(2) or Roman(2) < 2:
                errors.append(
                    'wrong response from __lt__ when both sides are equals to each other')
            if Roman(2) > Roman(2) or Roman(2) > 2:
                errors.append(
                    'wrong response from __gt__ when both sides are equals to each other')

        cases = [(Roman(2), Roman(2), Roman(4)), (Roman(1), Roman(-1), 'error'), (Roman(1), 2, Roman(3)),
                 (Roman(1), -1, 'add error'), (Roman(-3), Roman(-4), Roman(-7)), (Roman(5), -7, Roman(-2))]
        for case in cases:
            try:
                a1, a2, b1, b2 = case[0], case[0], case[1], case[1]
                res = a2 + b2
                if type(case[2]) == str:
                    errors.append(
                        f'should raise a value error if the addition result is 0')
                    continue
                if not (match_romans(a1, a2) and match_romans(b1, b2)):
                    errors.append(
                        'addition shouldn\'t change the added values, only return a new one')
                if not match_romans(case[2], res):
                    text = 'Roman' if isinstance(case[1], Roman) else 'int'
                    num = case[1].int_value if isinstance(
                        case[1], Roman) else case[1]
                    errors.append(
                        f'wrong addition result for Roman({case[0].int_value}) + {text}({num})')
            except ValueError:
                if type(case[2]) != str:
                    errors.append(
                        'raised an unexpected ValueError on addition')
            except Exception as error:
                errors.append(
                    f'raised an unexpected error on addition, error: {error}')

        return errors

    def part_5():
        errors = []
        cases = [(Roman(2), Roman(2), Roman(1)), (Roman(1), Roman(-1), Roman(-1)), (Roman(2), 2, Roman(1)),
                 (Roman(1), -1, Roman(-1)), (Roman(-3), Roman(-4), 'error'), (Roman(5), 7, 'error')]
        for case in cases:
            try:
                a1, a2, b1, b2 = case[0], case[0], case[1], case[1]
                res = a2 // b2
                if type(case[2]) == str:
                    errors.append(
                        f'should raise a value error if the division result is 0')
                    continue
                if not (match_romans(a1, a2) and match_romans(b1, b2)):
                    errors.append(
                        'division shouldn\'t change the divided values, only return a new one')
                if not match_romans(case[2], res):
                    text = 'Roman' if isinstance(case[1], Roman) else 'int'
                    num = case[1].int_value if isinstance(
                        case[1], Roman) else case[1]
                    errors.append(
                        f'wrong division result for Roman({case[0].int_value}) // {text}({num})')
            except ValueError:
                if type(case[2]) != str:
                    errors.append(
                        'raised an unexpected ValueError on division')
            except Exception as error:
                errors.append(
                    f'raised an unexpected error on division, error: {error}')
        return errors

    errors.extend(part_1())
    errors.extend(part_2())
    errors.extend(part_3())
    errors.extend(part_4())
    errors.extend(part_5())
    return errors


def q2_test():
    errors = []
    file_data_1 = [',January,February\n', 'Daniel,10, 9\n']
    file_data_2 = [',January,February,March,April\n', 'Daniel,10,9,1,7\n',
                   'Meir,10,9,2,5\n', 'Yael,10.3,9.2,3.1,7.99\n', 'roni,10.99,4,7,6.63\n']
    keys = ['column_names', 'row_names', 'data']
    data_dict1 = {
        keys[0]: np.array(['January', 'February']),
        keys[1]: np.array(['Daniel']),
        keys[2]: np.array([[10, 9]])
    }
    data_dict2 = {
        keys[0]: np.array(['January', 'February', 'March', 'April']),
        keys[1]: np.array(['Daniel', 'Meir', 'Yael', 'roni']),
        keys[2]: np.array([[10., 9., 1., 7.], [10., 9., 2., 5.], [
                          10.3, 9.2, 3.1, 7.99], [10.99, 4., 7., 6.63]])
    }

    def load_data_file(file_name, data):
        try:
            with open(file_name, 'w') as f:
                f.writelines(data)
        except:
            print('an error has occurred while trying to save tests files')

    def part_1():
        errors = []
        file_name = get_file_name()
        load_data_file(file_name, file_data_1)
        try:
            data_dict = load_training_data(file_name)
            if data_dict['data'].dtype not in [np.float64, np.int64]:
                errors.append(
                    f'wrong type in data_dict[\'data\'] (search for dtype in google)')
            elif not (data_dict['data'] == data_dict1['data']).all():
                errors.append(f'wrong values in data_dict[\'data\']')
            for key in keys[:-1]:
                if not (data_dict[key] == data_dict1[key]).all():
                    errors.append(f'wrong values in data_dict[\'{key}\']')
        except Exception as error:
            errors.append(
                f'an unexpected error has occurred, in load_training_data, error: {error}')
        remove_files(file_name)

        file_name = get_file_name()
        load_data_file(file_name, file_data_2)
        try:
            data_dict = load_training_data(file_name)
            if data_dict['data'].dtype not in [np.float64, np.int64]:
                errors.append(
                    f'wrong type in data_dict[\'data\'] (search for dtype in google)')
            elif not (data_dict['data'] == data_dict2['data']).all():
                errors.append(f'wrong values in data_dict[\'data\']')
            for key in keys[:-1]:
                if not (data_dict[key] == data_dict2[key]).all():
                    errors.append(f'wrong values in data_dict[\'{key}\']')
        except Exception as error:
            errors.append(
                f'an unexpected error has occurred, in load_training_data, error: {error}')
        remove_files(file_name)
        return errors

    def part_2():
        errors = []
        cases = [(copy.deepcopy(data_dict1), 'Daniel'),
                 (copy.deepcopy(data_dict2), 'Meir')]
        for i, (data, correct) in enumerate(cases):
            if get_highest_weight_loss_trainee(data) != correct:
                errors.append('wrong answer from the function - get_highest_weight_loss_trainee' +
                              (', when there is only one person' if i == 0 else ''))
        return errors

    def part_3():
        errors = []
        diff1 = np.array([[-1]])
        diff2 = np.array([[-1., -8.,  6.],
                          [-1., -7.,  3.],
                          [-1.1, -6.1,  4.89],
                          [-6.99,  3., -0.37]])
        cases = [(data_dict1, copy.deepcopy(data_dict1), diff1),
                 (data_dict2, copy.deepcopy(data_dict2), diff2)]
        for i, (original, data, correct) in enumerate(cases):
            if get_diff_data(data).shape != correct.shape or ((get_diff_data(data) - correct) > 0.0001).any():
                errors.append('wrong answer from the function - get_diff_data' +
                              (', when there is only one person' if i == 0 else ''))

            def match_dicts(dict1, dict2):
                if len(dict1) != len(dict2):
                    return False
                for key in dict1:
                    match_value = dict2.get(key, 'not found')
                    if type(match_value) == str or not (dict1[key] == match_value).all():
                        return False
                return True
            if not match_dicts(original, data):
                errors.append(
                    'get_diff_data shouldn\'t mutate the original data')
        return errors

    def part_4():
        errors = []
        cases = [(copy.deepcopy(data_dict1), 'February'),
                 (copy.deepcopy(data_dict2), 'March')]
        for i, (data, correct) in enumerate(cases):
            if get_highest_loss_month(data) != correct:
                errors.append('wrong answer from the function - get_highest_loss_month' +
                              (', when there is only one person' if i == 0 else ''))
        return errors

    def part_5():
        errors = []
        result1 = np.array([[-0.1]])
        result2 = np.array([[-0.1, -0.88888889,  6.],
                            [-0.1, -0.77777778,  1.5],
                            [-0.10679612, -0.66304348,  1.57741935],
                            [-0.63603276,  0.75, -0.05285714]])
        cases = [(data_dict1, result1), (data_dict2, result2)]
        for i, (data, correct) in enumerate(cases):
            if get_relative_diff_table(data).shape != correct.shape or ((get_relative_diff_table(data) - correct) > 0.00001).any():
                errors.append('wrong answer from the function - get_relative_diff_table' +
                              (', when there is only one person' if i == 0 else ''))
        return errors

    errors.extend(part_1())
    errors.extend(part_2())
    errors.extend(part_3())
    errors.extend(part_4())
    errors.extend(part_5())
    return errors


def q3_test():
    errors = []

    def part_1():
        errors = []
        cases = [(np.zeros((10, 10), dtype=np.uint8), 0), (np.array(np.vstack(
            (np.zeros((3, 10)), np.ones((3, 10)), np.zeros((2, 10)), np.ones((2, 10)))), dtype=np.uint8), 0.7219280948873623),
            (np.array(np.hstack((np.ones((10, 1)), np.ones((10, 2)) * 100, np.ones((10, 3))*255, np.ones((10, 1))*50, np.zeros((10, 1)))), dtype=np.uint8), 2.5)]
        for array, correct in cases:
            file_name = get_file_name('jpg')
            imageio.imwrite(file_name, array)
            diff = abs(compute_entropy(file_name) - correct)
            if diff > 0.000001:
                errors.append(
                    f'wrong response from compute_entropy, diff of: {diff}')
            remove_files(file_name)
        return errors

    def part_2():
        errors = []
        input_im = np.array([[128, 160,   8, 165, 138,  41, 126, 157, 155,   8],
                             [136,   9, 146,  74, 220, 123,  44,  66, 188, 239],
                             [215, 210, 119, 244, 201,  92,  26, 138,  62,  49],
                             [16, 200,  54, 255, 116, 126,  29, 203, 131, 224],
                             [97, 106, 158, 149, 106,  61, 145,  52,  62,  76],
                             [166, 136,  13,  33, 165, 233, 198, 181,   9,  94],
                             [14,  72,  56,  34, 198,  94, 100, 241, 188, 163],
                             [187,  89,  92, 209, 212, 143, 100,  48, 110, 164],
                             [8, 159,  27, 100,  39,  74,  13,  18, 173,  40],
                             [223,  28,  83, 123, 233, 119,  12, 232, 143, 165]], dtype=np.uint8)
        expected_output_2 = np.array([[128., 128., 161., 161.,   3.,   3., 166., 166., 137., 137.,  40.,
                                       40., 129., 129., 150., 150., 150., 150.,  16.,  16.],
                                      [128., 128., 161., 161.,   3.,   3., 166., 166., 137., 137.,  40.,
                                       40., 129., 129., 150., 150., 150., 150.,  16.,  16.],
                                      [134., 134.,   4.,   4., 152., 152.,  71.,  71., 237., 237., 107.,
                                       107.,  42.,  42.,  78.,  78., 204., 204., 224., 224.],
                                      [134., 134.,   4.,   4., 152., 152.,  71.,  71., 237., 237., 107.,
                                       107.,  42.,  42.,  78.,  78., 204., 204., 224., 224.],
                                      [210., 210., 227., 227., 111., 111., 237., 237., 184., 184., 118.,
                                       118.,  26.,  26., 136., 136.,  57.,  57.,  36.,  36.],
                                      [210., 210., 227., 227., 111., 111., 237., 237., 184., 184., 118.,
                                       118.,  26.,  26., 136., 136.,  57.,  57.,  36.,  36.],
                                      [19.,  19., 170., 170.,  68.,  68., 255., 255., 106., 106., 123.,
                                       123.,  27.,  27., 195., 195., 132., 132., 235., 235.],
                                      [19.,  19., 170., 170.,  68.,  68., 255., 255., 106., 106., 123.,
                                       123.,  27.,  27., 195., 195., 132., 132., 235., 235.],
                                      [108., 108., 106., 106., 158., 158., 162., 162., 111., 111.,  45.,
                                       45., 163., 163.,  43.,  43.,  52.,  52.,  78.,  78.],
                                      [108., 108., 106., 106., 158., 158., 162., 162., 111., 111.,  45.,
                                       45., 163., 163.,  43.,  43.,  52.,  52.,  78.,  78.],
                                      [154., 154., 138., 138.,  13.,  13.,  14.,  14., 163., 163., 243.,
                                       243., 181., 181., 206., 206.,   6.,   6., 103., 103.],
                                      [154., 154., 138., 138.,  13.,  13.,  14.,  14., 163., 163., 243.,
                                       243., 181., 181., 206., 206.,   6.,   6., 103., 103.],
                                      [33.,  33.,  62.,  62.,  63.,  63.,  43.,  43., 192., 192., 110.,
                                       110.,  94.,  94., 225., 225., 195., 195., 164., 164.],
                                      [33.,  33.,  62.,  62.,  63.,  63.,  43.,  43., 192., 192., 110.,
                                       110.,  94.,  94., 225., 225., 195., 195., 164., 164.],
                                      [184., 184.,  90.,  90.,  95.,  95., 203., 203., 213., 213., 141.,
                                       141., 103., 103.,  51.,  51., 106., 106., 157., 157.],
                                      [184., 184.,  90.,  90.,  95.,  95., 203., 203., 213., 213., 141.,
                                       141., 103., 103.,  51.,  51., 106., 106., 157., 157.],
                                      [2.,   2., 157., 157.,  28.,  28.,  92.,  92.,  42.,  42.,  73.,
                                       73.,  16.,  16.,  16.,  16., 160., 160.,  57.,  57.],
                                      [2.,   2., 157., 157.,  28.,  28.,  92.,  92.,  42.,  42.,  73.,
                                       73.,  16.,  16.,  16.,  16., 160., 160.,  57.,  57.],
                                      [225., 225.,  39.,  39.,  92.,  92., 132., 132., 229., 229., 115.,
                                       115.,  15.,  15., 232., 232., 160., 160., 154., 154.],
                                      [225., 225.,  39.,  39.,  92.,  92., 132., 132., 229., 229., 115.,
                                       115.,  15.,  15., 232., 232., 160., 160., 154., 154.]])
        expected_output_3 = np.array([[128., 128., 128., 161., 161., 161.,   3.,   3.,   3., 166., 166.,
                                       166., 137., 137., 137.,  40.,  40.,  40., 129., 129., 129., 150.,
                                       150., 150., 150., 150., 150.,  16.,  16.,  16.],
                                      [128., 128., 128., 161., 161., 161.,   3.,   3.,   3., 166., 166.,
                                       166., 137., 137., 137.,  40.,  40.,  40., 129., 129., 129., 150.,
                                       150., 150., 150., 150., 150.,  16.,  16.,  16.],
                                      [128., 128., 128., 161., 161., 161.,   3.,   3.,   3., 166., 166.,
                                       166., 137., 137., 137.,  40.,  40.,  40., 129., 129., 129., 150.,
                                       150., 150., 150., 150., 150.,  16.,  16.,  16.],
                                      [134., 134., 134.,   4.,   4.,   4., 152., 152., 152.,  71.,  71.,
                                       71., 237., 237., 237., 107., 107., 107.,  42.,  42.,  42.,  78.,
                                       78.,  78., 204., 204., 204., 224., 224., 224.],
                                      [134., 134., 134.,   4.,   4.,   4., 152., 152., 152.,  71.,  71.,
                                       71., 237., 237., 237., 107., 107., 107.,  42.,  42.,  42.,  78.,
                                       78.,  78., 204., 204., 204., 224., 224., 224.],
                                      [134., 134., 134.,   4.,   4.,   4., 152., 152., 152.,  71.,  71.,
                                       71., 237., 237., 237., 107., 107., 107.,  42.,  42.,  42.,  78.,
                                       78.,  78., 204., 204., 204., 224., 224., 224.],
                                      [210., 210., 210., 227., 227., 227., 111., 111., 111., 237., 237.,
                                       237., 184., 184., 184., 118., 118., 118.,  26.,  26.,  26., 136.,
                                       136., 136.,  57.,  57.,  57.,  36.,  36.,  36.],
                                      [210., 210., 210., 227., 227., 227., 111., 111., 111., 237., 237.,
                                       237., 184., 184., 184., 118., 118., 118.,  26.,  26.,  26., 136.,
                                       136., 136.,  57.,  57.,  57.,  36.,  36.,  36.],
                                      [210., 210., 210., 227., 227., 227., 111., 111., 111., 237., 237.,
                                       237., 184., 184., 184., 118., 118., 118.,  26.,  26.,  26., 136.,
                                       136., 136.,  57.,  57.,  57.,  36.,  36.,  36.],
                                      [19.,  19.,  19., 170., 170., 170.,  68.,  68.,  68., 255., 255.,
                                       255., 106., 106., 106., 123., 123., 123.,  27.,  27.,  27., 195.,
                                       195., 195., 132., 132., 132., 235., 235., 235.],
                                      [19.,  19.,  19., 170., 170., 170.,  68.,  68.,  68., 255., 255.,
                                       255., 106., 106., 106., 123., 123., 123.,  27.,  27.,  27., 195.,
                                       195., 195., 132., 132., 132., 235., 235., 235.],
                                      [19.,  19.,  19., 170., 170., 170.,  68.,  68.,  68., 255., 255.,
                                       255., 106., 106., 106., 123., 123., 123.,  27.,  27.,  27., 195.,
                                       195., 195., 132., 132., 132., 235., 235., 235.],
                                      [108., 108., 108., 106., 106., 106., 158., 158., 158., 162., 162.,
                                       162., 111., 111., 111.,  45.,  45.,  45., 163., 163., 163.,  43.,
                                       43.,  43.,  52.,  52.,  52.,  78.,  78.,  78.],
                                      [108., 108., 108., 106., 106., 106., 158., 158., 158., 162., 162.,
                                       162., 111., 111., 111.,  45.,  45.,  45., 163., 163., 163.,  43.,
                                       43.,  43.,  52.,  52.,  52.,  78.,  78.,  78.],
                                      [108., 108., 108., 106., 106., 106., 158., 158., 158., 162., 162.,
                                       162., 111., 111., 111.,  45.,  45.,  45., 163., 163., 163.,  43.,
                                       43.,  43.,  52.,  52.,  52.,  78.,  78.,  78.],
                                      [154., 154., 154., 138., 138., 138.,  13.,  13.,  13.,  14.,  14.,
                                       14., 163., 163., 163., 243., 243., 243., 181., 181., 181., 206.,
                                       206., 206.,   6.,   6.,   6., 103., 103., 103.],
                                      [154., 154., 154., 138., 138., 138.,  13.,  13.,  13.,  14.,  14.,
                                       14., 163., 163., 163., 243., 243., 243., 181., 181., 181., 206.,
                                       206., 206.,   6.,   6.,   6., 103., 103., 103.],
                                      [154., 154., 154., 138., 138., 138.,  13.,  13.,  13.,  14.,  14.,
                                       14., 163., 163., 163., 243., 243., 243., 181., 181., 181., 206.,
                                       206., 206.,   6.,   6.,   6., 103., 103., 103.],
                                      [33.,  33.,  33.,  62.,  62.,  62.,  63.,  63.,  63.,  43.,  43.,
                                       43., 192., 192., 192., 110., 110., 110.,  94.,  94.,  94., 225.,
                                       225., 225., 195., 195., 195., 164., 164., 164.],
                                      [33.,  33.,  33.,  62.,  62.,  62.,  63.,  63.,  63.,  43.,  43.,
                                       43., 192., 192., 192., 110., 110., 110.,  94.,  94.,  94., 225.,
                                       225., 225., 195., 195., 195., 164., 164., 164.],
                                      [33.,  33.,  33.,  62.,  62.,  62.,  63.,  63.,  63.,  43.,  43.,
                                       43., 192., 192., 192., 110., 110., 110.,  94.,  94.,  94., 225.,
                                       225., 225., 195., 195., 195., 164., 164., 164.],
                                      [184., 184., 184.,  90.,  90.,  90.,  95.,  95.,  95., 203., 203.,
                                       203., 213., 213., 213., 141., 141., 141., 103., 103., 103.,  51.,
                                       51.,  51., 106., 106., 106., 157., 157., 157.],
                                      [184., 184., 184.,  90.,  90.,  90.,  95.,  95.,  95., 203., 203.,
                                       203., 213., 213., 213., 141., 141., 141., 103., 103., 103.,  51.,
                                       51.,  51., 106., 106., 106., 157., 157., 157.],
                                      [184., 184., 184.,  90.,  90.,  90.,  95.,  95.,  95., 203., 203.,
                                       203., 213., 213., 213., 141., 141., 141., 103., 103., 103.,  51.,
                                       51.,  51., 106., 106., 106., 157., 157., 157.],
                                      [2.,   2.,   2., 157., 157., 157.,  28.,  28.,  28.,  92.,  92.,
                                       92.,  42.,  42.,  42.,  73.,  73.,  73.,  16.,  16.,  16.,  16.,
                                       16.,  16., 160., 160., 160.,  57.,  57.,  57.],
                                      [2.,   2.,   2., 157., 157., 157.,  28.,  28.,  28.,  92.,  92.,
                                       92.,  42.,  42.,  42.,  73.,  73.,  73.,  16.,  16.,  16.,  16.,
                                       16.,  16., 160., 160., 160.,  57.,  57.,  57.],
                                      [2.,   2.,   2., 157., 157., 157.,  28.,  28.,  28.,  92.,  92.,
                                       92.,  42.,  42.,  42.,  73.,  73.,  73.,  16.,  16.,  16.,  16.,
                                       16.,  16., 160., 160., 160.,  57.,  57.,  57.],
                                      [225., 225., 225.,  39.,  39.,  39.,  92.,  92.,  92., 132., 132.,
                                       132., 229., 229., 229., 115., 115., 115.,  15.,  15.,  15., 232.,
                                       232., 232., 160., 160., 160., 154., 154., 154.],
                                      [225., 225., 225.,  39.,  39.,  39.,  92.,  92.,  92., 132., 132.,
                                       132., 229., 229., 229., 115., 115., 115.,  15.,  15.,  15., 232.,
                                       232., 232., 160., 160., 160., 154., 154., 154.],
                                      [225., 225., 225.,  39.,  39.,  39.,  92.,  92.,  92., 132., 132.,
                                       132., 229., 229., 229., 115., 115., 115.,  15.,  15.,  15., 232.,
                                       232., 232., 160., 160., 160., 154., 154., 154.]])
        file_name = get_file_name('jpg')
        imageio.imwrite(file_name, input_im)
        result1 = nearest_enlarge(file_name, 2)
        if result1.shape != expected_output_2.shape:
            errors.append(
                'nearest_enlarge returned an image with the wrong size')
        elif not (result1 == expected_output_2).all():
            errors.append('wrong result from nearest_enlarge, with a = 2')
        result2 = nearest_enlarge(file_name, 3)
        if result2.shape != expected_output_3.shape:
            errors.append(
                'nearest_enlarge returned an image with the wrong size')
        elif not (result2 == expected_output_3).all():
            errors.append('wrong result from nearest_enlarge, with a = 3')
        remove_files(file_name)
        return errors

    errors.extend(part_1())
    errors.extend(part_2())
    return errors


def run(tests):
    for i, test in enumerate(tests):
        errors = []
        try:
            errors = test()
        except Exception as error:
            errors.append(f'raised an unexpected error: {error}')
        finally:
            did_pass(i + 1, errors)


tests = [q1_test, q2_test, q3_test]
run(tests)

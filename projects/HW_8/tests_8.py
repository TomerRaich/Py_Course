###########################################################################
##########################      DISCLAIMER      ##########################
###########################################################################

# this tests aren't official test,
# so you should take any success or error
# with the benefit of the doubt

############################# may be usefull ##############################

# https://www.programiz.com/python-programming/list-comprehension
# https://www.programiz.com/python-programming/dictionary-comprehension
# https://www.programiz.com/python-programming/methods/string/join

###########################################################################
##########################      DISCLAIMER      ###########################
###########################################################################

###########################################################################
#############################      CODE      ##############################
###########################################################################

''' Exercise #8. Python for Engineers.'''
#########################################
# Question 1 - do not delete this comment
#########################################
class Minibar:
    def __init__(self, drinks, snacks):
        #drinks = [drink.lower()for drink in drinks]
        #snacks = [snack.lower() for snack in snacks]
        self.drinks = drinks
        self.snacks = snacks
        self.bill = 0.0

    def __repr__(self):

        drinks = []
        snacks = []
        for drink in self.drinks:
            drinks.append(drink)
        for snack in self.snacks:
            snacks.append(snack)

        return (f"The minibar contains the drinks: {drinks}\n"
              f"And the snacks: {snacks}\n"
              f"The bill for the minibar is: {self.bill}")

    def eat_a_snack(self, snack):
        l_snaks = {}
        for snack1 in self.snacks:
            l_snaks[snack1.lower()] = snack1
        snack = snack.lower()
        if snack not in l_snaks:
            raise ValueError('The snack is not in the minibar')
        self.bill += self.snacks.pop(l_snaks[snack])

    def drink_a_drink(self, drink):
        l_drinks = {}
        for drink1 in self.drinks:
            l_drinks[drink1.lower()] = drink1
        drink = drink.lower()
        if drink not in l_drinks:
            raise ValueError('The drink is not in the minibar')
        self.bill += self.drinks.pop(l_drinks[drink])


#########################################
# Question 2 - do not delete this comment
#########################################
class RoomError(Exception):
    # A subclass of Exception that defines a new error type
    # DO NOT change this class
    pass


class Room:
    def __init__(self, minibar, floor, number, guests, clean_level, rank, satisfaction=1.0):
        if type(clean_level) is not int or type(rank) is not int:
            raise TypeError(f"{clean_level} or {rank} are not type - int - numbers!")
        if type(satisfaction) is not int and type(satisfaction) is not float:
            raise TypeError(f"{satisfaction} is not type - int or float - number!")
        if clean_level < 1 or clean_level > 10:
            raise ValueError(f"clean_level{clean_level} is not in range")
        if rank < 1 or rank > 3:
            raise ValueError(f"rank{rank} is not in range")
        if satisfaction < 1 or satisfaction > 5:
            raise ValueError(f"satisfaction{satisfaction} is not in range")

        l_guests = [guest.lower() for guest in guests]

        self.minibar = minibar
        self.floor = floor
        self.number = number
        self.guests = l_guests
        self.clean_level = clean_level
        self.rank = rank
        self.satisfaction = satisfaction

    def __repr__(self):
        if not self.is_occupied():
            guests = "empty"
        else:
            guests = ', '.join(self.guests)
        return (f"{self.minibar}\n"
                f"floor: {self.floor}\n"
                f"number: {self.number}\n"
                f"guests: {guests}\n"
                f"clean_level: {self.clean_level}\n"
                f"rank: {self.rank}\n"
                f"satisfaction: {round(self.satisfaction, 1)}")

    def is_occupied(self):
        if not self.guests:
            return False
        return True

    def clean(self):
        self.clean_level = min(10, self.clean_level + self.rank)

    def better_than(self, other):
        if type(other) is not Room:
            raise TypeError("Other must be an instance of Room")
        if (self.rank, self.floor, self.clean_level) > (other.rank, other.floor, other.clean_level):
            return True
        return False

    def check_in(self, guests):
        if self.is_occupied():
            raise RoomError("Cannot check-in new guests to an occupied room")
        self.guests = [guest.lower() for guest in guests]
        self.satisfaction = 1.0

    def check_out(self):
        if self.is_occupied() == False:
            raise RoomError("Cannot check-out an empty room")
        self.guests = []

    def move_to(self, other):
        if self.is_occupied() == False:
            raise RoomError("Cannot move guests from an empty room")
        if other.is_occupied():
            raise RoomError("Cannot move guests into an occupied room")
        other.check_in(self.guests)
        if other.better_than(self):
            other.satisfaction = min(5.0, self.satisfaction + 1.0)
        else:
            other.satisfaction = self.satisfaction
        self.check_out()


#########################################
# Question 3 - do not delete this comment
#########################################
class Hotel:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms

    def __repr__(self):
        return (f"{self.name} hotel has:\n"
                f"{len(self.rooms)} rooms\n"
                f"{self.occupied_rooms()} occupied rooms")

    def occupied_rooms(self):
        occupied_count = 0
        for room in self.rooms:
            if room.is_occupied():
                occupied_count += 1
        return occupied_count

    def check_in(self, guests, rank):
        for room in self.rooms:
            if room.rank == rank:
                try:
                    room.check_in(guests)
                    return room
                except RoomError:
                    continue
        return None

    def check_out(self, guest):
        guestl = guest.lower()
        for room in self.rooms:
            if guestl in room.guests:
                room.check_out()
                return room

        return None

    def upgrade(self, guest):
        guestl = guest.lower()
        for room in self.rooms:
            if guestl in room.guests:
                for broom in self.rooms:
                    if not broom.is_occupied():
                        if broom.better_than(room):
                            room.move_to(broom)
                            return broom

                break

        return None


###########################################################################
#############################      CODE      ##############################
###########################################################################


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


def lists_values_matches(*lists):
    if not all([len(lists[i]) == len(lists[i + 1]) for i, lst in enumerate(lists[:-1])]):
        return False
    return all([all([elem in lists[i + 1] for elem in lists[i]]) for i in range(len(lists) - 1)])


def q1_test():
    errors = []
    m1 = Minibar({}, {})
    if m1.drinks != {}:
        errors.append('doesn\'t set the drinks correctly')
    if m1.snacks != {}:
        errors.append('doesn\'t set the snacks correctly')
    if m1.bill != 0:
        errors.append('doesn\'t initialize the bill')
    if type(m1.bill) != float:
        errors.append('bill needs to be of type float')
    drinks2 = [{'SoDA': 1, 'water': 5, 'sprite': 3},
               {'soda': 1, 'water': 5, 'sprite': 3}]
    snacks2 = [{'TwIX': 11.5, 'lays': 3, 'cookies': 5.5},
               {'twix': 11.5, 'lays': 3, 'cookies': 5.5}]
    m2 = Minibar(drinks2[0], snacks2[0])
    if m2.drinks not in drinks2:
        errors.append(
            'doesn\'t set the drinks correctly when there are not empty')
    if m2.snacks not in snacks2:
        errors.append(
            'doesn\'t set the snacks correctly when there are not empty')
    catch_error(lambda: m2.drink_a_drink('water'), errors,
                'an error occurred while drinking a drink')
    drinks2_1 = [{'SoDA': 1, 'sprite': 3},
                 {'soda': 1, 'sprite': 3}]
    if m2.drinks not in drinks2_1:
        errors.append('doesn\'t remove the drink after drinking it')
    if m2.bill != 5:
        errors.append(
            'doesn\'t update the bill correctly after drinking a drink')
    if type(m2.bill) != float:
        errors.append(
            'bill stopped beeing of type "float" after drinking a drink')
    m2.bill = .0
    catch_error(lambda: m2.eat_a_snack('lays'), errors,
                'an error occurred while eating a snack')
    snacks2_1 = [{'TwIX': 11.5, 'cookies': 5.5},
                 {'twix': 11.5, 'cookies': 5.5}]
    if m2.snacks not in snacks2_1:
        errors.append('doesn\'t remove the snack after snacking it')
    if m2.bill != 3:
        errors.append(
            'doesn\'t update the bill correctly after snacking a snack')
    if type(m2.bill) != float:
        errors.append(
            'bill stopped beeing of type float after snacking a snack')
    m2.bill = .0
    flag = False
    try:
        drinks2_2 = [{'sprite': 3}, {'sprite': 3}]
        m2.drink_a_drink('SODA')
        if m2.drinks not in drinks2_2:
            errors.append(
                'doesn\'t compare the drink by there lowercase value before in drink_a_drink it from drinks, forum: "https://moodle.tau.ac.il/mod/forum/discuss.php?d=51182"')
    except:
        flag = True
        errors.append(
            'doesn\'t compare the drink by there lowercase value before in drink_a_drink it from drinks, forum: "https://moodle.tau.ac.il/mod/forum/discuss.php?d=51182"')
    try:
        snacks2_2 = [{'cookies': 5.5}, {'cookies': 5.5}]
        m2.eat_a_snack('TWIX')
        if m2.snacks not in snacks2_2:
            errors.append(
                'doesn\'t compare the snack by there lowercase value before in eat_a_snack it from snacks, forum: "https://moodle.tau.ac.il/mod/forum/discuss.php?d=51182"')
    except:
        flag = True
        errors.append(
            'doesn\'t compare the snack by there lowercase value before in eat_a_snack it from snacks, forum: "https://moodle.tau.ac.il/mod/forum/discuss.php?d=51182"')

    if not flag and m2.bill != 12.5:
        errors.append(
            'bill doesn\'t stay of type float after eating and drinking (please stop drinking - not for me, for you)')

    try:
        m1.drink_a_drink('water')
        errors.append('doesn\'t raise a ValueError if the drink is missing')
    except ValueError as error:
        if error.args[0] != 'The drink is not in the minibar':
            errors.append(
                'if a drink is missing the error message isn\'t right')
    except Exception as error:
        errors.append(
            f'raise an error but not a ValueError if the drink is missing, error: {error}')
    try:
        m1.eat_a_snack('twix')
        errors.append('doesn\'t raise a ValueError if the snack is missing')
    except ValueError as error:
        if error.args[0] != 'The snack is not in the minibar':
            errors.append(
                'if a snack is missing the error message isn\'t right')
    except Exception as error:
        errors.append(
            f'raise an error but not a ValueError if the snack is missing, error: {error}')

    if repr(m1) != 'The minibar contains the drinks: []\nAnd the snacks: []\nThe bill for the minibar is: 0.0':
        errors.append('doesn\'t print the an empty minibar instace correctly')
    if repr(m2) != 'The minibar contains the drinks: [\'sprite\']\nAnd the snacks: [\'cookies\']\nThe bill for the minibar is: 12.5':
        errors.append('doesn\'t print the a minibar instace correctly')
    return errors


def q2_test():
    errors = []
    m1 = Minibar({}, {})
    r1 = Room(m1, 1, 1, [], 1, 1)
    if r1.minibar != m1:
        errors.append('doesn\'t set correctly the minibar attribute')
    if r1.floor != 1:
        errors.append('doesn\'t set correctly the floor attribute')
    if r1.number != 1:
        errors.append('doesn\'t set correctly the number attribute')
    if r1.guests != []:
        errors.append('doesn\'t set correctly the guests attribute')
    if r1.clean_level != 1:
        errors.append('doesn\'t set correctly the clean_level attribute')
    if r1.rank != 1:
        errors.append('doesn\'t set correctly the rank attribute')
    if r1.satisfaction != 1.0:
        errors.append('doesn\'t set correctly the satisfaction attribute')

    def did_raise_type_error(fun, errors, error_message):
        try:
            fun()
            errors.append(error_message)
        except TypeError:
            pass
        except:
            error_message.append(error_message)

    def did_raise_value_error(fun, errors, error_message):
        try:
            fun()
            errors.append(error_message)
        except ValueError:
            pass
        except:
            error_message.append(error_message)

    did_raise_type_error(lambda: Room(m1, 1, 1, [], '1', 1),
                         errors, 'didn\'t raise a TypeError for wrong clean_level')
    did_raise_value_error(lambda: Room(m1, 1, 1, [], 0, 1), errors,
                          'didn\'t raise a ValueError for wrong clean_level - 0')
    did_raise_value_error(lambda: Room(m1, 1, 1, [], 11, 1), errors,
                          'didn\'t raise a ValueError for wrong clean_level - 11')
    did_raise_type_error(lambda: Room(m1, 1, 1, [], 1, '1'),
                         errors, 'didn\'t raise a TypeError for wrong rank')
    did_raise_value_error(lambda: Room(m1, 1, 1, [], 1, 0),
                          errors, 'didn\'t raise a ValueError for wrong rank - 0')
    did_raise_value_error(lambda: Room(m1, 1, 1, [], 1, 4),
                          errors, 'didn\'t raise a ValueError for wrong rank - 4')
    did_raise_type_error(lambda: Room(m1, 1, 1, [], 1, '1'),
                         errors, 'didn\'t raise a TypeError for wrong satisfaction')
    did_raise_value_error(lambda: Room(m1, 1, 1, [], 1, 1, 0.99), errors,
                          'didn\'t raise a ValueError for wrong satisfaction - 0.99')
    did_raise_value_error(lambda: Room(m1, 1, 1, [], 1, 1, 5.01), errors,
                          'didn\'t raise a ValueError for wrong satisfaction - 5.01')
    catch_error(lambda: Room(m1, 1, 1, [], 1, 1), errors,
                'raised an unexpected error for clean_level = 1')
    catch_error(lambda: Room(m1, 1, 1, [], 10, 1), errors,
                'raised an unexpected error for clean_level = 10')
    catch_error(lambda: Room(m1, 1, 1, [], 1, 1), errors,
                'raised an unexpected error for rank = 1')
    catch_error(lambda: Room(m1, 1, 1, [], 1, 3), errors,
                'raised an unexpected error for rank = 3')
    catch_error(lambda: Room(m1, 1, 1, [], 1, 1, 1.0), errors,
                'raised an unexpected error for satisfaction = 1.0')
    catch_error(lambda: Room(m1, 1, 1, [], 1, 1, 3), errors,
                'raised an unexpected error for satisfaction = 3')
    catch_error(lambda: Room(m1, 1, 1, [], 1, 1, 5.0), errors,
                'raised an unexpected error for satisfaction = 5.0')

    if Room(m1, 1, 1, ['Dana', 'SHIR', 'MichaeL'], 1, 1).guests != ['dana', 'shir', 'michael']:
        errors.append('doesn\'t convert the guests names to lowercase')

    minibar_repr = 'The minibar contains the drinks: []\nAnd the snacks: []\nThe bill for the minibar is: 0.0'
    if repr(Room(m1, 1, 1, [], 1, 1)) != f'{minibar_repr}\nfloor: 1\nnumber: 1\nguests: empty\nclean_level: 1\nrank: 1\nsatisfaction: 1.0':
        errors.append(
            'doesn\'t print correctly when the list of guests is empty')
    if repr(Room(m1, 1, 1, ['Dana'], 1, 1)) != f'{minibar_repr}\nfloor: 1\nnumber: 1\nguests: dana\nclean_level: 1\nrank: 1\nsatisfaction: 1.0':
        errors.append('doesn\'t print correctly when there is only one guest')
    if repr(Room(m1, 1, 1, ['Dana', 'yael', 'michal'], 1, 1)) != f'{minibar_repr}\nfloor: 1\nnumber: 1\nguests: dana, yael, michal\nclean_level: 1\nrank: 1\nsatisfaction: 1.0':
        errors.append(
            'doesn\'t print correctly when there are multiple guests')
    if repr(Room(m1, 1, 1, [], 1, 1, 3.2563)) != f'{minibar_repr}\nfloor: 1\nnumber: 1\nguests: empty\nclean_level: 1\nrank: 1\nsatisfaction: 3.3':
        errors.append('doesn\'t print correctly the rounded satisfaction')

    if Room(m1, 1, 1, [], 1, 1).is_occupied():
        errors.append('return that the room is occupied when it\'s empty')
    if not Room(m1, 1, 1, ['dana'], 1, 1).is_occupied():
        errors.append('return that the room isn\'t occupied when it is')

    r2 = Room(m1, 1, 1, [], 7, 2)
    r2.clean()
    if r2.clean_level != 9:
        errors.append('doesn\'t clean the room correctly')
    r2.clean()
    if r2.clean_level != 10:
        errors.append(
            'doesn\'t clean the room correctly when the clean_level + rank is over 10')

    if not (Room(m1, 1, 1, [], 2, 1).better_than(Room(m1, 1, 1, [], 1, 1)) and
            not Room(m1, 1, 1, [], 1, 1).better_than(Room(m1, 1, 1, [], 1, 1)) and
            Room(m1, 2, 1, [], 1, 1).better_than(Room(m1, 1, 1, [], 2, 1)) and
            Room(m1, 1, 1, [], 1, 2).better_than(Room(m1, 2, 1, [], 2, 1))):
        errors.append('better than doesn\'t work correctly')

    try:
        Room(m1, 1, 1, [], 1, 1).better_than(1)
        errors.append(
            'should raise an error if better_than receives an other than isn\'t of type Room')
    except TypeError as error:
        if error.args[0] != 'Other must be an instance of Room':
            errors.append(
                'wrongs error message in better_than method, for other that isn\'t of type Room')
    except Exception as error:
        errors.append(
            f'unexpected error from better_then when other isn\'t of type Room, error: {error}')

    try:
        Room(m1, 1, 1, ['dana'], 1, 1).check_in(['daniel'])
    except RoomError as error:
        if error.args[0] != 'Cannot check-in new guests to an occupied room':
            errors.append(
                'wrong error message for check_in into an occupied room')
    except Exception as error:
        errors.append(
            f'unexpected error on check_in into an occupied room, error: {error}')

    r3 = Room(m1, 1, 1, [], 1, 1, 3.5)
    catch_error(lambda: r3.check_in(['DANIEL']),
                errors, 'an error occurred while check_in')
    if r3.guests != ['daniel']:
        errors.append(
            'didn\'t convert the guests names to lowercase on check_in')
    if r3.satisfaction != 1.0:
        errors.append('didn\'t initialize the satisfaction on check_in')

    try:
        Room(m1, 1, 1, [], 1, 1).check_out()
    except RoomError as error:
        if error.args[0] != 'Cannot check-out an empty room':
            errors.append(
                'wrong error message for check_out from an empty room')
    except Exception as error:
        errors.append(
            f'unexpected error on check_out from an empty room, error: {error}')

    r3 = Room(m1, 1, 1, ['daniel'], 1, 1, 3.5)
    catch_error(lambda: r3.check_out(), errors,
                'an error occurred while check_in')
    if r3.guests != []:
        errors.append('didn\'t initialize then list of guests on check_out')
    if r3.floor != 1 or r3.number != 1 or r3.clean_level != 1 or r3.rank != 1 or r3.satisfaction != 3.5:
        errors.append(
            'shouldn\'t change anything but the guests list on check_out')

    try:
        Room(m1, 1, 1, [], 1, 1).move_to(Room(m1, 1, 1, [], 1, 1))
    except RoomError as error:
        if error.args[0] != 'Cannot move guests from an empty room':
            errors.append('wrong error message for move_to of an empty room')
    except Exception as error:
        errors.append(
            f'unexpected error on move_to of an empty room, error: {error}')

    try:
        Room(m1, 1, 1, ['daniel'], 1, 1).move_to(
            Room(m1, 1, 2, ['yael'], 1, 1))
    except RoomError as error:
        if error.args[0] != 'Cannot move guests into an occupied room':
            errors.append(
                'wrong error message for move_to into an occupied room')
    except Exception as error:
        errors.append(
            f'unexpected error on move_to into an occupied room, error: {error}')

    r4 = Room(m1, 1, 1, [], 1, 1, 1.5)
    r5 = Room(m1, 2, 1, [], 1, 1, 1.5)
    r6 = Room(m1, 2, 1, [], 1, 1, 3.5)
    r7 = Room(m1, 1, 1, ['daniel'], 1, 1, 3.5)
    catch_error(lambda: r7.move_to(r4), errors,
                'an error occurred while move_to')
    if r4.guests != ['daniel']:
        errors.append('didn\'t moved the guests on move_to')
    if r4.satisfaction != 3.5:
        errors.append(
            'should update the new room satisfaction to the previous room satisfaction if the other isn\'t better on move_to')
    if r7.guests != []:
        errors.append('didn\'t reset the guests of the room on move_to')
    r7 = Room(m1, 1, 1, ['daniel'], 1, 1, 3.5)
    catch_error(lambda: r7.move_to(r5), errors,
                'an error occurred while move_to')
    if r5.satisfaction != 4.5:
        errors.append(
            'didn\'t update correctly the satisfaction on move_to the a better room')
    r7 = Room(m1, 1, 1, ['daniel'], 1, 1, 4.5)
    catch_error(lambda: r7.move_to(r6), errors,
                'an error occurred while move_to')
    if r6.satisfaction != 5.0:
        errors.append(
            'didn\'t update correctly the satisfaction on move_to the a better room when the satisfaction pass 5.0')

    return errors


def q3_test():
    errors = []
    h1 = Hotel('Dan', [])
    if h1.name != 'Dan':
        errors.append('doesn\'t set the hotel name correctly')
    try:
        h1.rooms
    except:
        errors.append('doesn\'t set the hotel rooms correctly')

    if repr(h1) != 'Dan hotel has:\n0 rooms\n0 occupied rooms':
        errors.append('doesn\'t print the hotel correctly')

    m1 = Minibar({}, {})
    h2 = Hotel('Dan', [Room(m1, 1, 1, [], 1, 1),
                       Room(m1, 1, 1, ['daniel'], 1, 1)])
    if repr(h2) != 'Dan hotel has:\n2 rooms\n1 occupied rooms':
        errors.append(
            'doesn\'t print the hotel number of total and/or occupied room correctly ')
    try:
        res = Hotel('Dan', [Room(m1, 1, 1, ['daniel'], 1, 1)]
                    ).check_in(['yael'], 1)
        if res != None:
            errors.append(
                'should return None on check_in if there is no a matching available room')
    except Exception as error:
        errors.append(
            f'raised an unexpected error when trying to check in and there is no available room, error: {error}')
    try:
        res = Hotel('Dan', [Room(m1, 1, 1, [], 1, 3)]
                    ).check_in(['yael'], 2)
        if res != None:
            errors.append(
                'should check that the rank is equal in addition to the room being empty on check_in')
    except Exception as error:
        errors.append(
            f'raised an unexpected error when trying to check in and there is no available room, error: {error}')

    try:
        r1 = Room(m1, 1, 1, [], 1, 1, 2.0)
        res = Hotel('dan', [r1]).check_in(['daniel', 'yael'], 1)
        if not (isinstance(res, Room) and lists_values_matches(res.guests, r1.guests, ['daniel', 'yael'])):
            errors.append(
                'doesn\'t return the room with the updated guests list')
        if r1.satisfaction != 1.0:
            errors.append(
                'check_in should use the check_in method from the class Room, to initialize the satisfaction')
    except Exception as error:
        errors.append(f'an error has occurred while check_in, error: {error}')

    try:
        res = Hotel('Dan', [Room(m1, 1, 1, [], 1, 3)]
                    ).check_out('yael')
        if res != None:
            errors.append(
                'should return None on check_out if there is no room containing the guest')
    except Exception as error:
        errors.append(
            f'raised an unexpected error when trying to check out a guest that doesn\'t exist, error: {error}')

    try:
        r2 = Room(m1, 1, 1, ['daniel', 'yael'], 1, 1, 2.0)
        res = Hotel('dan', [r2]).check_out('yael')
        if not (isinstance(res, Room) and res.guests == r2.guests == []):
            errors.append(
                'doesn\'t return the room with the empty guests list')
    except Exception as error:
        errors.append(f'an error has occurred while check_in, error: {error}')

    try:
        r = Room(m1, 1, 1, ['yael'], 1, 3)
        Hotel('Dan', [r]
              ).check_out('YAEL')
        if r.guests:
            errors.append(
                'check_out should lowercase the guest name before comparing')
    except Exception as error:
        errors.append(
            f'raised an unexpected error when trying to check out a guest with uppercase, error: {error}')

    try:
        res = Hotel('Dan', [Room(m1, 1, 1, [], 1, 3)]
                    ).upgrade('yael')
        if res != None:
            errors.append(
                'should return None on upgrade if there is no room containing the guest')
    except Exception as error:
        errors.append(
            f'raised an unexpected error when trying to upgrade a guest that doesn\'t exist, error: {error}')

    try:
        res = Hotel('Dan', [Room(m1, 1, 1, ['yael'], 1, 3), Room(m1, 1, 1, [], 1, 3)]
                    ).upgrade('yael')
        if res != None:
            errors.append(
                'should return None on upgrade if there is no better room available')
    except Exception as error:
        errors.append(
            f'raised an unexpected error when trying to upgrade a guest without better rooms available, error: {error}')

    try:
        r3 = Room(m1, 1, 1, ['daniel', 'yael'], 1, 1, 2.0)
        r4 = Room(m1, 1, 1, [], 1, 2, 1.0)
        res = Hotel('dan', [r3, r4]).upgrade('yael')
        if not (isinstance(res, Room) and lists_values_matches(res.guests, r4.guests, ['daniel', 'yael']) and r3.guests == []):
            errors.append(
                'doesn\'t return the room with the empty guests list')
        if r4.satisfaction != 3.0:
            errors.append(
                f'upgrade should use the move_to method from the class Room, to update the satisfaction, error: {error}')
    except Exception as error:
        errors.append('an error has occurred while check_in')

    try:
        r5 = Room(m1, 1, 1, ['yael'], 1, 1)
        Hotel('Dan', [r5, Room(m1, 1, 1, [], 1, 3)]
              ).check_out('YAEL')
        if r5.guests:
            errors.append(
                'upgrade should lowercase the guest name before comparing')
    except Exception as error:
        errors.append(
            f'raised an unexpected error when trying to check out a guest with uppercase, error: {error}')

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

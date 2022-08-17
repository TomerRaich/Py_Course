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

#########################################
# Question 3 supplement - do not delete this comment
#########################################
def test_hotel():
    m = Minibar({'coke': 10, 'lemonade': 7}, {'bamba': 8, 'mars': 12})
    rooms = [Room(m, 15, 140, [], 5, 1), Room(m, 12, 101, ["Ronen", "Shir"], 6, 2),
             Room(m, 1, 2, ["Liat"], 7, 1), Room(m, 2, 23, [], 6, 3)]
    h = Hotel("Dan",rooms)
    test_sep = '\n------------------'
    print('PRINT h:\n', h, test_sep, sep="")
    print(m)
    print('PRINT h:\n', h, test_sep, sep="")
    print('CALL: h.upgrade("Liat")\n', h.upgrade("Liat"), test_sep, sep="")
    print('CALL: h.check_out("Ronen")\n', h.check_out("Ronen"), test_sep,  sep="")
    print('CALL: h.check_out("Ronen")\n', h.check_out("Ronen"), test_sep, sep="")
    print('CALL: h.check_in(["Alice", "Wonder"], 2)\n', h.check_in(["Alice", "Wonder"], 2), test_sep, sep="")
    print('CALL: h.check_in(["Alex"], 3)\n', h.check_in(["Alex"], 3), test_sep, sep="")
    print('PRINT h:\n', h, test_sep, sep="")
    print('CALL: h.check_in(["Oded", "Shani"], 3)\n', h.check_in(["Oded", "Shani"], 3), test_sep, sep="")
    print('CALL: h.check_in(["Oded", "Shani"], 1)\n', h.check_in(["Oded", "Shani"], 1), test_sep, sep="")
    print('CALL: h.check_out("Liat")\n', h.check_out("Liat"), test_sep, sep="")
    print('CALL: h.check_out("Liat")\n', h.check_out("Liat"), test_sep, sep="")
    print('PRINT h:\n', h, test_sep, sep="")


#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################
if __name__ == "__main__":
    ##test_hotel() ## After you are done implenting all classes and methods, you may comment-in the call to test_hotel() and compare the results with the
   
  test_hotel()
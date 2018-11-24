from pprint import pprint as p

class Flight:

    def __init__(self, num, aircraft):
        if not num[:2].isalpha():
            raise ValueError("No Airline Code in Flight Number")
        if not num[:2].isupper():
            raise ValueError("The Flight code should be Upper case")
        if not (num[2:].isnumeric() and int(num[2:])<= 9999):
            raise ValueError("Invalid Route Code")
        self._number = num
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()

        self._seating = [None] + [{letter:None for letter in seats} for _ in rows]

    def number(self):
        return self._number
    def airline(self):
        return self._number[:2]
    def aircraft_model(self):
        return self._aircraft.model()
    def _parse_seat(self, seat):
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError('Invalid Seat letter')
        row_num = seat[:-1]
        try:
            row = int(row_num)
        except:
            raise ValueError('Invalid Row Number')

        if row not in rows:
            raise ValueError('Row Number is not in aircraft')
        return row, letter

    def allocate_seat(self, seat, pessenger):

        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError('Seat is already occupied')

        self._seating[row][letter] = pessenger
    def relocate_passenger(self, from_seat, to_seat):

        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError('No pessenger to relocate')

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError('Seat is already occupied')

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_avai_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                    for row in self._seating
                    if row is not None)
    def make_boarding_cards(self, card_printer):
        for pessenger, seat in sorted(self._pessenger_seats()):
            card_printer(pessenger, seat, self.number(), self.aircraft_model())

    def _pessenger_seats(self):
        rows, letters = self._aircraft.seating_plan()
        for row in rows:
            for letter in letters:
                pessenger = self._seating[row][letter]
                if pessenger is not None:
                    yield (pessenger, "{}{}".format(row, letter))


class Aircraft:
    def __init__(self, registation):
        self._registration = registation

    def registration(self):
        return self._registration

    def num_seats(self):
        return self._num_rows(self._num_seats_per_row)

class Boeing777(Aircraft):

    def model(self):
        return 'Boeing777'

    def seating_plan(self):
        return (range(1, 20), "ABCDEFGHJ")

class AirBus320(Aircraft):

    def model(self):
        return 'AirBus320'

    def seating_plan(self):
        return (range(1, 56), "ABCDEF")





def console_card_printer(pessenger, seat, flight_number, aircraft):
    output = "| Name: {0}" \
            "   Flight: {1}"\
            "   Seat: {2}"\
            "   Aircraft: {3}" \
            "   |".format(pessenger, flight_number, seat, aircraft)
    banner = "+" + "-"*(len(output)-2) + "+"
    border = "|" + " "*(len(output)-2) + "|"
    lines = [banner, border, output, banner, border]
    card = "\n".join(lines)
    print(card)
    print()

def main():
    aircraft = AirBus320(registation='6E303')
    f= Flight('IN2345', aircraft)
    print(aircraft.model(), aircraft.seating_plan(), aircraft.registration())
    print(f.aircraft_model())
    f.allocate_seat('12C', 'Prem Kashyap')
    f.allocate_seat('12E', 'Raghwendra Rathod')
    f.relocate_passenger('12C', '12D')
    p(f._seating)
    p(f.num_avai_seats())
    f.make_boarding_cards(console_card_printer)


if(__name__ == "__main__"):
    main()
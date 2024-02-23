'''
    Program purpose: reservation hotel for customers (users)
    Programmer: NOORALIA EVIEANNA SOFEA
    Date: 23 February 2024
'''

print("WELCOME TO FAIRVIEW HOTEL")

#price list of hotel's room
single = 100.00
double = 150.00
suite = 250.00

# Define rates
room_rates = {'Single': 100, 'Double': 150, 'Suite': 250}

while True:
    room_type = input("Choose your room either its Single or Double or Suite: ").lower()
    number_rooms = int(input("Enter a number of room for your reserve: "))

    # Apply discounts and promotions
    if number_rooms > 5:
        total*= 0.9  # 10% discount
        print("You got 10% of discount !")
    else:
        print("Sorry you didn't get any discount. ")

    if room_type == 'single':
        total = single * number_rooms
        if number_rooms > 7:
            print("CONGRATS! You get a free breakfast voucher.")

    elif room_type == 'double':
        total = double * number_rooms
        if number_rooms > 7:
            print("SORRY! You didn'tt get a free breakfast voucher.")

    elif room_type == 'suite':
        total = suite * number_rooms
        if number_rooms > 7:
            print("SORRY! You didn't get a free breakfast voucher.")

    if number_rooms > 5:
        total_discount = total * 0.1
        total = total_discount

    print("Type of room: ", room_type)
    print("Number of rooms to reserve: ", number_rooms)
    print("The total cost :",total)
    break

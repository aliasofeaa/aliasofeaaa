'''
    Program purpose: reservation hotel for customers (users)
    Programmer: NOORALIA EVIEANNA SOFEA
    Date: 23 February 2024
'''

print("Welcome to FairviewHotel")

# Define rates
room_rates = {'Single': 100, 'Double': 150, 'Suite': 250}

# Prompt user to select room type
while True:
    room_type = input("Enter room type (Single/Double/Suite): ")
    if room_type in room_rates:
        break
    else:
        print("Invalid room type. Please choose based on the option only !")

# Prompt user to enter number of rooms
while True:
    number_rooms = input("Enter number of rooms: ")
    if number_rooms.isdigit() and int(number_rooms) > 0:
        break
    else:
        print("Invalid number of rooms. Please enter a valid number !")

# Prompt user to enter number of nights
while True:
    number_nights = input("Enter number of nights: ")
    if number_nights.isdigit() and int(number_nights) > 0:
        break
    else:
        print("Invalid number of nights. Please enter a valid number !")

number_rooms = int(number_rooms)
number_nights = int(number_nights)
rate = room_rates[room_type]

# Calculate total cost
total_cost = rate * number_rooms * number_nights

# Apply discounts and promotions
if number_rooms > 5:
    total_cost *= 0.9  # 10% discount
    print("You got 10% of discount !")
else:
    print("Sorry you didn't get any discount. ")
if room_type == 'Single' and number_nights > 7:
    print("Congratulations! You've got a complimentary breakfast voucher.")
else:
    print("Sorry you didn't get any complimentary breakfast voucher ")
if room_type == 'Suite' and number_nights < 3:
    print("Minimum stay for a Suite is 3 nights.")
    total_cost = None

if total_cost is not None:
    print("Total cost of reservation: RM", total_cost)

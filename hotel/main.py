'''
    Program purpose: reservation hotel for customers (users)
    Programmer: NOORALIA EVIEANNA SOFEA
    Date: 23 February 2024
'''

print("Welcome to FairviewHotel")

# Define rates
room_rates = {'Single': 100, 'Double': 150, 'Suite': 250}

# Ask user to select their room type
while True:
    room_type = input("Enter room type (Single/Double/Suite): ")
    if room_type in room_rates:
        break
    else:
        print("Invalid room type. Please choose based on the option only !")

# Ask user to enter number of rooms
while True:
    num_rooms = input("Enter number of rooms: ")
    if num_rooms.isdigit() and int(num_rooms) > 0:
        break
    else:
        print("Invalid number of rooms. Please enter a valid number !")

# Ask user to enter how many nights they want to stay
while True:
    num_nights = input("Enter number of nights: ")
    if num_nights.isdigit() and int(num_nights) > 0:
        break
    else:
        print("Invalid number of nights. Please enter a valid number !")

num_rooms = int(num_rooms)
num_nights = int(num_nights)
rate = room_rates[room_type]

# Calculate total cost
total_cost = rate * num_rooms * num_nights

# Apply discounts and promotions
if num_rooms > 5:
    total_cost *= 0.9  # 10% discount
    print("You got 10% of discount !")
else:
    print("Sorry you didn't get any discount. ")
if room_type == 'Single' and num_nights > 7:
    print("Congratulations! You've got a complimentary breakfast voucher.")
else:
    print("Sorry you didn't get any complimentary breakfast voucher ")
if room_type == 'Suite' and num_nights < 3:
    print("Minimum stay for a Suite is 3 nights.")
    total_cost = None

if total_cost is not None:
    print("Total cost of reservation: RM", total_cost)

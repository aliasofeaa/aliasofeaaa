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
    num_rooms = input("Enter number of rooms: ")
    if num_rooms.isdigit() and int(num_rooms) > 0:
        break
    else:
        print("Invalid number of rooms. Please enter a valid number !")

# Prompt user to enter number of nights
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
if room_type == 'Single' and num_nights > 7:
    print("Congratulations! You've got a complimentary breakfast voucher.")
if room_type == 'Suite' and num_nights < 3:
    print("Minimum stay for a Suite is 3 nights.")
    total_cost = None

if total_cost is not None:
    print("Total cost of reservation: RM", total_cost)

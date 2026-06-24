#Prompt user to enter the number of seats
num_seats = int(input("Enter the number of seats on the train: "))
#Create a list representing the seats; set to False for empty
seats = [False] * num_seats

#Validate the user input
while True:
    try:
        #Prompt user to select an action
        selection = input("What would you like to do? (Book / Cancel / View / Group / Quit): ").capitalize()
        if selection == "Book":
            #Prompt user to book a seat
            book_seat = int(input(f"Enter the seat number you want to book (1-{num_seats}): "))
            index = book_seat - 1
            if index < 0 or index >= num_seats:
                print(f"Invalid seat number. Please choose between 1 and {num_seats}.")
            elif seats[index]:
                print("The seat is already occupied. Select another seat.")
            else:
                seats[index] = True
                print(f"You have booked seat no. {book_seat}.")
        elif selection == "Cancel":
            #Prompt user to select the seat to cancel
            cancel_seat = int(input(f"Enter the seat number you want to cancel (1-{num_seats}): "))
            index = cancel_seat - 1
            if index < 0 or index >= num_seats:
                print(f"Invalid seat number. Please choose between 1 and {num_seats}.")
            elif not seats[index]:
                print(f"This seat was not booked. Please try again with another seat number.")
            else:
                seats[index] = False
                print(f"Seat no. {cancel_seat} has been canceled.")
        elif selection == "View":
            free_seats = [str(i + 1) for i, booked in enumerate(seats) if not booked]
            booked_seats = [str(i + 1) for i, booked in enumerate(seats) if booked]
            if not booked_seats:
                print("No seats have been booked.")
            elif not free_seats:
                print("All seats have been booked.")
            else:
                print(f"Free seats: {', '.join(free_seats)}.")
                print(f"Booked seats: {', '.join(booked_seats)}.")
        elif selection == "Quit":
            total_booked = sum(seats)
            print(f"Total booked seats: {total_booked}")
            total_free = num_seats - total_booked
            print(f"Total free seats: {total_free}")
            occupancy = total_booked / num_seats * 100
            print(f"Occupancy: {occupancy:.2f}%.")
            print("Quitting the app. Bye!")
            break
        #Option for selecting 2 or more adjacent seats
        elif selection == "Group":
            book_group = int(input("How many seats do you want to book as a group? "))
            start_seat = int(input(f"Enter the starting seat (1-{num_seats}): "))
            index = start_seat - 1
            if index < 0 or index + book_group > num_seats:
                print("Invalid group of seats. Please choose a different starting seat or smaller group size.")
            elif not all(not seats[i] for i in range(index, index + book_group)):
                print("Not all seats in that block are free. Please choose a different starting seat.")
            else:
                for i in range(index, index + book_group):
                    seats[i] = True
                booked_group = [str(i + 1) for i in range(index, index + book_group)]
                print(f"You have booked seats no. {', '.join(booked_group)}.")
        else:
            print("Invalid option. Please choose Book, Cancel, View, Group or Quit.")
    except ValueError:
        print("Invalid input. Please enter a number where required.")
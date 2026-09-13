#Print header and separator
print("<-- Museum Ticket Counter -->")
print("-----------------------------")

#Create empty list to store the visitors' names, the ticket type and the price paid
museum = []
#Create list with the pizza sizes
tickets = ["Adult", "Child", "Senior"]
#Prompt user to enter the number of visitors for the day
while True:
    try:
        num_visitors = int(input("Enter the number of visitors recorded today: "))
        if num_visitors <= 0:
            print("The number of visitors cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop over the number of visitors
for i in range(num_visitors):
    #Loop for validating the visitor's name
    while True:
        #Prompt user to enter the visitor's name
        visitor_name = input(f"Enter the name of visitor {i + 1}: ").strip().title()
        #Check that the name entered is not empty
        if visitor_name == "":
            print("The name cannot be empty. Please try again.")
            continue
        if not visitor_name.replace(" ", "").isalpha():
            print("The name cannot contain digits. Please try again.")
            continue
        break
    #Prompt user to enter a ticket type
    while True:
        ticket_type = input(f"Enter the ticket for {visitor_name}: ").strip().capitalize()
        #Check that the ticket type is entered correctly
        if ticket_type not in tickets:
            print("The ticket type must be Adult, Child or Senior. Please enter a correct type.")
            continue
        break
    #Loop for validating the price paid
    while True:
        try:
            #Prompt user to enter the price paid per ticket
            price = float(input(f"Enter the price paid by {visitor_name} for a {ticket_type} ticket: $"))
            #Check that the price value is positive
            if price <= 0:
                print("The price must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Add visitor name, ticket type and price to the pizza museum list
    museum.append((visitor_name, ticket_type, price))

#Print header
print("\n<-- MUSEUM TICKETS SOLD TODAY -->")
#Loop over the museum list
for i, (visitor_name, ticket_type, price) in enumerate(museum, start = 1):
    #Print the visitor name, ticket type and price
    print(f" {i}. {visitor_name} - {ticket_type} ticket - ${price:.2f}.")

#Calculate the total revenue from all the tickets sold
total_tickets = sum(price for visitor_name, ticket_type, price in museum)
print(f"  Total revenue from tickets sold today: ${total_tickets:.2f}")

#Print header
print("\n<-- CHILDREN VISITORS -->")
#Find and print all child tickets sold
children = [visitor_name for visitor_name, ticket_type, price in museum if ticket_type == "Child"]
if len(children) == 0:
    print("There were no children in the museum today.")
elif len(children) == 1:
    print(f"There was only 1 child at the museum today:")
else:
    print(f"There were {len(children)} children at the museum today:")
# Print the names once, regardless of which branch ran above
for visitor_name in children:
    print(f" {visitor_name}")

#Find the most expensive ticket sold
print()
top_price = max(museum, key=lambda x: x[2])[2]
top_tickets = [(visitor_name, ticket_type, price) for visitor_name, ticket_type, price in museum if price == top_price]
if len(top_tickets) == 1:
    top_visitor, top_ticket_type, top_ticket_price = top_tickets[0]
    print(f"{top_visitor} got the most expensive ticket: {top_ticket_type} ticket, for ${top_ticket_price:.2f}.")
else:
    names = ', '.join(f"{visitor} ({ticket} ticket - ${ticket_price:.2f})" for visitor, ticket, ticket_price in top_tickets)
    print(f"The most expensive tickets (${top_price:.2f}) were bought by: {names}.")

#Print header
print("\n<-- TOTAL REVENUE PER TICKET TYPE -->")
#Create dictionary for aggregating total revenue per ticket type
tickets_totals = {}
for visitor_name, ticket_type, price in museum:
    tickets_totals[ticket_type] = tickets_totals.get(ticket_type, 0) + price
#Sort the dictionary by ticket type, descending, and print as a leaderboard
sorted_categories = sorted(tickets_totals.items(), key = lambda x: x[1], reverse = True)
for rank, (ticket_type, total) in enumerate(sorted_categories, start = 1):
    print(f" {rank}. {ticket_type} ticket - ${total:.2f} ({((total / total_tickets) * 100):.1f}%)")
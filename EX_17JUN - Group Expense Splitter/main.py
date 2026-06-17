#Prompt the user for the number of group members
num_members = int(input("Enter the number of members in the group: "))
#Create empty list for holding the names and money spent
group = []
#Loop through the number of members
for i in range(num_members):
    #Prompt user to enter the name of the group member
    member_name = input(f"Enter name for group member {i + 1}: ").title()
    #Prompt user to enter the amount spent by the member
    member_amount = float(input(f"Enter the amount spent ($): "))
    #Add the name and amount to the list as tuples
    group.append((member_name, member_amount))

#Print section title
print("\nGroup members and amounts spent")
#Loop through the group list
for i, (member_name, member_amount) in enumerate(group, start = 1):
    #Print each member and the amount spent
    print(f"{i}. {member_name} has spent ${member_amount}")

#Declare variable for total amount and initialize it
total_amount = 0
#Loop through the names and amounts in the group
for member_name, member_amount in group:
    #Add each member amount to the total amount
    total_amount += member_amount
#Print the total amount spent
print(f"\nTotal amount spent: ${total_amount}")
#Calculate the fair share of each member
fair_share = total_amount / num_members
#Print the fair share for each member
print(f"\nFair share for each group member: ${fair_share:.2f}")
#Loop through the names and amounts in the group
for member_name, member_amount in group:
    #Set condition for amount spent greater than the fair share
    if member_amount > fair_share:
        #Print how much the member is owed
        print(f" -> {member_name} is owed ${(member_amount - fair_share):.2f}")
    #Set condition for amount spent smaller than the fair share
    elif member_amount < fair_share:
        #Print how much the member owes
        print(f" -> {member_name} owes ${(fair_share - member_amount):.2f}")
    #Set condition for amount spent equal to the fair share
    else:
        #Print message that the member has met his/her fair share
        print(f" -> {member_name} has met his/her fair share.")

#Build the list of balances
member_balances = [(name, amount - fair_share) for name, amount in group]
#Loop through the balances list
for name, balance in member_balances:
    #Print each member and the balance
    print(f"\nBalance for {name}: ${balance:.2f}")
    #Set condition for negative balance
    if balance < 0:
        print(f" -> {name} owes ${abs(balance):.2f}")
    #Set condition for positive balance
    else:
        print(f" -> {name} is owed ${abs(balance):.2f}")

#Print section title
print("\nGroup members and balances:")
#Sort people from "owes the most" to "gets back the most" before printing the summary
sorted_balances = sorted(member_balances, key = lambda x: x[1])
#Loop through the sorted balances
for i, (name, balance) in enumerate(sorted_balances, start = 1):
    #Print each member and the balance
    print(f"{i}. {name} - ${balance:.2f}")
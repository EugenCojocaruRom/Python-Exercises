#Print header and separator
print("<-- ATM Transaction Tracker -->")
print("-------------------------------")

#Prompt user to enter the starting balance
initial_balance = float(input("Enter initial balance ($): "))
#Set the current balance as the initial balance
current_balance = initial_balance
#Create empty list to store the transaction name and the amount
transactions = []
#Declare variable as counter for rejected transactions
rejected_count = 0
#Initiate loop to allow the user to enter transactions
while True:
    #Prompt user to enter an amount
    user_input = input("Enter transaction amount (or 'done' to finish): ")
    if user_input.lower() == "done":
        break
    elif user_input == "":
        print("Please enter a transaction amount.")
        continue
    transaction_amount = float(user_input)
    #Reject withdrawals that would overdraw the account
    if transaction_amount < 0 and current_balance + transaction_amount < 0:
        #Increment the rejected count
        rejected_count += 1
        print("Insufficient funds. Please enter another amount.")
    #Set condition for deposit
    elif transaction_amount > 0:
        current_balance += transaction_amount
        #Add transaction to the list
        transactions.append(("deposit", transaction_amount, current_balance))
        # Print informative message
        print(f"Current balance: ${current_balance:.2f}")
    #Set condition for withdrawal
    elif transaction_amount < 0:
        current_balance += transaction_amount
        #Add transaction to the list
        transactions.append(("withdrawal", transaction_amount, current_balance))
        if transaction_amount < -300:
            print(f"Current balance: ${current_balance:.2f} ->⚠️ Large withdrawal")
        else:
            print(f"Current balance: ${current_balance:.2f}")
    #Zero amount
    else:
        print("Please add an amount different from zero.")

#Print separator
print("----------------------------")
#Loop over the transactions list
for i, (t_type, amount, balance) in enumerate(transactions, start = 1):
    #Print each transaction alongside the amount and the balance
    line = f"{i}. {t_type.capitalize():<12} {amount:+.2f} -> ${balance:.2f}"
    if amount < -300:
        line += " ⚠️ Large withdrawal"
    elif amount >= 300:
        line += " ⚠️ Large deposit"
    print(line)

#Calculate the total deposited
deposits = [amount for t_type, amount, balance in transactions if t_type == "deposit"]
total_deposit = sum(deposits)
#Calculate the total withdrawn
withdrawals = [amount for t_type, amount, balance in transactions if t_type == "withdrawal"]
total_withdrawn = sum(withdrawals)
#Find the biggest transaction
biggest_transaction = max(transactions, key=lambda t: abs(t[1]))
#Print separator and header
print("----------------------------")
print("<-- Transactions Summary -->")
#Print the totals - deposits, withdrawals, rejected
print(f"Total deposited: ${total_deposit:.2f}")
print(f"Total withdrawn: ${abs(total_withdrawn):.2f}")
print(f"Rejected withdrawal attempts: {rejected_count}")
print(f"Biggest transaction: {biggest_transaction[0].capitalize()} of ${abs(biggest_transaction[1]):.2f}")
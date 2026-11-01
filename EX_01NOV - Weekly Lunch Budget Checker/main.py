#Print header and separator
print("<== Weekly Lunch Budget Checker ==>")
print("-----------------------------------")

#Have a list of days
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
#Create empty list for storing the prices (amount spent each day)
prices = []
#Loop over the list of days
for day in days:
    #Loop for validating the amount spent per day
    while True:
        try:
            #Prompt user to enter the amount spent per day
            spent_daily = float(input(f"Enter the amount spent on {day}: "))
            #Check that the amount is not negative
            if spent_daily < 0:
                print("The amount spent must be at least 0. Please try again.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Add the daily amount to the prices list
    prices.append(spent_daily)

#Loop for validating the daily budget
while True:
    try:
        #Prompt user to enter the daily budget
        daily_budget = float(input(f"Enter the daily budget: "))
        #Check that the amount is not negative
        if daily_budget < 0:
            print("The daily budget must be at least 0. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")

print()
#Loop over the days and amounts spent and print a list
for index, price in enumerate(prices):
    if price <= daily_budget:
        print(f"{days[index]}: ${price:.2f} - OK")
    else:
        print(f"{days[index]}: ${price:.2f} - OVER by ${(price - daily_budget):.2f}")

print()
#Filter the over-budget prices
over_budget = [price for price in prices if price > daily_budget]
#Calculate the total spent for the week
week_total = sum(prices)
#Calculate the average spent per day
daily_avg = week_total / len(days)
#Print the over budget prices, the weekly total, the daily average and the number of days over budget
print(f"Over-budget prices: {over_budget}")
print(f"Total spent this week: ${week_total:.2f}")
print(f"Daily average: ${daily_avg:.2f}")
#Set conditions for displaying the days over budget
if not over_budget:
    print("No days over budget.")
elif len(over_budget) == 1:
    print(f"Only 1 day over budget.")
else:
    print(f"Days over budget: {len(over_budget)}")

#Compare the total to the weekly budget and print a message
weekly_budget = daily_budget * len(days)
if week_total < weekly_budget:
    print(f"Under weekly budget by ${(weekly_budget - week_total):.2f}.")
elif week_total == weekly_budget:
    print("Great! You managed to fit exactly in your weekly budget!")
else:
    print(f"Over weekly budget by ${(week_total - weekly_budget):.2f}.")

#Find and print the most expensive day
most_expensive = days[prices.index(max(prices))]
print(f"Most expensive day: {most_expensive}")
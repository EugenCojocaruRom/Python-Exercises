#Loop for as long as the condition is true
while True:
    try:
        #Prompt the user to provide the number of entries
        num_logs = int(input("How many IP entries do you want to input? "))
        #Set condition exiting the loop -> only if there is a valid, positive number
        if num_logs > 0:
            break
        #If num_logs is 0 or negative, skip the break and display this error
        print("Please enter a number greater than 0.")
    except ValueError:
        #Display message in case the user enters anything else than int
        print("Invalid input. Please enter a whole number.")

#Create empty list to hold tuples -> ip, status
raw_logs = []

#Prompt the user to enter the IP and Status separately
print("\nEnter the details for each network device:")
#Loop through the number of logs
for i in range(num_logs):
    #Print section title
    print(f"\n--- Device {i + 1} ---")
    #Prompt user to enter the IP (and remove any extra spaces)
    ip = input("Enter IP Address: ").strip()
    #Prompt user to enter the status (and remove any extra spaces)
    status = input("Enter Status Code: ").strip()

    #Add IP and status to the raw logs list as a pair
    raw_logs.append((ip, status))

#Filter the flagged logs using IP and status
flagged_logs = [
    (line_num, ip, status)
    for line_num, (ip, status) in enumerate(raw_logs, start=1)
    if status != "200"
]

#Display the final scan results
print("\n--- SCAN RESULTS ---")
#Set condition for the case when the log is not in the flagged logs list
if not flagged_logs:
    #Print message
    print("All green! No network anomalies detected.")
else:
    #Loop through the flagged logs list
    for line, ip, status in flagged_logs:
        #Print message with log line, IP and status
        print(f"Line {line}: Flagged IP {ip} (Status: {status})")